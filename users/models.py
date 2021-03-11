from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length = 25, null=False, blank=False, default="Enter your first name")
    lastName =  models.CharField(max_length = 25, null=False, blank=False, default="Enter your last name")
    #username = models.CharField(max_length=25, null=False, blank=False, unique=True, default=User.username)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
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
    Major = models.CharField(max_length=50, null=False, blank=False, default="Undeclared")
    Minor = models.CharField(max_length=50, null=True, blank=True)
    interest = models.TextField(default="What academic or commercial areas are you interested in?")
    expertise = models.TextField(default="Do you have any niche skills? For example: I can design and 3D print on SolidWorks.")
    research_goals = models.TextField(default="What do you want to get out of reserach? For example, you may be interested in research purely to pursue passion, or you may want to work towards a graduate school scholarship")
    look = (
        ('a research team to join.', ('Established Research Team')),
        ('a project to work on.', ('A fun project')),
        ('faculty to work under.', ('A faculty mentor')),
        ('nothing at the moment.', ('Nothing')),
        ('motivated cadets.', ('Recruiting Cadets')),
        ('anyone who needs help.', ('I want to help other people')),
        ('cadets looking to do research for three or four years.', ('Cadets interested in research that works towards a scholarship')),
    )
    
    lookingFor = models.CharField(
        max_length=75,
        choices=look,
        default='nothing at the moment.',
    )
    faculty_cadet = (
        ('Faculty', ('Faculty')),
        ('Cadet', ('Cadet')),
    )

    title = models.CharField(
        max_length=50,
        choices=faculty_cadet,
        default='Cadet',
    )
    twitter = models.CharField(max_length=30, null=False, blank=False, default="@")
    #insta = models.CharField(max_length=30, null=False, blank=False)
    #facebook = models.CharField(max_length=30, null=False, blank=False)
    #linkedin = models.CharField(max_length=30, null=False, blank=False)
    #tictok = models.CharField(max_length=30, null=False, blank=False)

    gradYear = models.IntegerField(blank=True, default=2023)
    company = models.CharField(max_length=2, blank=True, default="")
    phone = models.IntegerField(null=False, blank=False, default=+11111111111)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
