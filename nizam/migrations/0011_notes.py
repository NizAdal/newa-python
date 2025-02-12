# Generated by Django 5.0.3 on 2024-03-17 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nizam', '0010_alter_membership_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('dep', models.CharField(max_length=40)),
                ('year', models.CharField(max_length=40)),
                ('semester', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('subject', models.CharField(max_length=40)),
                ('phone', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(999999999999)])),
                ('file', models.ImageField(default='none', upload_to='president_images')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
