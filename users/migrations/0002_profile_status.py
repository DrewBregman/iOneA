# Generated by Django 3.1.7 on 2021-03-24 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Archived', 'Archived'), ('Deleted', 'Deleted')], default='Active', max_length=50),
        ),
    ]
