# Generated by Django 5.0.3 on 2024-04-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nizam', '0039_remove_question_survey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='no',
        ),
        migrations.RemoveField(
            model_name='question',
            name='yes',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
