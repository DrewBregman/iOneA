from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
from multiselectfield import MultiSelectField
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    bPic = models.ImageField("Choose Your Project Banner Picture", default='defaultproban.jpg', upload_to='project_banner')
    logo = models.ImageField("Choose Your Project Logo", default='defaultlogo.jpg', upload_to='project_logo')
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
    purpose = models.CharField("Enter your project's purpose", max_length=50,null=True)
    description=models.TextField("Please give a brief description of your project, progress, team, and goals.", null=True)
    tag_choice = (
        ('Data Analysis' , ('Data Analysis')),
        ('3D Printing' , ('3D Printing')),
        ('Robotics' , ('Robotics')),
        ('Coding' , ('Coding')),
        ('Science' , ('Science')),
        ('Drones' , ('Drones')),
        ('Math' , ('Math')),
        ('Chemistry' , ('Chemistry')),
        ('Nuclear Engineering' , ('Nuclear Engineering')),
        ('Physics' , ('Physics')),
        ('Photonics' , ('Photonics')),
        ('MATLAB' , ('MATLAB')),
        ('SolidWorks' , ('SolidWorks')),
        ('Writing' , ('Writing')),
        ('Graphic Design' , ('Graphic Design')),
        ('Design' , ('Design')),
        ('Robotics' , ('Robotics')),
        ('Business' , ('Business')),
        ('Stocks' , ('Stocks')),
        ('Hacking' , ('Hacking')),
        ('Law' , ('Law Studies')),
        ('Coding' , ('Coding')),
        ('Environmental' , ('Environment')),
        ('Lifestyle' , ('Lifestyle')),
        ('Kinesiology' , ('Kinesiology')),
        ('Health' , ('Health')),
        ('Sleep' , ('Sleep')),
        ('Psychology' , ('Psychology')),
        ('Material Science' , ('Material Science')),
        ('Batteries' , ('Batteries')),
        ('Energy' , ('Energy')),
        ('Fiber Optics' , ('Fiber Optics')),
        ('Space' , ('Space')),
        ('Autonomous Vehicles' , ('Autonomous Vehicles')),
        ('Biology' , ('Biology')),
    )

    projectTag = MultiSelectField(
                "Choose Up To 5 Tags", 
                choices= tag_choice, 
                max_choices=5
    )

    look = (
        ('Expert Cadets.', ('motivated cadets with niche expertise.')),
        ('Any cadet who wants to help.', ('cadets who want to learn and help.')),
        ('an engineering cadet.', ('an engineering Cadet')),
        ('a cadet with a scientific background.', ('a cadet with a scientific background')),
        ('cadets with programming experience.', ('cadets with programming experience')),
        ('Stem interests.', ('cadets with an interest in STEM.')),
        ('scholarship', ('cadets seeking scholarships from research')),
        ('a lot of work.', ('cadets who can work 10-20 hours a week')),
        ('anyone', ('anyone!')),
        ('Nothing', ('nothing at the moment')),
    )
    
    lookingFor = MultiSelectField(
                "What Does This Project Need", 
                choices= look, 
                max_choices=5
    )

    recruit = (
        ('Yes', ('Yes')),
        ('No', ('No')),
    )

    recruiting = models.CharField(
        "Is This Project Currently Recruiting?",
        max_length=50,
        choices=recruit,
        default='Yes',
    )
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



class uProjects(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="u")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="uProj")
    ifAccepted = models.BooleanField(null = True, blank=False, default=False)
    #ifLeader = models.BooleanField(null = False, blank=False)
    ifAdmin = models.BooleanField("Do you want this user to be a project Admin?",null = True, blank=False, default=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.user.username + ',' + self.project.name