# Generated by Django 2.2.6 on 2019-11-18 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0011_auto_20191118_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='book',
            field=models.ManyToManyField(blank=True, through='p_library.Rent', to='p_library.Book'),
        ),
    ]