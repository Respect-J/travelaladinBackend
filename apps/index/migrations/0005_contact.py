# Generated by Django 5.0.1 on 2024-02-08 13:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_excluded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number_uz', models.CharField(blank=True, max_length=20, null=True)),
                ('number_ru', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]