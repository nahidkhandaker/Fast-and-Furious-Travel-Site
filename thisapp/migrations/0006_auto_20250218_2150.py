# Generated by Django 3.2.3 on 2025-02-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thisapp', '0005_auto_20241231_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdetail',
            name='app_contact',
            field=models.CharField(blank=True, help_text='Please add country code with contact number but no spaces.', max_length=15, null=True, verbose_name='Contact Number for Website'),
        ),
        migrations.AlterField(
            model_name='appdetail',
            name='developed_by',
            field=models.CharField(blank=True, help_text='Do not change it. Changing it may cause your website to not function correctly.', max_length=20, null=True, verbose_name='Developed By'),
        ),
        migrations.AlterField(
            model_name='appdetail',
            name='whatsapp_booking',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='Yes', help_text='Select Yes to accept booking on WhatsApp. Also make sure Contact Number is added.', max_length=10, verbose_name='Book On Whatsapp?'),
        ),
    ]
