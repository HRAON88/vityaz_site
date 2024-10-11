from django.urls import reverse
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Содержание")
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post', kwargs={'id': self.id})
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['time_create', 'title']



class Photo(models.Model):
    name = models.ForeignKey('News', related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    def __str__(self):
        return f'Photo for {self.name.title}'

class Coach(models.Model):
    fio = models.CharField(max_length=100)
    bio = models.TextField(blank=True, verbose_name="О тренере")

class Group(models.Model):
    name = models.CharField(max_length=100)
    trainer = models.CharField(max_length=100)

class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()
