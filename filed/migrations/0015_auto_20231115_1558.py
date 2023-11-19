# Generated by Django 3.2.15 on 2023-11-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filed', '0014_operatorobservation_createdat'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='file',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]