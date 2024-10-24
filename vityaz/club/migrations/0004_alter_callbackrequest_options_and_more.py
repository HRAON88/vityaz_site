# Generated by Django 5.1.1 on 2024-10-20 12:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_callbackrequest_triallesson_alter_group_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='callbackrequest',
            options={'ordering': ['time_create', 'full_name'], 'verbose_name': 'Заявки на звонок для уточнения'},
        ),
        migrations.AlterModelOptions(
            name='triallesson',
            options={'ordering': ['time_create', 'direction'], 'verbose_name': 'Заявки на тренировку'},
        ),
        migrations.AddField(
            model_name='callbackrequest',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triallesson',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='callbackrequest',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='callbackrequest',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='fio',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='group',
            name='age_end',
            field=models.IntegerField(default=8, verbose_name='До скольки лет'),
        ),
        migrations.AlterField(
            model_name='group',
            name='age_start',
            field=models.IntegerField(default=6, verbose_name='Со скольки лет'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название группы'),
        ),
        migrations.AlterField(
            model_name='group',
            name='trainer',
            field=models.CharField(max_length=100, verbose_name='Тренер'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='day_of_week',
            field=models.IntegerField(verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.TimeField(verbose_name='Конец тренировки'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(verbose_name='Начало тренировки'),
        ),
        migrations.AlterField(
            model_name='triallesson',
            name='age',
            field=models.IntegerField(verbose_name='Возраст ребенка'),
        ),
        migrations.AlterField(
            model_name='triallesson',
            name='direction',
            field=models.CharField(max_length=100, verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='triallesson',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='triallesson',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Телефон'),
        ),
    ]
