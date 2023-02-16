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
                        '<h5 class="card-title">Question</h5>'+
                        '<div class="mb-3">'+
                            '<label for="question_field_'+n+'_title" class="form-label">Title/Question*</label>'+
                            '<input type="text" class="form-control" name="question_field_'+n+'_title" placeholder="Title or question" required>'+
                        '</div>'+
                        '<div class="form-group">'+
                            '<label for="description">Description</label>'+
                            '<textarea class="form-control rounded-0" id="description" name="question_field_'+n+'_description" rows="3"></textarea>'+
                        '</div>'+
                        '<a class="btn btn-light" type="button" name="add_image_to_question" id="add_image_to_question_'+n+'" value="Image" onclick="AddImageToQuestionField('+n+');" data-toggle="tooltip" data-placement="top" title="Add Image"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Image</a>'+
                    '</div>'+
                    '<div class="one_line" style="display:flex;">'+
                        '<div class="required" style="right: -80%">'+
                            '<div class="checkbox-wrapper-15">'+
                                '<input class="inp-cbx" id="question_field_'+n+'_required" type="checkbox" name="question_field_'+n+'_required" style="display: none;"/>'+
                                '<label class="cbx" for="question_field_'+n+'_required">'+
                                    '<span>'+
                                        '<svg width="12px" height="9px" viewbox="0 0 12 9">'+
                                            '<polyline points="1 5 4 8 11 1"></polyline>'+
                                        '</svg>'+
                                    '</span>'+
                                    '<span>Required</span>'+
                                '</label>'+
                            '</div>'+
                        '</div>'+
                    '</div>'+
                    '<br/>'+
                '</div>'+
                '<br/>');
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
                            '<label for="checkbox_field_'+n+'_title" class="form-label">*Title/Question</label>'+
                            '<input type="text" class="form-control" name="checkbox_field_'+n+'_title" placeholder="Title or question" required>'+
                        '</div>'+
                        '<div class="form-group">'+
                            '<label for="description">Description</label>'+
                            '<textarea class="form-control rounded-0" id="description" name="checkbox_field_'+n+'_'+v+'_description" rows="3"></textarea>'+
                        '</div>'+
                        '<div class="mb-3" id="value">'+
                            '<label for="value" class="form-label">*Value</label>'+
                            '<input type="text" class="form-control" name="checkbox_field_'+n+'_'+v+'_values" id="checkbox_field_'+n+'_'+v+'_values" placeholder="Value" required>'+
                        '</div>'+
                        '<div class="checkbox-wrapper-15">'+
                            '<input class="inp-cbx" id="checkbox_field_'+n+'_allow" type="checkbox" name="checkbox_field_'+n+'_allow" style="display: none;"/>'+
                            '<label class="cbx" for="checkbox_field_'+n+'_allow">'+
                                '<span>'+
                                    '<svg width="12px" height="9px" viewbox="0 0 12 9">'+
                                        '<polyline points="1 5 4 8 11 1"></polyline>'+
                                    '</svg>'+
                                '</span>'+
                                '<span>Allow to add another answer</span>'+
                            '</label>'+
                        '</div>'+
                        '<div class="add_'+n+'" id="add_'+n+'">'+
                            '<a class="btn btn-light" type="button" name="add_value_to_checkbox" id="add_value_to_checkbox" value="Value" onclick="AddValueToCheckboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Value"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Value</a>'+
                            '<a class="btn btn-light" type="button" name="add_url_to_checkbox" id="add_url_to_checkbox" value="Add Url" onclick="AddUrlToCheckboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Url"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Url</a>'+
                            '<a class="btn btn-light" type="button" name="add_image_url_to_checkbox" id="add_image_url_to_checkbox" value="Image Url" onclick="AddImageUrlToCheckboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Image Url"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Image Url</a>'+
                            '<a class="btn btn-light" type="button" name="add_youtube_url_to_checkbox" id="add_youtube_url_to_checkbox" value="Youtube Url" onclick="AddYoutubeUrlToCheckboxField('+n+')" data-toggle="tooltip" data-placement="top" title="Add Youtube Url"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Youtube Url</a>'+
                            '<a class="btn btn-light" type="button" name="add_image_to_checkbox" id="add_image_to_checkbox_'+n+'" value="Image" onclick="AddImageToCheckboxField('+n+');" data-toggle="tooltip" data-placement="top" title="Add Image"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Image</a>'+
                        '</div>'+
                    '</div>'+
                    '<div class="one_line" style="display:flex;">'+
                        '<div class="required" style="right: -80%">'+
                            '<div class="checkbox-wrapper-15">'+
                                '<input class="inp-cbx" id="checkbox_field_'+n+'_required" type="checkbox" name="checkbox_field_'+n+'_required" style="display: none;"/>'+
                                '<label class="cbx" for="checkbox_field_'+n+'_required">'+
                                    '<span>'+
                                        '<svg width="12px" height="9px" viewbox="0 0 12 9">'+
                                            '<polyline points="1 5 4 8 11 1"></polyline>'+
                                        '</svg>'+
                                    '</span>'+
                                    '<span>Required</span>'+
                                '</label>'+
                            '</div>'+
                        '</div>'+
                        '<div class="required" style="right: -40%">'+
                            '<div class="checkbox-wrapper-15">'+
                                '<input class="inp-cbx" id="checkbox_field_'+n+'_select" type="checkbox" name="checkbox_field_'+n+'_select" style="display: none;"/>'+
                                '<label class="cbx" for="checkbox_field_'+n+'_select">'+
                                    '<span>'+
                                        '<svg width="12px" height="9px" viewbox="0 0 12 9">'+
                                            '<polyline points="1 5 4 8 11 1"></polyline>'+
                                        '</svg>'+
                                    '</span>'+
                                    '<span>One Selection</span>'+
                                '</label>'+
                            '</div>'+
                        '</div>'+
                    '</div>'+
                    '<br/>'+
                '</div>'+
                '<br/>');
                n++;
                x++;
                }
            }) 
        })

    var v = 1
    // ########### For Question ############
    function AddImageToQuestionField(id){
        document.getElementById("add_image_to_question_"+id).remove()
        $("#body_"+id).append(
            '<div class="mb-3" id="value_'+v+'" style="display:flex;">'+
                '<input class="form-control" type="file" name="question_field_'+id+'_'+v+'_uploaded_image" id="question_field_'+id+'_'+v+'_uploaded_image" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveValue('+v+');ImageAddingButtonToQuestion('+id+');" value="Remove"><i class="fa fa-remove"></i></a>'+
            '</div>'
            );
        console.log("Image added")
        v++;
    }
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
        document.getElementById("add_image_to_checkbox_"+id).remove()
        console.log("Image Deleted>>>"+id)
        $("#body_"+id).append(
            '<div class="mb-3" id="image_'+v+'">'+
                '<div style="display:flex;">'+
                    '<input class="form-control" type="file" name="checkbox_field_'+id+'_'+v+'_uploaded_image" id="checkbox_field_'+id+'_'+v+'_uploaded_image" placeholder="Image Url" required><a class="btn btn-light" style="font-size:24px;color:brown;" onclick="RemoveImage('+v+');ImageAddingButtonToCheckBox('+id+');" value="Remove"><i class="fa fa-remove"></i></a>'+
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

    // ############ Remove elements #############
    function RemoveValue(id){
        document.getElementById("value_"+id).remove()
        console.log("Value Deleted>>>"+id)
    } 
    function RemoveImage(id){
        document.getElementById("image_"+id).remove()
        console.log("Image Deleted>>>"+id)
    } 
    // ############ Buttons ######################
    function ImageAddingButtonToCheckBox(id){
        $("#add_"+id).append(
            '<a class="btn btn-light" type="button" name="add_image_to_checkbox" id="add_image_to_checkbox_'+id+'" value="Image" onclick="AddImageToCheckboxField('+id+');" data-toggle="tooltip" data-placement="top" title="Add Image"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Image</a>'
            );
        console.log("Button added")
        }
    function ImageAddingButtonToQuestion(id){
        $("#body_"+id).append(
            '<a class="btn btn-light" type="button" name="add_image_to_question" id="add_image_to_question_'+id+'" value="Image" onclick="AddImageToQuestionField('+id+');" data-toggle="tooltip" data-placement="top" title="Add Image"><i class="fa fa-plus" style="color:green;" aria-hidden="true"></i> Image</a>'
        );
        console.log("Button added")
    }
    // ########################################

    function RemoveCard(id) {
        document.getElementById("card_"+id).remove()
        console.log("Deleted")
    }
    