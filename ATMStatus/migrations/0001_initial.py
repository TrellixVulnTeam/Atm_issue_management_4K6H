# Generated by Django 2.2.3 on 2020-03-19 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtmDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_n', models.IntegerField()),
                ('branch_name', models.CharField(max_length=100)),
                ('branch_code', models.IntegerField()),
                ('atm_location', models.CharField(choices=[('OffSite', 'OffSite'), ('OnSite', 'OnSite')], default='OnSite', max_length=7)),
                ('atm_address', models.CharField(max_length=100, null=True)),
                ('atm_ip_address', models.CharField(max_length=12)),
                ('switch_ip_address', models.CharField(max_length=12)),
                ('switch_port_number', models.IntegerField(default=24023)),
                ('atm_installed_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='AtmTerminalIdDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_n', models.IntegerField()),
                ('atm_terminal_id', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='AtmIssueDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_n', models.IntegerField(null=True)),
                ('problem', models.CharField(max_length=2083, null=True)),
                ('remarks', models.CharField(max_length=2083, null=True)),
                ('atm_issue_priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=6)),
                ('atm_terminal_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ATMStatus.AtmTerminalIdDetails')),
                ('branch_code', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ATMStatus.AtmDetails')),
                ('branch_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AtmDetails_branch_name', to='ATMStatus.AtmDetails')),
            ],
        ),
        migrations.AddField(
            model_name='atmdetails',
            name='atm_terminal_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ATMStatus.AtmTerminalIdDetails'),
        ),
    ]
