# Generated by Django 3.0.4 on 2020-04-30 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ATMStatus', '0013_auto_20200430_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atmlogincredentialsdetails',
            name='branch_name',
            field=models.ForeignKey(default='Please select branch name', on_delete=django.db.models.deletion.CASCADE, related_name='BranchDetails_branch_name', to='ATMStatus.BranchDetails'),
        ),
    ]
