# Generated by Django 5.0.3 on 2024-03-23 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nizam', '0018_alter_membership_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option1', models.CharField(max_length=40)),
                ('option2', models.CharField(max_length=40)),
                ('q1', models.CharField(max_length=40)),
                ('q2', models.CharField(max_length=40)),
                ('q3', models.CharField(max_length=40)),
                ('q4', models.CharField(max_length=40)),
                ('q5', models.CharField(max_length=40)),
                ('q6', models.CharField(max_length=40)),
                ('q7', models.CharField(max_length=40)),
                ('q8', models.CharField(max_length=40)),
                ('q9', models.CharField(max_length=40)),
                ('q10', models.CharField(max_length=40)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
