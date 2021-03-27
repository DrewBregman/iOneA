from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from Notifications.models import Notification
from multiselectfield import MultiSelectField
from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField("First Name", max_length = 25, null=False, blank=False, default="")
    lastName =  models.CharField("Last Name",max_length = 25, null=False, blank=False, default="")
    #username = models.CharField(max_length=25, null=False, blank=False, unique=True, default=User.username)
    image = models.ImageField("Profile Picture",default='default.jpg', upload_to='profile_pics')
    email =  models.EmailField(default="")
    first = models.BooleanField(default = True)
    #MeetMe = models.TextField()
    
    dep_choice = (
        ('Behavioral Sciences and Leadership', ('Behavioral Sciences and Leadership')),
        ('Chemistry and Life Science', ('Chemistry and Life Science')),
        ('Civil and Mechanical Engineering', ('Civil and Mechanical Engineering')),
        ('Electrical Engineering and Comptuer Science', ('Electrical Engineering and Comptuer Science')),
        ('English and Philosophy', ('English and Philosophy')),
        ('Foreign Languages', ('Foreign Languages')),
        ('Geography and Environmental Engineering', ('Geography and Environmental Engineering')),
        ('History', ('History')),
        ('Law', ('Law')),
        ('Mathematical Sciences', ('Mathematical Sciences')),
        ('Physics and Nuclear Engineering', ('Physics and Nuclear Engineering')),
        ('Social Sciences', ('Social Sciences')),
        ('Systems Engineering', ('Systems Engineering')),
        ('Independent', ('Independent')),
    )
    Department = models.CharField(
        max_length=50,
        choices=dep_choice,
        default='Independent',
    )

    #title = models.CharField(max_length=30, null=False, blank=False)
    Major = models.CharField(max_length=50, null=True, blank=False)
    Minor = models.CharField(max_length=50, null=True, blank=True)
    interest = models.TextField("What Are Your Interests?", null = True)
    expertise = models.TextField("Please list Your Areas of Expertise (separate by commas)", null = True)
    research_goals = models.TextField("What Do You Want To Get Out Of Research?", null = True)
    look = (
        ('a research team to join.', ('an established Research Team')),
        ('a project to work on.', ('a fun project to work on')),
        ('faculty to work under.', ('a faculty mentor')),
        ('nothing at the moment.', ('nothing at the moment')),
        ('start project', ('to start a research project')),
        ('anyone who needs help.', ('the opportunity to help other people however I can')),
        ('cadets looking to do research for three or four years.', ('cadets interested in research that works towards a scholarship')),
        ('cadets who want to join a project.', ('cadets who want to join a project')),
        ('AIADs.', ('AIADs')),
    )
    #lookingFor = models.CharField(
        #max_length=75,
        #choices=look, lookOne, lookTwo,
        #default='nothing at the moment.',
    #)

    lookingFor = MultiSelectField("What Are You Currently Looking For?", choices= look, max_choices=3)
    faculty_cadet = (
        ('Faculty', ('Faculty')),
        ('Cadet', ('Cadet')),
    )

    title = models.CharField(
        max_length=50,
        choices=faculty_cadet,
        default='Cadet',
    )
    twitter = models.CharField(max_length=30, null=True, blank=True, default="@")
    #insta = models.CharField(max_length=30, null=False, blank=False)
    #facebook = models.CharField(max_length=30, null=False, blank=False)
    #linkedin = models.CharField(max_length=30, null=False, blank=False)
    #tictok = models.CharField(max_length=30, null=False, blank=False)

    gradYear = models.IntegerField("Graduation Year", null=True, blank=True, default=2023)
    company = models.CharField(max_length=2, null=True, blank=True, default="")
    phone = PhoneNumberField(null=True, blank=False, default = '') #, unique=True)
    statusOptions = (
        ('Active', ('Active')),
        ('Archived', ('Archived')),
        ('Deleted', ('Deleted')),
    )

    status = models.CharField(
        max_length=50,
        choices=statusOptions,
        default='Active',
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def add_notification(self, message):
        notification = Notification(user=self.user, message=message)
        notification.save()