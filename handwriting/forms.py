from django import forms

class FormName(forms.Form):
    text=forms.CharField(widget=forms.Textarea)
