# Generated by Django 5.0.6 on 2024-05-26 17:58

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('ward', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=200)),
                ('full_address', models.CharField(max_length=200)),
                ('applicant_age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200)),
                ('phone_number', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must start with '+255' followed by 9 digits.", regex='^\\+255\\d{9}$')])),
                ('business_duration', models.CharField(blank=True, max_length=200, null=True)),
                ('pharmacy_name', models.CharField(max_length=200)),
                ('full_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must start with '+255' followed by 9 digits.", regex='^\\+255\\d{9}$')])),
                ('registration_number', models.CharField(max_length=200)),
                ('registration_date', models.DateField()),
                ('certificate', models.FileField(blank=True, upload_to='images/')),
                ('application_date', models.DateField()),
                ('signature', models.BooleanField(default=False)),
                ('status', models.CharField(default='pending', max_length=200)),
                ('location', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='mainapp.region')),
            ],
        ),
    ]
