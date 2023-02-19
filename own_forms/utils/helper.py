from django.shortcuts import redirect
from django.contrib import messages
from .image_check_and_upload import check_image_upload_errors, image_upload
from django.core.serializers import serialize
import json

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
                                    'url':[],'button':[],'input':None,'values':[], 'required':None, 'allow':None, 'counter':0}
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
                my_dict[field_name]['values'].append(True)
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
    for k,i in my_dict.items():
        print(f"key>> {k} | value>> {i}")
    return my_dict



def fill_form(request, pk, form_pk):
    form_keys = ['checkbox_field', 'question_field']
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
        check_field = "_".join(key_parts[:2])
        if len(add_item) < 1:
            messages.warning(request, 'Inputs cannot be empty')
            return redirect(f"/forms/{form_pk.id}/view")
        if check_field not in form_keys:
            messages.warning(request, 'Something went wrong')
            return redirect(f"/forms/{form_pk.id}/view")
        if field_name not in my_dict:
            my_dict[field_name] = []
        my_dict[field_name].append(add_item)
    # for k,i in my_dict[0:1].items():
    #     print(i)
    return my_dict