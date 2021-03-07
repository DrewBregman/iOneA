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

    class Meta:
        verbose_name_plural= "projects"

    def __str__(self):
        return self.name