# Generated by Django 3.2.15 on 2023-09-11 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filed', '0006_auto_20230712_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
