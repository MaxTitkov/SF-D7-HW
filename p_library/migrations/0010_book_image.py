# Generated by Django 2.2.6 on 2019-11-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0009_auto_20191113_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='img_field'),
        ),
    ]