# Generated by Django 5.1.1 on 2024-10-23 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0011_alter_coach_options_coach_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='photo',
            field=models.ImageField(default='null', upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
    ]
