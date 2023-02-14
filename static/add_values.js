$(function () {
    $('[data-toggle="tooltip"]').tooltip()
    })
$(document).ready(function() {
    var max = 50;
    var x = 1;
    var n = 1 
    $("#add_question").click(function(){
        if(x <= max){
            $("#cards").append(
                '<div class="card" id="card_'+n+'" style="background: #fbf7f7;">'+
                    '<div class="card-body" id="body_'+n+'">'+
                        '<a class="btn btn-light" style="font-size:24px;float:right;" id="remove" name="remove" onclick="RemoveCard('+n+')" value="Remove" data-toggle="tooltip" data-placement="top" title="Remove"><i class="fa fa-remove"></i></a>'+
                        '<h5 class="card-title">Checbox</h5>'+
                        '<div class="mb-3">'+
                            '<label for="question_field_'+n+'_title" class="form-label">Title/Question</label>'+
                            '<input type="text" class="form-control" name="question_field_'+n+'_title" placeholder="Title or question" required>'+
                        '</div>'+
                        '</div>'+
                    '</div>'+
                    '<br/>'+
                '</div>');
                n++;
                x++;
                }
            }) 
    $("#add_checkbox").click(function(){
        if(x <= max){
            $("#cards").append(
                '<div class="card" id="card_'+n+'" style="background: #fbf7f7;">'+
                    '<div class="card-body" id="body_'+n+'">'+
                        '<a class="btn btn-light" style="font-size:24px;float:right;" id="remove" name="remove" onclick="RemoveCard('+n+')" value="Remove" data-toggle="tooltip" data-placement="top" title="Remove"><i class="fa fa-remove"></i></a>'+
                        '<h5 class="card-title">Checbox</h5>'+
                        '<div class="mb-3">'+
                            '<label for="checkbox_field_'+n+'_title" class="form-label">Title/Question</label>'+
                            '<input type="text" class="form-control" name="checkbox_field_'+n+'_title" placeholder="Title or question" required>'+
                        '</div>'+
                        '<a class="btn btn-light" type="button" name="add_value_to_checkbox" id="add_value_to_checkbox" value="Value" onclick="AddValueToCheckboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Value"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Value</a>'+
                        '<a class="btn btn-light" type="button" name="add_url_to_checkbox" id="add_url_to_checkbox" value="Add Url" onclick="AddUrlToCheckboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Url"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Url</a>'+
                        '<a class="btn btn-light" type="button" name="add_image_url_to_checkbox" id="add_image_url_to_checkbox" value="Image Url" onclick="AddImageUrlToCheckboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Image Url"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Image Url</a>'+
                        '<a class="btn btn-light" type="button" name="add_youtube_url_to_checkbox" id="add_youtube_url_to_checkbox" value="Youtube Url" onclick="AddYoutubeUrlToCheckboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Youtube Url"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Youtube Url</a>'+
                        '<a class="btn btn-light" type="button" name="add_image_to_checkbox" id="add_image_to_checkbox" value="Image" onclick="AddImageToCheckboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Image"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Image</a>'+
                        '</div>'+
                    '</div>'+
                    '<br/>'+
                '</div>');
                n++;
                x++;
                }
            }) 
        $("#add_selectbox").click(function(){
        if(x <= max){
            $("#cards").append(
                '<div class="card" id="card_'+n+'" style="background: #fbf7f7;">'+
                    '<div class="card-body" id="body_'+n+'">'+
                        '<a class="btn btn-light" style="font-size:24px;float: right;" id="remove" name="remove" onclick="RemoveCard('+n+')" value="Remove" data-toggle="tooltip" data-placement="top" title="Remove"><i class="fa fa-remove"></i></a>'+
                        '<h5 class="card-title">Selectbox</h5>'+
                        '<div class="mb-3">'+
                            '<label for="selectbox_field_'+n+'_title" class="form-label">Title/Question</label>'+
                            '<input type="text" class="form-control" name="selectbox_field_'+n+'_title" placeholder="Title or question" required>'+
                        '</div>'+
                        '<a class="btn btn-light" type="button" name="add_value_to_selectbox" id="add_value_to_selectbox" value="Value" onclick="AddValueToSelectboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Value"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Value</a>'+
                        '<a class="btn btn-light" type="button" name="add_url_to_selectbox" id="add_url_to_selectbox" value="Add Url" onclick="AddUrlToSelectboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Url"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Url</a>'+
                        '<a class="btn btn-light" type="button" name="add_image_url_to_selectbox" id="add_image_url_to_selectbox" value="Image Url" onclick="AddImageUrlToSelectboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Image Url"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Image Url</a>'+
                        '<a class="btn btn-light" type="button" name="add_youtube_url_to_selectbox" id="add_youtube_url_to_selectbox" value="Youtube Url" onclick="AddYoutubeUrlToSelectboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Youtube Url"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Youtube Url</a>'+
                        '<a class="btn btn-light" type="button" name="add_image_to_selectbox" id="add_image_to_selectbox" value="Image" onclick="AddImageToSelectboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Image"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Image</a>'+
                        '</div>'+
                    '</div>'+
                    '<br/>'+
                '</div>');
                n++;
                x++;
                }
            }) 
        })

    var v = 1
    // ########### For CheckBox ##################
    function AddValueToCheckboxField(id){
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'" style="display:flex;">'+
                '<input type="text" class="form-control" name="checkbox_field_'+id+'_'+v+'_values" id="checkbox_field_'+id+'_'+v+'_values" placeholder="Value" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+')" value="Remove"><i class="fa fa-remove"></i></a>'+
            '</div>'
            );
        console.log("Value added")
        v++;
    }
    function AddUrlToCheckboxField(id){
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'" style="display:flex;">'+
                '<input type="url" class="form-control" name="checkbox_field_'+id+'_'+v+'_url" id="checkbox_field_'+id+'_'+v+'_url" placeholder="Url" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+')" value="Remove"><i class="fa fa-remove"></i></a>'+
            '</div>'
            );
        console.log("Url added")
        v++;
    }
    function AddImageUrlToCheckboxField(id){
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'" style="display:flex;">'+
                '<input type="url" class="form-control" name="checkbox_field_'+id+'_'+v+'_image" id="checkbox_field_'+id+'_'+v+'_image" placeholder="Image Url" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+')" value="Remove"><i class="fa fa-remove"></i></a>'+
            '</div>'
            );
        console.log("Image url added")
        v++;
    }
    function AddImageToCheckboxField(id){
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'">'+
                '<div style="display:flex;">'+
                    '<input class="form-control" type="file" name="checkbox_field_'+id+'_'+v+'_uploaded_image" id="checkbox_field_'+id+'_'+v+'_uploaded_image" placeholder="Image Url" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+')" value="Remove"><i class="fa fa-remove"></i></a>'+
                '</div>'+
                '<small style="color: brown; id="imageHelp" >Max 8 MB and  JPG, JPEG, PNG files</small>'+
            '</div>'
            );
        console.log("Image upload added")
        v++;
    }
    function AddYoutubeUrlToCheckboxField(id){
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'" style="display:flex;">'+
                '<input type="url" class="form-control" name="checkbox_field_'+id+'_'+v+'_youtube" id="checkbox_field_'+id+'_'+v+'_youtube" placeholder="Youtube Url" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+')" value="Remove"><i class="fa fa-remove"></i></a>'+
            '</div>'
            );
        console.log("Youtube url added")
        v++;
    }

    // ########### For SelectBox #################
    function AddValueToSelectboxField(id){
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'" style="display:flex;">'+
                '<input type="text" class="form-control" name="selectbox_field_'+id+'_'+v+'_values" id="selectbox_field_'+id+'_'+v+'_values" placeholder="Value" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+')" value="Remove"><i class="fa fa-remove"></i></a>'+
            '</div>'
            );
        console.log("Value added")
        v++;
    }
    function AddUrlToSelectboxField(id){
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'" style="display:flex;">'+
                '<input type="url" class="form-control" name="selectbox_field_'+id+'_'+v+'_url" id="selectbox_field_'+id+'_'+v+'_url" placeholder="Url" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+')" value="Remove"><i class="fa fa-remove"></i></a>'+
            '</div>'
            );
        console.log("Value added")
        v++;
    }
    function AddImageUrlToSelectboxField(id){
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'" style="display:flex;">'+
                '<input type="url" class="form-control" name="selectbox_field_'+id+'_'+v+'_image" id="selectbox_field_'+id+'_'+v+'_image" placeholder="Image Url" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+')" value="Remove"><i class="fa fa-remove"></i></a>'+
            '</div>'
            );
        console.log("Value added")
        v++;
    }
    function AddImageToSelectboxField(id){
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'">'+
                '<div style="display:flex;">'+
                    '<input class="form-control" type="file" name="selectbox_field_'+id+'_'+v+'_uploaded_image" id="selectbox_field_'+id+'_'+v+'_uploaded_image" placeholder="Image Url" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+')" value="Remove"><i class="fa fa-remove"></i></a>'+
                '</div>'+
                '<small style="color: brown; id="imageHelp" >Max 8 MB and  JPG, JPEG, PNG files</small>'+
            '</div>'
            );
        console.log("Image upload added")
        v++;
    }
    function AddYoutubeUrlToSelectboxField(id){
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'" style="display:flex;">'+
                '<input type="url" class="form-control" name="selectbox_field_'+id+'_'+v+'_youtube" id="selectbox_field_'+id+'_'+v+'_youtube" placeholder="Youtube Url" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+')" value="Remove"><i class="fa fa-remove"></i></a>'+
            '</div>'
            );
        console.log("Value added")
        v++;
    }
    
    // ############ Remove elements #############
    function RemoveValue(id){
        document.getElementById("value_"+id).remove()
        console.log("Value Deleted>>>"+id)
    } 
    function RemoveCard(id) {
        document.getElementById("card_"+id).remove()
        console.log("Deleted")
    }