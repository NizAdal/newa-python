# Generated by Django 5.0.3 on 2024-03-11 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=200)),
                ('post_image', models.ImageField(upload_to='post image')),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
