# Generated by Django 3.1.2 on 2020-11-09 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0002_auto_20201109_1225'),
        ('management', '0010_auto_20201109_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='pharmacy_prescription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='treatment_prescription', to='pharmacy.prescription'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Show'), (0, 'Hide')], null=True),
        ),
        migrations.AlterField(
            model_name='bed',
            name='status',
            field=models.CharField(blank=True, choices=[('Assigned', 'Assigned'), ('Unassigned', 'Unassigned')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'), ('Married', 'Married')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Canceled', 'Canceled')], max_length=100, null=True),
        ),
    ]
