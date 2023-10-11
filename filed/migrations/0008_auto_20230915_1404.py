# Generated by Django 3.2.15 on 2023-09-15 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filed', '0007_alter_file_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='operator_observation',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='resolution_date2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='resolution_number2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]