# Generated by Django 3.0.3 on 2020-03-15 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0004_auto_20200315_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='number_bike',
            field=models.IntegerField(unique=True),
        ),
    ]
