# Generated by Django 5.0 on 2024-02-16 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_rename_pass1_user_password1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
    ]