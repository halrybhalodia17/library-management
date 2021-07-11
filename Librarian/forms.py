from django import forms

class Libform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=6)

class Studinfo(forms.Form):
    enroll_no = forms.IntegerField()
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    branch = forms.CharField(max_length=100)
    phone_no = forms.IntegerField()
    password = forms.CharField(min_length=20)
    roll_no = forms.IntegerField()
    shift = forms.CharField(max_length=20)

class AddBook(forms.Form):
    name = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
    total= forms.IntegerField()

class Issue(forms.Form):
    semail = forms.EmailField()
    bname = forms.IntegerField()

class Removeform(forms.Form):
    bid = forms.IntegerField()


class Searchform(forms.Form):
    bid = forms.IntegerField()

class Returnform(forms.Form):
    semail = forms.EmailField()

class Returnform1(forms.Form):
    bname = forms.IntegerField()
    