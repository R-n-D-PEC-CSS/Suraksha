# Generated by Django 3.0.6 on 2020-05-22 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_contact_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user',
            new_name='curr_user',
        ),
    ]
