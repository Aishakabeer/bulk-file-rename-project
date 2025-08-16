from django import forms

class RenameForm(forms.Form):
    regex = forms.CharField(label='Match Regex', max_length=255)
    prefix = forms.CharField(label='New Prefix', max_length=255)
