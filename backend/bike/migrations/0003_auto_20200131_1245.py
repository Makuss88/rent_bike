# Generated by Django 2.2.7 on 2020-01-31 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_auto_20200114_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='color_bike',
            field=models.CharField(choices=[('BLACK', 'Black'), ('RED', 'Red'), ('WHITE', 'White')], max_length=5),
        ),
    ]
