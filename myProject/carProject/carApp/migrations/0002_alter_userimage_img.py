# Generated by Django 5.0 on 2023-12-29 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
