from django.shortcuts import render, redirect
from .forms import FirstForm
from django.contrib import messages
from .models import Form, FilledForms
from django.http import HttpResponse
from .utils.helper import check_values_for_add_form
import shutil
import sys, errno 

# from django.core.files.uploadedfile import InMemoryUploadedFile
 

def index(request):
    forms = Form.objects.all()
    context = {
        'title':'Create your own form',
        'forms': forms
    }
    if request.method == 'POST':
        form = FirstForm(request.POST)
        check_url = Form.objects.filter(url=form['url'].value()).first()
        if check_url:
            messages.warning(request, 'Url is available')
            return redirect('/forms')
        else:
            if form.is_valid():
                print(form['fullname'].value())
                new_form = Form.objects.create(email=form['email'].value(), url=form['url'].value(), fullname=form['fullname'].value(), form_name=form['form_name'].value())
                new_form.save()
                form_url = Form.objects.filter(url=form['url'].value()).first()
                return redirect(f'/forms/{form_url.id}')
    return render(request, 'index.html', context)


def create_values_for_form(request, pk=None):
    form_pk = Form.objects.filter(id=pk).first()
    files_path = f'/static/'
    if form_pk:
        context = {
            'title':f' {form_pk.form_name}',
            'url':form_pk.url,
            'author':form_pk.fullname,
            'files_path':files_path
        }
        if request.method == 'POST':
            # print(check_values_for_add_form(request, pk, form_pk))
            Form.objects.filter(id=pk).update(values=check_values_for_add_form(request, pk, form_pk))
            messages.success(request, 'Form created')
            return redirect("/forms")
        return render(request, 'add_values.html', context)
    else:
        messages.warning(request, 'Form not found')
        return redirect('/forms')


def fill_form(request, pk, form_pk):
    form_keys = ['checkbox_field_', 'selectbox_field_', 'question_field_']
    form = (request.POST or None)
    my_dict = {}
    for key, add_item in form.items():
        # print(f"key: {key} | value: {add_item}")
        key_parts = key.split("_")
        if key == 'csrfmiddlewaretoken':
            continue
        if key == 'email':
            if len(add_item) < 4 or "@" not in add_item:
                messages.warning(request, 'Wrong email')
                return redirect(f"/forms/{form_pk.id}/view")
            email = add_item
            continue
        elif key == 'name':
            if len(add_item) < 1:
                messages.warning(request, 'Name cannot be empty')
                return redirect(f"/forms/{form_pk.id}/view")
            fullname = add_item
            continue
        field_name = "_".join(key_parts[:3])
        # if len(add_item) < 1:
        #     messages.warning(request, 'Inputs cannot be empty')
        #     return redirect(f"/forms/{form_pk.id}/view")
        if field_name[0:-1] not in form_keys:
            messages.warning(request, 'Something went wrong')
            return redirect(f"/forms/{form_pk.id}/view")
        if field_name not in my_dict:
            my_dict[field_name] = []
        my_dict[field_name].append(add_item)

    FilledForms.objects.create(email=email, fullname=fullname, filled_form=my_dict, form_id_id=form_pk.id)
    Form.objects.filter(id=form_pk.id).update(forms_count=form_pk.forms_count+1)
    messages.success(request, 'Form filled successfull')
    return redirect('/forms')


def get_form(request, pk=None):
    form_pk = Form.objects.filter(id=pk).first()
    images_path = f'/static/media/{pk}/'
    for k, i in form_pk.values.items():
        print(i)
    if form_pk:
        values = form_pk.values
        if len(values) < 1:
            messages.warning(request, 'The form is empty, fill in your information')
            return redirect(f'/forms/{form_pk.id}')
        if request.method == 'POST':
            fill_form(request, pk, form_pk)

        context = {
            'title':form_pk.form_name,
            'id':form_pk.id,
            'url':form_pk.url,
            'author':form_pk.fullname,
            'data':values,
            'images_path':images_path
        }
        return HttpResponse(render(request, 'form.html', context))
    else:
        messages.warning(request, 'Form not found')
        return redirect('/forms')


def get_the_list_of_filled_form(request, pk=None):
    form_pk = FilledForms.objects.filter(form_id_id=pk).all()
    get_form = Form.objects.filter(id=pk).first()
    if form_pk:
        context = {
            'title':get_form.form_name,
            'id':get_form.id,
            'url':get_form.url,
            'author':get_form.fullname,
            "data":form_pk
        }
        return render(request, 'list_filled.html', context)
    else:
        messages.warning(request, f'No form has been filled for the "{get_form.form_name}"')
        return redirect('/forms')


def get_filled_form(request, pk=None, wk=None):
    form_pk = FilledForms.objects.filter(form_id_id=pk).all()

def delete_filled_form(request, pk=None):
    form_pk = FilledForms.objects.filter(id=pk).first()
    forms_count = Form.objects.filter(id=form_pk.form_id_id).first()
    name = form_pk.fullname
    referer = request.META.get('HTTP_REFERER')
    if form_pk:
        delete_this_form = FilledForms.objects.filter(id=pk)
        delete_this_form.delete()
        Form.objects.filter(id=form_pk.form_id_id).update(forms_count=forms_count.forms_count-1)
        messages.success(request, f'The form filled by {name} has been deleted')
        return redirect(referer)
    else:
        messages.warning(request, 'Form not found')
        return redirect('/forms')


def delete_form(request, pk=None):
    form_pk = Form.objects.filter(id=pk).first()
    images_path = f'static/media/{pk}/'
    if form_pk:
        Form.objects.filter(id=pk).delete()
        shutil.rmtree(images_path, ignore_errors=True)
        messages.warning(request, f'The form with the {form_pk.url} has been deleted')
        return redirect('/forms')
    else:
        messages.warning(request, 'Form not found')
        return redirect('/forms')