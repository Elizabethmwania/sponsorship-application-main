# Generated by Django 3.2.7 on 2022-10-17 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('approvedApplications', '0002_auto_20221017_0446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approvedapplications',
            old_name='status',
            new_name='application_status',
        ),
    ]
