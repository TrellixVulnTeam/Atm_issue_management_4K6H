# Generated by Django 2.2.3 on 2019-08-06 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATMStatus', '0002_auto_20190801_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewatmstatus',
            name='s_n',
            field=models.IntegerField(null=True),
        ),
    ]
