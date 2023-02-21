from django.shortcuts import redirect
from django.contrib import messages
from .image_check_and_upload import check_image_upload_errors, image_upload
from django.http import HttpResponse
from ..models import Form, FilledForms
import xlsxwriter, os


def check_values_for_add_form(request, pk, form_pk):
    form_keys = ['checkbox_field', 'question_field']
    ### Dict to add to the database
    my_dict = {}
    form = (request.POST or None)
    count = 0
    if len(form) < 2:
        messages.warning(request, 'Form is empty')
        return redirect(f"/forms/{form_pk.id}")
    
    for nums, (key, add_item) in enumerate(form.items(), 0):
        key_parts = key.split("_")
        #### Index 0 of the dict is set to 'title'. A title must be included. Returns an error if 'header' is missing or has been modified
        if nums == 1:
            if key_parts[-1] != 'title':
                messages.warning(request, 'Something went wrong')
                return redirect(f"/forms/{form_pk.id}")
        if key == 'csrfmiddlewaretoken':
            continue
        #### We compare this (field_name) to a list of 'form_keys' so that other keys in the frontend are not located in the database
        field_name = "_".join(key_parts[:3])
        field_check_name = "_".join(key_parts[:2])
        if key_parts[-1] == 'description':
            if len(add_item) == 0:
                continue
        if len(add_item) < 1:
            messages.warning(request, 'Inputs cannot be empty')
            return redirect(f"/forms/{form_pk.id}")
        if field_check_name not in form_keys:
            messages.warning(request, 'Something went wrong')
            return redirect(f"/forms/{form_pk.id}")
        if field_name not in my_dict:
            my_dict[field_name] = {'title':None,'description':None,'image':[],'uploaded_image':[],'youtube':[],
                                    'url':[],'button':[],'input':None,'values':[], 'required':None, 'allow':None, 'one_selection':None, 'counter':0}
        ######## check dictionary keys
        if field_check_name == 'question_field':
            if key_parts[-1] == 'button':
                my_dict[field_name]['button'].append(add_item)
                if key_parts[-1] == 'allow':
                    my_dict[field_name].update({'allow':True})
            my_dict[field_name].update({'input':True})
        if key_parts[-1] == 'title':
            my_dict[field_name].update({'title':add_item})
            count+=1
            my_dict[field_name].update({'counter':count})
            
        elif key_parts[-1] == 'description':
            my_dict[field_name].update({'description':add_item})
        elif key_parts[-1] == 'image':
            my_dict[field_name].get('image').append(add_item)
        elif key_parts[-1] == 'youtube':
            my_dict[field_name].get('youtube').append(add_item)
        elif key_parts[-1] == 'url':
            my_dict[field_name].get('url').append(add_item)
        elif key_parts[-1] == 'values':
            my_dict[field_name].get('values').append(add_item)
        elif key_parts[-1] == 'select':
            if add_item == "on":
                my_dict[field_name].update({'one_selection':True})
        elif key_parts[-1] == 'allow':
            if add_item == "on":
                my_dict[field_name].update({'allow':True})
        elif key_parts[-1] == 'required':
            if add_item == "on":
                my_dict[field_name].update({'required':True})
    ######## returns an error if the image does not meet the standards
    if 'error' in check_image_upload_errors(request, form_pk, my_dict)['message'].keys():
        messages.warning(request, check_image_upload_errors(request, form_pk, my_dict)['message']['error'])
        return redirect(f"/forms/{form_pk.id}")
    else:
        image_upload(request, pk, form_pk, my_dict)
    ####### check None keys. If none, deletes that key
    for check_key, check_value in my_dict.items():
        for value_none in check_value.copy():
            if not check_value[value_none]:
                check_value.pop(value_none)
    # for k,i in my_dict.items():
        # print(f"key>> {k} | value>> {i}")
    return my_dict


def fill_form(request, pk, form_pk):
    form = (request.POST or None)
    my_dict = {}
    for keys, val in form_pk.values.items():
        if keys not in my_dict:
            my_dict.update({keys:[]})
        ## check required keys and append to my_dict[keys]
        if 'required' in val.keys():
            my_dict[keys].append(True)
    for key, add_item in form.items():
        key_parts = key.split("_")
        if key == 'csrfmiddlewaretoken':
            continue
        if key == 'email':
            continue
        elif key == 'fullname':
            continue
        field_name = "_".join(key_parts[:3])
        if field_name not in my_dict:
            if field_name == 'email' or field_name == 'fullname':
                continue
            messages.warning(request, 'Something went wrong')
            return HttpResponse
        my_dict[field_name].append(add_item)
    for i in my_dict.values():
        if True in i:
            if len(i) < 2:
                messages.warning(request, 'Required inputs cannot be empty')
                return HttpResponse
    return my_dict


def form_id_to_xlsx(request, pk=None):
    get_form = Form.objects.filter(id=pk).first()
    ######## EXCEL ########
    root = 'http://127.0.0.1:8000'
    images_path = f'/static/media/{pk}/'
    xlsx_path = '/static/xlsx_files/form/'
    if " " in get_form.form_name:
        file_name = f'{get_form.form_name.replace(" ","_")}.xlsx'
    else:
        file_name = f'{get_form.form_name}.xlsx'
    workbook = xlsxwriter.Workbook("static/xlsx_files/form/"+file_name)
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
    download = root+xlsx_path+file_name
    return redirect(download)


def filled_form_to_xlsx(request, pk=None, wk=None):
    form = Form.objects.filter(id=pk).first()
    form_pk = FilledForms.objects.filter(id=wk).first()
    root = 'http://127.0.0.1:8000/'
    images_path = f'/static/media/{pk}/'
    xlsx_path = f'static/xlsx_files/filled_form/{pk}/'
    if not os.path.exists(xlsx_path):
        os.mkdir(xlsx_path)
    if " " in form_pk.fullname:
        file_name = f'{form_pk.fullname.replace(" ","_")}.xlsx'
    else:
        file_name = f'{form_pk.fullname}.xlsx'

    workbook = xlsxwriter.Workbook(xlsx_path+file_name)
    worksheet = workbook.add_worksheet()
    cell_format = workbook.add_format({'bold': True, 'bg_color': 'blue', 'color':'white'})
    full = workbook.add_format({'bold': True, 'bg_color': 'green', 'color':'white'})
    null = workbook.add_format({'bold': True, 'bg_color': 'red', 'color':'white'})
    worksheet.set_column(0, 1, 10)
    worksheet.set_column(1, 1, 30)
    worksheet.set_column(2, 1, 30)
    worksheet.set_column(3, 1, 30)
    worksheet.set_column(4, 1, 30)
    worksheet.set_column(5, 1, 30)

    worksheet.write('A1', 'Counter', cell_format)
    worksheet.write('B1', 'Answer', cell_format)
    worksheet.write('C1', 'Values', cell_format)
    worksheet.write('D1', 'Button', cell_format)
    worksheet.write('E1', 'Title/Question', cell_format)
    worksheet.write('F1', 'Description', cell_format)
    worksheet.write('G1', 'Image url', cell_format)
    worksheet.write('H1', 'Uploaded Image', cell_format)
    worksheet.write('I1', 'Youtube Url', cell_format)
    worksheet.write('J1', 'Url', cell_format)
    worksheet.write('K1', 'Required', cell_format)
    
    for nums, (form_key, form_value) in enumerate(form.values.items(), 2):
        for filled_form_key, filled_form_value in form_pk.filled_form.items():
            if form_key == filled_form_key:
                ########## A line ##########
                if 'counter' in form_value:
                    worksheet.write(f'A{nums}', form_value['counter'])
                ########## B line ##########
                if filled_form_value:
                    for answer in filled_form_value:
                        if answer == True:
                            continue
                        else:
                            worksheet.write(f'B{nums}', answer, full)
                else:
                    worksheet.write(f'B{nums}', 'No answer was given', null)
                ########## C line ##########
                if 'values' in form_value:
                    values_v = """"""
                    for values in form_value['values']:
                        values_v += values+'\n'
                    worksheet.write(f'C{nums}', values_v)
                else:
                    worksheet.write(f'C{nums}', 'No value given', null)
                ########## D line ##########
                if 'button' in form_value:
                    button_v = """"""
                    for button in form_value['button']:
                        button_v += button+'\n'
                    worksheet.write(f'D{nums}', button_v)
                else:
                    worksheet.write(f'D{nums}', 'No value given', null)
                ########## E line ##########
                if 'title' in form_value:
                    worksheet.write(f'E{nums}', form_value['title'])
                ########## F line ##########
                if 'description' in form_value:
                    worksheet.write(f'F{nums}', form_value['description'])
                ########## G line ##########
                if 'image' in form_value:
                    image_v = """"""
                    for image in form_value['image']:
                        image_v += image+'\n'
                    worksheet.write(f'G{nums}', image_v)
                ########## H line##########
                if 'uploaded_image' in form_value:
                    for image in form_value['uploaded_image']:
                        worksheet.write(f'H{nums}', root+images_path+image)
                ########## I line ##########
                if 'youtube' in form_value:
                    youtube_v = """"""
                    for youtube in form_value['youtube']:
                        youtube_v += youtube+'\n'
                    worksheet.write(f'I{nums}', youtube_v)
                ########## J line ##########
                if 'url' in form_value:
                    url_v = """"""
                    for url in form_value['url']:
                        url_v += url+'\n'
                    worksheet.write(f'J{nums}', url_v)
                ########## K line ##########
                if 'required' in form_value:
                    worksheet.write(f'K{nums}', 'True') 
    workbook.close()
    download = root+xlsx_path+file_name
    return redirect(download)