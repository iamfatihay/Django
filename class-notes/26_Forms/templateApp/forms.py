from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    number = forms.IntegerField(blank=True, null=True)