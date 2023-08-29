from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    number = forms.IntegerField()