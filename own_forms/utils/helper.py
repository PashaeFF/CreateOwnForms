import os, uuid

def check_image_upload_errors(request, form_pk):
    for i in request.FILES.keys():
        fileitem = request.FILES[i]
        extension = fileitem.name.split('.')[-1]
        image_extensions = ['jpeg','jpg','png']
        if fileitem.size > 512000:
            message = 'Image can be max 500kb'
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
    for file_key, file_item in request.FILES.items():
        fileitem = request.FILES[file_key]
        files_key_parts = file_key.split("_")
        files_field_name = "_".join(files_key_parts[:3])
        last_field_name = "_".join(files_key_parts[-2:])
        extension = fileitem.name.split('.')[-1]
        if fileitem.name:
            image_name = f'{uuid.uuid4()}.{extension}'
            open(f'{image_path}/{image_name}', 'wb').write(fileitem.file.read())
            if 'uploaded_image' not in my_dict[files_field_name].keys():
                my_dict[files_field_name] = {'uploaded_image':[]}
            else:
                if last_field_name == 'uploaded_image':
                    my_dict[files_field_name].get('uploaded_image').append(image_name)

        
# def image_upload(request, pk, form_pk, my_dict):
#     image_path = f'static/media/{pk}'
#     if os.path.exists(f'static/media/{pk}'):
#         pass
#     else:
#         os.mkdir(f'static/media/{pk}')
#     for i in request.FILES.keys():
#         fileitem = request.FILES[i]
#         extension = fileitem.name.split('.')[-1]
#         if fileitem.name:
#             image_name = f'{uuid.uuid4()}.{extension}'
#             open(f'{image_path}/{image_name}', 'wb').write(fileitem.file.read())
#     for file_key, file_item in request.FILES.items():
#         files_key_parts = file_key.split("_")
#         files_field_name = "_".join(files_key_parts[:3])
#         last_field_name = "_".join(files_key_parts[-2:])
#         if 'uploaded_image' not in my_dict[files_field_name].keys():
#             my_dict[files_field_name] = {'uploaded_image':[]}
#         else:
#             if last_field_name == 'uploaded_image':
#                 my_dict[files_field_name].get('uploaded_image').append(image_name)