# Generated by Django 3.2.4 on 2021-06-24 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imggal',
            name='image',
            field=models.ImageField(upload_to='dcopzmedia/static/img/'),
        ),
    ]
