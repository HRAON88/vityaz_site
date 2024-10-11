from django.urls import path, re_path
from django.urls import include, path
#from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from vityaz import settings
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', ClubHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('schedules/', schedules, name='schedules'),
    path('post/<int:id>/', ShowPost.as_view(), name='post'),


]

'''path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),'''

