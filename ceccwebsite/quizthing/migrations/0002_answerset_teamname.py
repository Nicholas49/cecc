# Generated by Django 2.1.4 on 2020-08-24 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizthing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerset',
            name='teamname',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
