# Generated by Django 3.0.5 on 2020-05-04 08:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app_website', '0003_auto_20200504_1129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pic',
            name='src',
        ),
        migrations.AddField(
            model_name='pic',
            name='img_url',
            field=models.ImageField(default='', upload_to='img'),
        ),
        migrations.AlterField(
            model_name='pic',
            name='time',
            field=models.DateTimeField(default='2020-05-04 16:21:17'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='time',
            field=models.DateTimeField(default='2020-05-04 16:21:17'),
        ),
    ]