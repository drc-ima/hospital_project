# Generated by Django 3.1.2 on 2020-11-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_auto_20201110_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='accumulated_boxes_bought',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='accumulated_total_cost',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='cost_price_per_box',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='medicine_type',
            field=models.CharField(blank=True, choices=[('Tablet', 'Tablet'), ('Capsule', 'Capsule'), ('Syrup', 'Syrup')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Not Paid'), (1, 'Paid')], null=True),
        ),
    ]
