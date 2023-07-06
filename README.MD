# Create Own Forms
- [Create your own forms](#create-own-forms)
- [Project Title](#project-title)
- [Description](#description)
    - [Azərbaycanca](#az)
    - [English](#en)

<hr>

- İnstallation/Quraşdırılma
- [Azərbaycanca quraşdırılma](#azərbaycanca-quraşdırılma)  |  [İnstallation English](#installation-in-english)
- [Author](#author)
- [Version](#version)
___



<hr>

# Project Title
___
* <b>Create your own forms</b>
___

# Description

## AZ
___
* <b>Skript Django ilə qurulub.</b>
* <b>Qeydiyyatsız şəxsi formunuzu yarada bilərsiniz.</b>
* <b>Dizayn həm mobile, həm də web'ə uyğundur.</b>

![alt text](/docs/forms.png)
![alt text](/docs/mobile.png) 
![alt text](/docs/web.png)

* <b>2 tip yaratmaq olur. Sual və Seçim qutusu olan sorğu.</b>

![alt text](/docs/selects.png)

![alt text](/docs/question.png)

![alt text](/docs/checkbox.png)

* <b>+ İmage - Hər sorğuya maksimum 1 şəkil əlavə etmək olar. Maksimum limit 8mb-dır. 400kb-a qədər şəkil 100% keyfiyyətlə yüklənir bazaya. 400kb-dan yuxarı şəkillər isə 'image_check_and_upload.py' faylından tənzimlənir 400kb-1mb arası şəkillər 40%, 1mb-3mb arası şəkillər 20%, 3-5mb arası şəkillər 11%, 5-8mb arası şəkillər isə 7% keyfiyyətlə yüklənir.</b>

* <b>İnsanlar qeydiyyatsız daxil olub email və adlarını daxil edərək yaratdığınız formu doldura bilər.</b>

* <b>+ Answer - seçim üçün radio buttonlar yaradır.</b>

* <b>Required - seçimini seçdikdə formu dolduran qarşı tərəf artıq məcbur olur həmin suala cavab verməyə.</b>

* <b>Allow to add another answer - Bu seçim, seçim qutusunda mövcuddur, bunu işarə etdikdə formu dolduran şəxs başqa input da əlavə edə bilir.</b>

* <b>One selection - Bu seçim, seçim qutusunda mövcuddur, bunu seçdikdə istifadəçi yalnız 1 variant seçə bilir.</b>

* <b>+ Value - Bu seçim, seçim qutusunda mövcuddur, bunu seçib istədiyiniz qədər cavab variantı əlavə edə bilərsiniz.</b>
* <b>+ Url - Bu seçim, seçim qutusunda mövcuddur, bunu seçdikdə sorğuya link əlavə edə bilərsiniz.</b>
* <b>+ İmage Url - Bu seçim, seçim qutusunda mövcuddur, bunu seçdikdə şəkil Linki əlavə edirsiniz, formu dolduran şəxsin qarşısına şəkil kimi əks olunur.</b>
* <b>+ Youtube Url - Bu seçim, seçim qutusunda mövcuddur, bunu seçdikdə Youtube Linki əlavə edirsiniz.</b>




* <b>Yaradılan formu fieldləri ilə birlikdə "Microsoft Excell"-ə ".xlsx" formatında çıxarış verə bilərsiniz.</b>
* <b>Həmçinin insanların doldurduqları formlara verdikləri cavablarla birlikdə baxa bilər və "Microsoft Excell"-ə ".xlsx" formatında çıxarış verə bilərsiniz.</b>
* <b>Form dinamik olduğundan, front qismi JavaScript ilə yığılıb. Python onu JsonField kimi qəbul edir(Dictionary). Backend qisminde bütün qorumalar əlavə olunub ki, təsadüfi field seçib göndərilməsin(Frontdan nəsə dəyişiklik etsə kimsə).</b>

* <b>Qeyd: Formda heçbir İdentifikasiya və İcazələr əlavə olunmayıb, istəyə uyğun olaraq dashboarda vəya adi istifadəçi qismində icazələr daxil edib integrasiya edə bilərsiniz.</b>

* <b>Yaradılmış formun doldurulması:</b>

![alt text](/docs/fill_form.png)

* <b>Doldurulmuş formaya baxmaq(istifadəçinin cavabları yaşıl rənglə qeyd olunub):</b>

![alt text](/docs/filled_form.png)

* <b>Doldurulmuş formadan excell faylına çıxarış:</b>

![alt text](/docs/xlsx.png)
____


## EN
___
* <b>The script is built with Django.</b>
* <b>You can create your own form without registration.</b>
* <b>The design is suitable for both mobile and web.</b>

![alt text](/docs/forms.png)
![alt text](/docs/mobile.png) 
![alt text](/docs/web.png)

* <b>2 types can be created. A survey with a Question and a Choice box.</b>

![alt text](/docs/selects.png)

![alt text](/docs/question.png)

![alt text](/docs/checkbox.png)

* <b>+ İmage - A maximum of 1 image can be added per request. The maximum limit is 8mb. Images up to 400kb are uploaded with 100% quality data. Images above 400 kb are handled from the 'image_check_and_upload.py' file. 400kb-1mb images are loaded at 40% quality, 1mb-3mb images at 20%, 3-5mb images at 11% and 5-8mb images at 7% quality..</b>

* <b>People can log in without registering and fill out the form you create by entering their email and name.</b>

* <b>+ Answer - creates radio buttons for selection.</b>

* <b>Required - when choosing the option, the other party who fills out the form is forced to answer that question.</b>

* <b>Allow to add another answer - This option is available in the checkbox, by ticking it the form filler can add another input.</b>

* <b>One selection - This option is available in the option box, when selected, the user can select only 1 option.</b>

* <b>+ Value - This option is available in the selection box, you can select it and add as many answer options as you want.</b>
* <b>+ Url - This option is available in the option box, when you select it you can add a link to the survey.</b>
* <b>+ İmage Url - This option is available in the option box, when you select it you add an image Link and it is displayed as an image in front of the person filling the form.</b>
* <b>+ Youtube Url - This option is available in the option box, when you select it you add a Youtube Link.</b>




* <b>You can export the generated form fields to Microsoft Excel in ".xlsx" format.</b>
* <b>You can also view forms that people have filled out with their answers and export them to Microsoft Excel in ".xlsx" format..</b>
* <b>Since the form is dynamic, the frontend is designed with JavaScript. Python treats it as a JsonField(Dictionary). Added all protections like backend to avoid random field selection and sending (if someone changes something from frontend)..</b>

* <b>Note: No credentials or permissions are added to the form, you can optionally add and combine permissions in the dashboard or as a regular user.</b>


* <b>Filling the created form:</b>

![alt text](/docs/fill_form.png)

* <b>View the completed form (user responses are highlighted in green):</b>

![alt text](/docs/filled_form.png)

*<b>Extract from completed form to excel file:</b>

![alt text](/docs/xlsx.png)
____

# Author

<b>Contributors names and contact info</b>

<b>ex. Pashayev Rafig - [PashaeFF - Github](https://github.com/PashaeFF) </b>

# Version

>* <b>v1.0</b>
>* <b>Initial Release</b>

___