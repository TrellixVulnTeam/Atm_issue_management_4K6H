# Generated by Django 3.0.4 on 2020-06-04 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATMStatus', '0017_auto_20200604_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmlogincredentialsdetails',
            name='VNC_password',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
