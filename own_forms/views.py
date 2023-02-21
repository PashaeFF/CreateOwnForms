from django.shortcuts import render, redirect
from .forms import FirstForm
from django.contrib import messages
from .models import Form, FilledForms
from django.http import HttpResponse
from .utils.helper import check_values_for_add_form, fill_form
import shutil, xlsxwriter

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
                new_form = Form.objects.create(email=form['email'].value(), url=form['url'].value(),
                                                fullname=form['fullname'].value(), form_name=form['form_name'].value())
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
            form_id_to_xlsx(pk,form_pk)
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
            email = request.POST['email']
            if len(email) < 4 or "@" not in email:
                messages.warning(request, 'Wrong email')
                return redirect(f"/forms/{form_pk.id}/view")  
            fullname = request.POST['fullname']
            print("name", fullname, type(fullname), len(fullname))
            if len(fullname) < 1:
                messages.warning(request, 'Enter your name')
                return redirect(f"/forms/{form_pk.id}/view")
            my_dict = fill_form(request, pk, form_pk)
            if type(my_dict) == dict:
                try:
                    FilledForms.objects.create(email=email, fullname=fullname, filled_form=fill_form(request, pk, form_pk), form_id_id=form_pk.id)
                    Form.objects.filter(id=form_pk.id).update(forms_count=form_pk.forms_count+1)
                    messages.success(request, 'Form filled successfull')
                    return redirect('/forms')
                except:
                    messages.warning(request, 'Something went wrong')
                    return redirect(f"/forms/{form_pk.id}/view")  
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

def form_id_to_xlsx(pk,get_form):
    ######## EXCEL ########
    images_path = f'/static/media/{pk}/'
    if " " in get_form.form_name:
        file_name = f'{get_form.form_name.replace(" ","_")}.xlsx'
    else:
        file_name = f'{get_form.form_name}.xlsx'
    workbook = xlsxwriter.Workbook("xlsx_files/form/"+file_name)
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format({'bold': True, 'bg_color': 'blue', 'color':'white'})
    worksheet.set_column(1, 1, 30)
    worksheet.set_column(2, 2, 30)
    worksheet.set_column(3, 3, 30)
    worksheet.set_column(4, 4, 30)
    worksheet.set_column(5, 5, 30)
    worksheet.set_column(6, 6, 30)
    worksheet.set_column(7, 7, 20)
    worksheet.set_column(8, 8, 20)
    worksheet.write('A1', 'Counter', cell_format)
    worksheet.write('B1', 'Title/Question', cell_format)
    worksheet.write('C1', 'Description', cell_format)
    worksheet.write('D1', 'Image url', cell_format)
    worksheet.write('E1', 'Uploaded Image', cell_format)
    worksheet.write('F1', 'Youtube Url', cell_format)
    worksheet.write('G1', 'Url', cell_format)
    worksheet.write('H1', 'Button', cell_format)
    worksheet.write('I1', 'Values', cell_format)
    worksheet.write('J1', 'Required', cell_format)
    for num,v in enumerate(get_form.values.values(),2):
        for e,i in v.items():
            if e == 'counter':
                worksheet.write(f'A{num}', i)
            if e == 'title':
                worksheet.write(f'B{num}', i)
            if e == 'description':
                worksheet.write(f'C{num}', i)
            if e == 'image':
                image_v = """"""
                for image in i:
                    image_v += image+'\n'
                worksheet.write(f'D{num}', image_v)
            if e == 'uploaded_image':
                for image in i:
                    worksheet.write(f'E{num}', images_path+image)
            if e == 'youtube':
                youtube_v = """"""
                for youtube in i:
                    youtube_v += youtube+'\n'
                worksheet.write(f'F{num}', youtube_v)
            if e == 'url':
                url_v = """"""
                for url in i:
                    url_v += url+'\n'
                worksheet.write(f'G{num}', url_v)
            if e == 'button':
                button_v = """"""
                for button in i:
                    button_v += button+'\n'
                worksheet.write(f'H{num}', button_v)
            if e == 'values':
                values_v = """"""
                for values in i:
                    values_v += values+'\n'
                worksheet.write(f'I{num}', values_v)
            if e == 'required':
                worksheet.write(f'J{num}', 'True')  
    workbook.close()
    print("file_name", file_name)
    return file_name



def get_filled_form(request, pk=None, wk=None):
    images_path = f'/static/media/{pk}/'
    form_pk = Form.objects.filter(id=pk).first()
    if form_pk:
        filled = FilledForms.objects.filter(id=wk).first()
        if filled:
            context = {
            "title":form_pk.form_name,
            "id":form_pk.id,
            "url":form_pk.url,
            "author":form_pk.fullname,
            "data":form_pk.values,
            "filled":filled,
            "images_path":images_path
            }
            if len(filled.filled_form) < 1:
                messages.warning(request, 'Form is empty')
                return redirect(f'/forms/{form_pk.id}/list')
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