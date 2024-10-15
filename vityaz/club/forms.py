from django import forms
from .models import Group




class AgeForm(forms.Form):
    age = forms.IntegerField(label='Введите ваш возраст')