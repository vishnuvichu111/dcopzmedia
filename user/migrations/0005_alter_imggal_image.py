# Generated by Django 3.2.4 on 2021-06-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_imggal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imggal',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
