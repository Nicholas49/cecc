# Generated by Django 2.1.4 on 2020-08-24 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizthing', '0002_answerset_teamname'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerset',
            name='answer8',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
