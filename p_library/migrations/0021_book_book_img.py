# Generated by Django 2.2.6 on 2019-11-27 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0020_auto_20191121_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d'),
        ),
    ]