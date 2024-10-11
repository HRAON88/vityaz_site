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


class ClubHome(DataMixin, ListView):

    model = News
    template_name = 'club/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': "Главная страница"}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        cc = dict(list(context.items()) + list(c_def.items()))
        return cc
    def get_queryset(self):
        return News.objects.all().prefetch_related('photos')

def about(request):
    return HttpResponse('О сайте')

def schedules(request):
    return HttpResponse('Расписания')
def contact(request):
    return HttpResponse('Котакты')
def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h2> Вика игнорщица</h2>')


class ShowPost(DataMixin, DetailView):
    model = News
    template_name = 'club/post.html'
    pk_url_kwarg = 'id'
    context_object_name = 'posts'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context["post"])
        return dict(list(context.items()) + list(c_def.items()))

