# Generated by Django 3.1.7 on 2021-03-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210308_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first',
            field=models.BooleanField(default=True),
        ),
    ]
