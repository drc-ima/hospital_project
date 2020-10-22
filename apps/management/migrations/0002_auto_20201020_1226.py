# Generated by Django 3.1.2 on 2020-10-20 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bed',
            name='status',
            field=models.CharField(blank=True, choices=[('Unassigned', 'Unassigned'), ('Assigned', 'Assigned')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='discharged_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Divorced', 'Divorced'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Single', 'Single')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('ER', 'Emergency'), ('OPD', 'OPD'), ('Ward', 'Ward')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='BedAllocate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admitted_at', models.DateField(blank=True, null=True)),
                ('discharged_at', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('bed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_allocate_bed', to='management.bed')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_allocates', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_allocate_patient', to='management.patient')),
            ],
            options={
                'db_table': 'bed_allocate',
            },
        ),
        migrations.AddField(
            model_name='bed',
            name='allocate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bed_allocate', to='management.bedallocate'),
        ),
        migrations.AddField(
            model_name='bed',
            name='bed_allocates',
            field=models.ManyToManyField(blank=True, related_name='bed_bed_allocates', to='management.BedAllocate'),
        ),
    ]