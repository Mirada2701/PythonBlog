# Generated by Django 5.1.3 on 2024-12-09 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_rename_news_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]