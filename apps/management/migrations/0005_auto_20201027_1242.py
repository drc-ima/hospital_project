# Generated by Django 3.1.2 on 2020-10-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20201022_1316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicaldiagnosis',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AlterModelOptions(
            name='treatment',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RemoveField(
            model_name='patient',
            name='admitted_at',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='discharged_at',
        ),
        migrations.AddField(
            model_name='patient',
            name='date_admitted',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='date_discharged',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='time_admitted',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='time_discharged',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Widowed', 'Widowed'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Single', 'Single')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('Ward', 'Ward'), ('ER', 'Emergency'), ('OPD', 'OPD')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], max_length=100, null=True),
        ),
    ]
