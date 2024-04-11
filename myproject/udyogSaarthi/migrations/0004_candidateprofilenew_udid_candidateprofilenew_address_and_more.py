# Generated by Django 5.0.1 on 2024-04-03 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udyogSaarthi', '0003_rename_dob_candidateprofilenew_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateprofilenew',
            name='UDID',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofilenew',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='candidateprofilenew',
            name='assistive_device',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofilenew',
            name='functional_difficulties',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofilenew',
            name='highest_qualification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofilenew',
            name='human_assistance',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofilenew',
            name='pincode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='candidateprofilenew',
            name='skills',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
