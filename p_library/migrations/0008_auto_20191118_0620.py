# Generated by Django 2.2.6 on 2019-11-18 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_rent_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='borrower',
            field=models.ManyToManyField(blank=True, null=True, related_name='bfriend', through='p_library.Rent', to='p_library.Friend'),
        ),
    ]