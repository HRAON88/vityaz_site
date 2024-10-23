from django.urls import reverse
from django.db import models
from django.utils import timezone
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Содержание")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post', kwargs={'id': self.id})
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create', 'title']



class Photo(models.Model):
    name = models.ForeignKey('News', related_name='photos', on_delete=models.CASCADE, verbose_name='Новость')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")

    def __str__(self):
        return f'Photo for {self.name.title}'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
        ordering = ['name']

class Coach(models.Model):
    fio = models.CharField(max_length=100, verbose_name="ФИО")
    bio = models.TextField(blank=True, verbose_name="О тренере")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото", default='null')
    ordering = models.IntegerField(verbose_name="Порядок", default=6)


    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'
        ordering = ['ordering', 'fio']

class Group(models.Model):
    SAMBO = 'Sambo'
    KARATE = 'Karate'
    TAEKWONDO = 'Taekwondo'

    SPORT_CHOICES = [
        (SAMBO, 'Самбо'),
        (KARATE, 'Карате'),
        (TAEKWONDO, 'Тхэквондо'),
    ]

    name = models.CharField(max_length=100, verbose_name="Название группы")
    trainer = models.CharField(max_length=100, verbose_name="Тренер")
    age_start = models.IntegerField(default=6, verbose_name="Со скольки лет")
    age_end = models.IntegerField(default=8, verbose_name="До скольки лет")
    kind_of_sport = models.CharField(
        max_length=100,
        verbose_name="Название спорта",
        choices=SPORT_CHOICES,
        default=SAMBO
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name']


class Schedule(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    day_of_week = models.IntegerField(verbose_name="День недели")
    start_time = models.TimeField(verbose_name="Начало тренировки")
    end_time = models.TimeField(verbose_name="Конец тренировки")

    def __str__(self):
        return f'Расписание для группы {self.group.name} в {self.start_time}. Тренер {self.group.trainer}'

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
        ordering = ['day_of_week', 'start_time']


class TrialLesson(models.Model):
    full_name = models.CharField(max_length=100,  verbose_name='ФИО')
    age = models.IntegerField(verbose_name='Возраст ребенка')
    sport = models.CharField(max_length=100,  verbose_name='Вид спорта', default='Самбо')
    phone_number = models.CharField(max_length=15,  verbose_name='Телефон')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.full_name} - {self.sport}"
    class Meta:
        verbose_name = 'Заявки на тренировку'
        verbose_name_plural = 'Заявки на тренировки'
        ordering = ['-time_create', 'sport']

class CallbackRequest(models.Model):
    full_name = models.CharField(max_length=100,  verbose_name='ФИО')
    phone_number = models.CharField(max_length=15,  verbose_name='Телефон')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Заявки на звонок для уточнения'
        verbose_name_plural = 'Заявки на звонок для уточнения'
        ordering = ['-time_create', 'full_name']
