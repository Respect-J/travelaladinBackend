# Generated by Django 5.0.1 on 2024-02-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_alter_tours_mainimg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tours',
            name='price_for_one',
        ),
        migrations.RemoveField(
            model_name='tours',
            name='price_for_two',
        ),
        migrations.AddField(
            model_name='tours',
            name='price_for_one_bussines',
            field=models.CharField(blank=True, default=0, max_length=56, null=True),
        ),
        migrations.AddField(
            model_name='tours',
            name='price_for_one_classic',
            field=models.CharField(blank=True, default=0, max_length=56, null=True),
        ),
        migrations.AddField(
            model_name='tours',
            name='price_for_one_wine',
            field=models.CharField(blank=True, default=0, max_length=56, null=True),
        ),
        migrations.AddField(
            model_name='tours',
            name='price_for_two_bussines',
            field=models.CharField(blank=True, default=0, max_length=56, null=True),
        ),
        migrations.AddField(
            model_name='tours',
            name='price_for_two_classic',
            field=models.CharField(blank=True, default=0, max_length=56, null=True),
        ),
        migrations.AddField(
            model_name='tours',
            name='price_for_two_wine',
            field=models.CharField(blank=True, default=0, max_length=56, null=True),
        ),
    ]
