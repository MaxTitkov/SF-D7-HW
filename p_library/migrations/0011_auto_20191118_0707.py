# Generated by Django 2.2.6 on 2019-11-18 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0010_auto_20191118_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='book',
            field=models.ManyToManyField(blank=True, null=True, through='p_library.Rent', to='p_library.Book'),
        ),
    ]
