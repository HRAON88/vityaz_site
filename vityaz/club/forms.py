from django import forms
from captcha.fields import CaptchaField

class TrialLessonForm(forms.Form):
    SPORTS_CHOICES = [
        ('sambo', 'Самбо'),
        ('arashi_karate', 'Араши Карате'),
        ('taekwondo', 'Тхэквондо'),
    ]
    full_name = forms.CharField(label='ФИО', max_length=100)
    age = forms.IntegerField(label='Возраст', min_value=1)
    sport = forms.ChoiceField(choices=SPORTS_CHOICES, label='Вид спорта')
    phone_number = forms.CharField(label='Номер телефона', max_length=15)


class CallbackRequestForm(forms.Form):
    full_name = forms.CharField(label='ФИО', max_length=100)
    phone_number = forms.CharField(label='Номер телефона', max_length=15)
