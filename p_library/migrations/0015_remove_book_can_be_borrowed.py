# Generated by Django 2.2.6 on 2019-11-20 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0014_auto_20191120_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='can_be_borrowed',
        ),
    ]
