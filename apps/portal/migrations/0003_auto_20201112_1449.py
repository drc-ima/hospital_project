# Generated by Django 3.1.2 on 2020-11-12 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0007_auto_20201112_1449'),
        ('portal', '0002_auto_20201103_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='prescription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bill_prescription', to='pharmacy.prescription'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_type',
            field=models.CharField(blank=True, choices=[('CB', 'Card Bills'), ('CnB', 'Consultation Bills'), ('WB', 'Ward Bills'), ('LB', 'Lab Bills'), ('PhB', 'Pharmacy Bills'), ('PB', 'Procedures Bills')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='defaultbill',
            name='bill_type',
            field=models.CharField(blank=True, choices=[('CB', 'Card Bills'), ('CnB', 'Consultation Bills'), ('WB', 'Ward Bills'), ('LB', 'Lab Bills'), ('PhB', 'Pharmacy Bills'), ('PB', 'Procedures Bills')], max_length=100, null=True),
        ),
    ]
