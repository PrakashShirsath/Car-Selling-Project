# Generated by Django 5.0 on 2024-01-04 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carApp', '0004_rename_img_userimage_imgtake'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userimage',
            old_name='imgTake',
            new_name='imgPick',
        ),
    ]
