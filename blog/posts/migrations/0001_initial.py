# Generated by Django 5.1.3 on 2024-12-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
