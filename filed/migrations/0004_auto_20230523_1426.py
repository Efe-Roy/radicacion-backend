# Generated by Django 3.2.15 on 2023-05-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filed', '0003_loggerall_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='correct_document_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='is_notified_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='is_personal_notified_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='observation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='payment_receipt_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='payment_status_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='process_act_num_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='resolution_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='resolution_notification_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='review_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='underReview_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
