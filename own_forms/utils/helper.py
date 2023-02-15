from django.shortcuts import redirect
from django.contrib import messages
from .image_check_and_upload import check_image_upload_errors, image_upload

def check_values_for_add_form(request, pk, form_pk):
    form_keys = ['checkbox_field_', 'question_field_']
    ### Dict to add to the database
    my_dict = {}
    form = (request.POST or None)
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
        if len(add_item) < 1:
            messages.warning(request, 'Inputs cannot be empty')
            return redirect(f"/forms/{form_pk.id}")
        if field_name[0:-1] not in form_keys:
            messages.warning(request, 'Something went wrong')
            return redirect(f"/forms/{form_pk.id}")
        if field_name not in my_dict:
            my_dict[field_name] = {'title':'','description':'','image':[],'uploaded_image':[],'youtube':[],'url':[],'values':[], 'select':'', 'required':''}
        ######## check dictionary keys
        if key_parts[-1] == 'title':
            my_dict[field_name].update({'title':add_item})
        elif key_parts[-1] == 'description':
            print("var>>>",key_parts[-1])
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
                my_dict[field_name].update({'select':True})
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
    print("my_dict >>>>>", my_dict)
    return my_dict