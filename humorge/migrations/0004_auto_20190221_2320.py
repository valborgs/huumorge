# Generated by Django 2.1.5 on 2019-02-21 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('humorge', '0003_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
