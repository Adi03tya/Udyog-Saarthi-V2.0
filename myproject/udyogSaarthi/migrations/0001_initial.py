# Generated by Django 5.0.1 on 2024-01-28 16:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=100)),
                ('organization_type', models.CharField(choices=[('Private', 'Private'), ('Government', 'Government'), ('PSU', 'PSU')], max_length=10)),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.TextField(max_length=500)),
                ('openings', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PYQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='files')),
                ('Braille_pdf', models.FileField(null=True, upload_to='files')),
                ('Audio_English', models.FileField(null=True, upload_to='files')),
                ('Audio_Hindi', models.FileField(null=True, upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mothers_name', models.CharField(blank=True, max_length=255)),
                ('fathers_name', models.CharField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True)),
                ('pincode', models.IntegerField()),
                ('DOB', models.DateField()),
                ('stream', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('UDID', models.IntegerField()),
                ('functional_difficulties', models.TextField(max_length=200)),
                ('assistive_device', models.CharField(max_length=100)),
                ('human_assistance', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='employerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(blank=True, max_length=255)),
                ('organization_address', models.TextField(blank=True)),
                ('organization_type', models.CharField(choices=[('Private', 'Private'), ('Government', 'Government'), ('PSU', 'PSU')], max_length=10)),
                ('pincode', models.IntegerField()),
                ('DOB', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udyogSaarthi.jobs')),
            ],
        ),
        migrations.CreateModel(
            name='Posted_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='udyogSaarthi.jobs')),
            ],
        ),
    ]
