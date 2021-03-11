from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=30)
    department=models.CharField(max_length=30)
    numUser=models.IntegerField()
    bPic = models.ImageField(
        upload_to ='uploads', blank=False)

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

    class Meta:
        verbose_name_plural= "projects"

    def __str__(self):
        return self.name