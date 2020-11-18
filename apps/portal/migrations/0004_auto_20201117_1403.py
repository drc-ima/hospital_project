# Generated by Django 3.1.2 on 2020-11-17 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20201112_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_type',
            field=models.CharField(blank=True, choices=[('CnB', 'Consultation Bills'), ('WB', 'Ward Bills'), ('PB', 'Procedures Bills'), ('PhB', 'Pharmacy Bills'), ('LB', 'Lab Bills'), ('CB', 'Card Bills')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Paid'), (0, 'Not Paid')], null=True),
        ),
        migrations.AlterField(
            model_name='defaultbill',
            name='bill_type',
            field=models.CharField(blank=True, choices=[('CnB', 'Consultation Bills'), ('WB', 'Ward Bills'), ('PB', 'Procedures Bills'), ('PhB', 'Pharmacy Bills'), ('LB', 'Lab Bills'), ('CB', 'Card Bills')], max_length=100, null=True),
        ),
    ]
