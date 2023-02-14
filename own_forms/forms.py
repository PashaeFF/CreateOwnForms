from django import forms

class FirstForm(forms.Form):
    email = forms.CharField()
    url = forms.CharField()
    fullname = forms.CharField()
    form_name = forms.CharField()