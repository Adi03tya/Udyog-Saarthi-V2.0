# Generated by Django 5.0.1 on 2024-04-03 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('udyogSaarthi', '0002_candidateprofilenew'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidateprofilenew',
            old_name='DOB',
            new_name='date_of_birth',
        ),
    ]
