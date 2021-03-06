# Generated by Django 3.1.2 on 2020-11-07 21:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0008_auto_20201030_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Widowed', 'Widowed'), ('Divorced', 'Divorced'), ('Single', 'Single'), ('Married', 'Married')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(blank=True, choices=[('ER', 'Emergency'), ('OPD', 'OPD'), ('Discharged', 'Discharged'), ('Ward', 'Ward')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='status',
            field=models.CharField(blank=True, choices=[('Canceled', 'Canceled'), ('Pending', 'Pending'), ('Completed', 'Completed')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='announce/')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=100000, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Hide'), (1, 'Show')], null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='announcements', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'announcement',
                'get_latest_by': 'created_at',
            },
        ),
    ]
