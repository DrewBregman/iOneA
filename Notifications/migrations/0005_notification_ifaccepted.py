# Generated by Django 3.1.7 on 2021-03-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications', '0004_auto_20210320_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='ifAccepted',
            field=models.BooleanField(default=False),
        ),
    ]
