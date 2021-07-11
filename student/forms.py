from django import forms

class Studform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=6)
