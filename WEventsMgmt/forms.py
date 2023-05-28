from django import forms

class AddUserForm(forms.Form):
    name = forms.CharField(label="Full Name")
    loginName = forms.CharField(label="Login Name")
    password = forms.CharField(label="Password")

class CreateEventForm(forms.Form):
    name = forms.CharField(label="Event Name")
    eventdate = forms.DateField(label="Event Date")
