from django.shortcuts import render, redirect
from .forms import FirstForm
from django.contrib import messages
from .models import Form, FilledForms
from django.http import HttpResponse
import os, uuid, shutil
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


def check_image_upload_errors(request, form_pk):
    for i in request.FILES.keys():
        fileitem = request.FILES[i]
        extension = fileitem.name.split('.')[-1]
        image_extensions = ['jpeg','jpg','png']
        if fileitem.size > 1024000:
            message = 'Image can be max 1024kb'
            return {'message':{'error':message}}
        elif extension not in image_extensions:
            message = 'Only "jpg", "jpeg", "png" images are allowed'
            return {'message':{'error':message}}
        else:
            return {'message':{'success':'Image ok'}}



def image_upload(request, pk, form_pk, my_dict):
    image_path = f'static/media/{pk}'
    if os.path.exists(f'static/media/{pk}'):
        pass
    else:
        os.mkdir(f'static/media/{pk}')
    for i in request.FILES.keys():
        fileitem = request.FILES[i]
        extension = fileitem.name.split('.')[-1]
        if fileitem.name:
            image_name = f'{uuid.uuid4()}.{extension}'
            open(f'{image_path}/{image_name}', 'wb').write(fileitem.file.read())
    for file_key, file_item in request.FILES.items():
        files_key_parts = file_key.split("_")
        files_field_name = "_".join(files_key_parts[:3])
        last_field_name = "_".join(files_key_parts[-2:])
        if 'uploaded_image' not in my_dict[files_field_name].keys():
            my_dict[files_field_name] = {'uploaded_image':[]}
        else:
            if last_field_name == 'uploaded_image':
                my_dict[files_field_name].get('uploaded_image').append(image_name)


def create_values_for_form(request, pk=None):
    form_pk = Form.objects.filter(id=pk).first()
    if form_pk:
        context = {
            'title':f' {form_pk.form_name}',
            'url':form_pk.url,
            'author':form_pk.fullname,
        }
        form_keys = ['checkbox_field_', 'selectbox_field_', 'question_field_']
        if request.method == 'POST':
            my_dict = {}
            form = (request.POST or None)
            if len(form) < 2:
                messages.warning(request, 'Form is empty')
                return redirect(f"/forms/{form_pk.id}")
            for key, add_item in form.items():
                key_parts = key.split("_")
                if key == 'csrfmiddlewaretoken':
                    continue
                field_name = "_".join(key_parts[:3])
                if len(add_item) < 1:
                    messages.warning(request, 'Inputs cannot be empty')
                    return redirect(f"/forms/{form_pk.id}")
                if field_name[0:-1] not in form_keys:
                    messages.warning(request, 'Something went wrong')
                    return redirect(f"/forms/{form_pk.id}")
                if field_name not in my_dict:
                    my_dict[field_name] = {'title':'','image':[],'uploaded_image':[],'youtube':[],'url':[],'values':[]}

                if key_parts[-1] == 'title':
                    title = {'title':add_item}
                    my_dict[field_name].update(title)
                elif key_parts[-1] == 'image':
                    my_dict[field_name].get('image').append(add_item)
                elif key_parts[-1] == 'youtube':
                    my_dict[field_name].get('youtube').append(add_item)
                elif key_parts[-1] == 'url':
                    my_dict[field_name].get('url').append(add_item)
                elif key_parts[-1] == 'values':
                    my_dict[field_name].get('values').append(add_item)
            
            check_image_upload_errors(request, form_pk)
            if 'error' in check_image_upload_errors(request, form_pk)['message'].keys():
                messages.warning(request, check_image_upload_errors(request, form_pk)['message']['error'])
                return redirect(f"/forms/{form_pk.id}")
            else:
                image_upload(request, pk, form_pk, my_dict)
                
            for check_key, check_value in my_dict.items():
                for value_none in check_value.copy():
                    if not check_value[value_none]:
                        check_value.pop(value_none)
                
            print("my_dict >>>>>", my_dict)  
            Form.objects.filter(id=pk).update(values=my_dict)
            messages.success(request, 'Form created')
            return redirect("/forms")
        return render(request, 'add_values.html', context)
    else:
        messages.warning(request, 'Form not found')
        return redirect('/forms')


def get_form(request, pk=None):
    form_pk = Form.objects.filter(id=pk).first()
    images_path = f'/static/media/{pk}/'

    for k, i in form_pk.values.items():
        print(k, i)
    if form_pk:
        values = form_pk.values
        if len(values) < 1:
            messages.warning(request, 'The form is empty, fill in your information')
            return redirect(f'/forms/{form_pk.id}')
        if request.method == 'POST':
            form_keys = ['checkbox_field_', 'selectbox_field_', 'question_field_']
            form = (request.POST or None)
            my_dict = {}
            for key, add_item in form.items():
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
                if len(add_item) < 1:
                    messages.warning(request, 'Inputs cannot be empty')
                    return redirect(f"/forms/{form_pk.id}/view")
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