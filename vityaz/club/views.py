import json
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from .forms import *
from .models import *
from django.urls import reverse_lazy
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Schedule
from .serializers import ScheduleSerializer
from django.http import HttpResponse
from django.shortcuts import render
from .forms import TrialLessonForm, CallbackRequestForm
import requests
from django.conf import settings



class ClubNews(DataMixin, ListView):

    model = News
    template_name = 'club/news.html'
    context_object_name = 'posts'
    # extra_context = {'title': "Главная страница"}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Новости")
        return dict(list(context.items()) + list(c_def.items()))
    def get_queryset(self):
        return News.objects.all().prefetch_related('photos')


def schedule(request):
    return HttpResponse('Котакты')


def contact(request):
    return HttpResponse('Котакты')
def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h2> Вика игнорщица</h2>')


class ShowPost(DataMixin, DetailView):
    model = News
    template_name = 'club/post.html'
    pk_url_kwarg = 'id'
    context_object_name = 'post'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context["post"])
        return dict(list(context.items()) + list(c_def.items()))




class ScheduleView(DataMixin, ListView):

    model = Group
    template_name = 'club/schedule.html'
    context_object_name = 'schedules'
    # extra_context = {'title': "Главная страница"}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Расписание")
        return dict(list(context.items()) + list(c_def.items()))
    def get_queryset(self):
        return self.model.objects.all()



class ScheduleAPIView(APIView):

    def get(self, request, age, format=None):

        schedules = Schedule.objects.filter(group__age_start__lte=age,
                                            group__age_end__gte=age)
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data)



class ClubMainMenu(DataMixin, ListView):
    template_name = 'club/mainmenu1.html'
    context_object_name = 'menu'
    model = Coach

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trial_form = TrialLessonForm()
        callback_form = CallbackRequestForm()

        context.update({
            'trial_form': trial_form,
            'callback_form': callback_form,
            'RECAPTCHA_SITE_KEY': settings.RECAPTCHA_SITE_KEY,
            'message': None
        })

        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        message = None
        message_success = None

        if 'trial_submit' in request.POST:
            trial_form = TrialLessonForm(request.POST)
            callback_form = CallbackRequestForm()
            if trial_form.is_valid():
                recaptcha_response = request.POST.get('g-recaptcha-response')
                data = {
                    'secret': settings.RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
                result = r.json()

                if result['success']:
                    TrialLesson.objects.create(
                        full_name=trial_form.cleaned_data['full_name'],
                        age=trial_form.cleaned_data['age'],
                        sport=trial_form.cleaned_data['sport'],
                        phone_number=trial_form.cleaned_data['phone_number']
                    )
                    message_success = "Вы успешно записались на пробное занятие!"
                    trial_form = TrialLessonForm()
                else:
                    message = "Пожалуйста, исправьте ошибки в форме."

        elif 'callback_submit' in request.POST:
            callback_form = CallbackRequestForm(request.POST)
            trial_form = TrialLessonForm()
            if callback_form.is_valid():
                recaptcha_response = request.POST.get('g-recaptcha-response')
                data = {
                    'secret': settings.RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
                result = r.json()

                if result['success']:
                    CallbackRequest.objects.create(
                        full_name=callback_form.cleaned_data['full_name'],
                        phone_number=callback_form.cleaned_data['phone_number']
                    )
                    message_success = "Запрос на обратный звонок успешно отправлен!"
                    callback_form = CallbackRequestForm()
                else:
                    message = "Пожалуйста, исправьте ошибки в форме."

        context = self.get_context_data()
        context.update({
            'trial_form': trial_form,
            'callback_form': callback_form,
            'message': message,
            'message_success': message_success
        })

        return render(request, self.template_name, context)
