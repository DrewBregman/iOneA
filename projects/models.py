from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
# Create your models here.
class Project(models.Model):

    name = models.CharField(max_length=30)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    bPic = models.ImageField(default='defaultproban.jpg', upload_to='project_banner')
    logo = models.ImageField(default='defaultlogo.jpg', upload_to='project_logo')
    dep_choice1 = (
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
    department = models.CharField(
        max_length=50,
        choices=dep_choice1,
        default='Independent',
    )
    description = models.CharField(max_length=50, null = True)
    purpose=models.TextField()
    tag_choice = (
        ('Data Analysis' , ('Data Analysis')),
        ('3D Printing' , ('3D Printing')),
        ('Robotics' , ('Robotics')),
        ('Coding' , ('Coding')),
        ('Frauds' , ('Frauds, AKA Law majors')),
    )

    projectTag = models.CharField(
        max_length=32,
        choices=tag_choice,
        default='Frauds',
    )

    look = (
        ('motivated cadets with niche expertise.', ('Expert Cadets')),
        ('cadets who want to learn and help.', ('Any cadet who wants to help')),
        ('an engineering cadet.', ('Engineering Cadet')),
        ('a cadet with a scientific background.', ('Scientific background')),
        ('cadets with programming experience.', ('Coding Background')),
       
    )
    
    lookingFor = models.CharField(
        max_length=75,
        choices=look,
        default='an engineering cadet,',
    )

    recruit = (
        ('Yes', ('Yes')),
        ('No', ('No')),
    )

    recruiting = models.CharField(
        max_length=50,
        choices=recruit,
        default='Yes',
    )
    class Meta:
        verbose_name_plural= "projects"

    def __str__(self):
        return self.name

class MemberList(models.Model):
    members = models.CharField(max_length=2000)
    def __str__(self):
        return self.members


class Member(models.Model):
    memberlist = models.ManyToManyField(MemberList)
    username = models.CharField(max_length=50, null = True)
    email = forms.EmailField()
    text = models.CharField(max_length=300)
    is_admin = models.BooleanField(null=True)
    admins = models.ManyToManyField(User, limit_choices_to={'is_admin': True})
    def __str__(self):
        return self.text
