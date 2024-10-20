from django import forms
from captcha.fields import CaptchaField

class TrialLessonForm(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=100)
    age = forms.IntegerField(label='Возраст', min_value=1)
    direction = forms.CharField(label='Направление', max_length=100)
    phone_number = forms.CharField(label='Номер телефона', max_length=15)


class CallbackRequestForm(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=100)
    phone_number = forms.CharField(label='Номер телефона', max_length=15)
