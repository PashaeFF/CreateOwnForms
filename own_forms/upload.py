def image_upload(request, pk, form_pk):
    image_path = f'static/media/{pk}'
    if os.path.exists(f'static/media/{pk}'):
        pass
    else:
        os.mkdir(f'static/media/{pk}')
    for i in request.FILES.keys():
        fileitem = request.FILES[i]
        extension = fileitem.name.split('.')[-1]
        image_extensions = ['jpeg','jpg','png']
        if fileitem.size > 1024000:
            messages.warning(request, 'Image can be max 1024kb')
            return redirect(f"/forms/{form_pk.id}")
        elif extension not in image_extensions:
            messages.warning(request, 'Only "jpg", "jpeg", "png" images are allowed')
            return redirect(f"/forms/{form_pk.id}")
        elif fileitem.name:
            fn = os.path.basename(fileitem.name)
            print(fn)
            open(f'{image_path}/{uuid.uuid4()}.{extension}', 'wb').write(fileitem.file.read())