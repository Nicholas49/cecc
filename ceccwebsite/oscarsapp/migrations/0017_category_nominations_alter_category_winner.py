# Generated by Django 4.1.4 on 2025-02-09 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("oscarsapp", "0016_category_shortname_alter_category_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="nominations",
            field=models.ManyToManyField(
                related_name="nominations",
                through="oscarsapp.Nomination",
                to="oscarsapp.movie",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="winner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="winner",
                to="oscarsapp.movie",
            ),
        ),
    ]
