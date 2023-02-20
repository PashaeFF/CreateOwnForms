from django.shortcuts import redirect
from django.contrib import messages
from .image_check_and_upload import check_image_upload_errors, image_upload
from django.http import HttpResponse

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