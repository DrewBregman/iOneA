# Generated by Django 3.1.7 on 2021-03-08 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210308_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Department',
            field=models.CharField(choices=[('Behavioral Sciences and Leadership', 'Behavioral Sciences and Leadership'), ('Chemistry and Life Science', 'Chemistry and Life Science'), ('Civil and Mechanical Engineering', 'Civil and Mechanical Engineering'), ('Electrical Engineering and Comptuer Science', 'Electrical Engineering and Comptuer Science'), ('English and Philosophy', 'English and Philosophy'), ('Foreign Languages', 'Foreign Languages'), ('Geography and Environmental Engineering', 'Geography and Environmental Engineering'), ('History', 'History'), ('Law', 'Law'), ('Mathematical Sciences', 'Mathematical Sciences'), ('Physics and Nuclear Engineering', 'Physics and Nuclear Engineering'), ('Social Sciences', 'Social Sciences'), ('Systems Engineering', 'Systems Engineering'), ('Independent', 'Independent')], default='Independent', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='Major',
            field=models.CharField(default='Undeclared', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='Minor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.CharField(blank=True, default='', max_length=2),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='profile',
            name='expertise',
            field=models.TextField(default='Do you have any niche skills? For example: I can design and 3D print on SolidWorks.'),
        ),
        migrations.AddField(
            model_name='profile',
            name='firstName',
            field=models.CharField(default='Enter your first name', max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='gradYear',
            field=models.IntegerField(blank=True, default=2023),
        ),
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.TextField(default='What academic or commercial areas are you interested in?'),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastName',
            field=models.CharField(default='Enter your last name', max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='lookingFor',
            field=models.CharField(choices=[('a research team to join.', 'Established Research Team'), ('a project to work on.', 'A fun project'), ('faculty to work under.', 'A faculty mentor'), ('nothing at the moment.', 'Nothing'), ('motivated cadets.', 'Recruiting Cadets'), ('anyone who needs help.', 'I want to help other people'), ('cadets looking to do research for three or four years.', 'Cadets interested in research that works towards a scholarship')], default='nothing at the moment.', max_length=75),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(default=11111111111),
        ),
        migrations.AddField(
            model_name='profile',
            name='research_goals',
            field=models.TextField(default='What do you want to get out of reserach? For example, you may be interested in research purely to pursue passion, or you may want to work towards a graduate school scholarship'),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(choices=[('Faculty', 'Faculty'), ('Cadet', 'Cadet')], default='Cadet', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.CharField(default='@', max_length=30),
        ),
    ]