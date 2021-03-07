from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    numUser=models.IntegerField()
    purpose=models.TextField()

    tag_choice = (
        ('d' , ('Data Analysis')),
        ('p' , ('3D Printing')),
        ('r' , ('Robotics')),
        ('c' , ('Coding')),
        ('f' , ('Frauds, AKA Law majors')),

    )

    projectTag = models.CharField(
        max_length=32,
        choices=tag_choice,
        default='f',
    )
    numUsers = models.IntegerField(blank = False, null = False)
    CIC_OIC = models.CharField(max_length=100)
    Purpose = models.TextField()
    ifRecruting = models.BooleanField()
    name = models.CharField(max_length=100)
    #bPic = models.ImageField(height_field='396', width_field='396')
    #pPic = models.ImageField(height_field='320', width_field='320')
    currentlyWorkingOn = models.TextField()
    class Meta:
        verbose_name_plural= "projects"

    def __str__(self):
        return self.name