# Generated by Django 5.1.1 on 2024-10-20 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_alter_callbackrequest_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['name'], 'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
    ]
