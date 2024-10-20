from django.contrib import admin
from .models import Group, Schedule, Photo, News
from .models import TrialLesson, CallbackRequest

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 5  # количество пустых форм для добавления фотографий

class NewsAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(News, NewsAdmin)
admin.site.register(Photo)
admin.site.register(Group)
admin.site.register(Schedule)
admin.site.register(TrialLesson)
admin.site.register(CallbackRequest)

