from django.shortcuts import render, redirect
from .forms import FirstForm
from django.contrib import messages
from .models import Form, FilledForms
from django.http import HttpResponse, JsonResponse
from .utils.helper import check_values_for_add_form, fill_form
import shutil
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
                # print(form['fullname'].value())
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
            Form.objects.filter(id=pk).update(values=check_values_for_add_form(request, pk, form_pk))
            messages.success(request, 'Form created')
            return redirect("/forms")
        return render(request, 'add_values.html', context)
    else:
        messages.warning(request, 'Form not found')
        return redirect('/forms')


def get_form(request, pk=None):
    form_pk = Form.objects.filter(id=pk).first()
    images_path = f'/static/media/{pk}/'
    if form_pk:
        values = form_pk.values
        if len(values) < 1:
            messages.warning(request, 'The form is empty, fill in your information')
            return redirect(f'/forms/{form_pk.id}')
        context = {
            'title':form_pk.form_name,
            'id':form_pk.id,
            'url':form_pk.url,
            'author':form_pk.fullname,
            'data':values,
            'images_path':images_path
        }
        #### filled form post request
        if request.method == 'POST':
            my_dict = fill_form(request, pk, form_pk)
            if type(my_dict) == dict:
                FilledForms.objects.create(filled_form=fill_form(request, pk, form_pk), form_id_id=form_pk.id)
                Form.objects.filter(id=form_pk.id).update(forms_count=form_pk.forms_count+1)
                messages.success(request, 'Form filled successfull')
                return redirect('/forms')
            else:
                return redirect(f"/forms/{form_pk.id}/view")

       
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
    form_pk = Form.objects.filter(id=pk).first()
    if form_pk:
        filled = FilledForms.objects.filter(id=wk).first()
        if filled:
            context = {
            'title':form_pk.form_name,
            'id':form_pk.id,
            'url':form_pk.url,
            'author':form_pk.fullname,
            "data":form_pk.values,
            "filled":filled
            }
            if len(filled.filled_form) < 1:
                messages.warning(request, 'Form is empty')
                return redirect(f'/forms/{form_pk.id}/list')
            # print("form_pk len", len(form_pk.values))
            print("form_pk", form_pk.values)
            # print("form >>>", filled.filled_form)
            # print("form len >>>", len(filled.filled_form))

            # messages.warning(request, 'var')
            return render(request, 'get_filled_form.html', context)
        messages.warning(request, 'Form not found')
        return redirect('/forms')
    messages.warning(request, 'Form not found')
    return redirect('/forms')


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