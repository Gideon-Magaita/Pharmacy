# Generated by Django 5.0.6 on 2024-05-27 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_applicant_business_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.CharField(default='pending', max_length=200),
        ),
    ]
