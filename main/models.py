from django.db import models
import datetime
from partial_date import PartialDate
from django import forms
from phone_field import PhoneField


# Create your models here.
class ToDoList(models.Model):
    uname = models.CharField(max_length=200)

    def __str__(self):
        return self.uname


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class userID(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=25, null=False, blank=False, unique=True)

    # firstName = models.CharField(max_length = 25, null=False, blank=False)
    # lastName =  models.CharField(max_length = 25, null=False, blank=False)
    # email =  models.EmailField()
    # pas = models.CharField(max_length=50, null=False, blank=False)
    # class UserForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # phone = PhoneField(null=False, blank=False, unique=True, help_text='Contact phone number')
    # phone = models.IntegerField(null=False, blank=False)
    # gradYear = models.IntegerField(_('year'), validators=[MinValueValidator(1984), max_value_current_year])
    # gradYear = PartialDate("2023")
    # gradYear.format('%Y')
    # gradYear = models.IntegerField()
    # company = models.CharField(max_length = 2)

    def __str__(self):
        return self.username
    # def __str__(self):
    #   return self.firstName
    # def __str__(self):
    #   return self.lastName


class uBio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    MeetMe = models.CharField(max_length=150, null=False, blank=False)
    Department = models.CharField(max_length=100, null=False, blank=False)
    Title = models.CharField(max_length=30, null=False, blank=False)
    Major = models.CharField(max_length=50, null=False, blank=False)
    Minor = models.CharField(max_length=50, null=False, blank=False)
    aInterest = models.TextField()
    aExpertise = models.TextField()
    rGoal = models.TextField()
    bPic = models.ImageField(height_field='396', width_field='384')
    uPic = models.ImageField(height_field='320', width_field='320')
    curLooking = models.TextField()
    twitter = models.CharField(max_length=30, null=False, blank=False)
    insta = models.CharField(max_length=30, null=False, blank=False)
    facebook = models.CharField(max_length=30, null=False, blank=False)
    linkedin = models.CharField(max_length=30, null=False, blank=False)
    tictok = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.user


class uProjects(models.Model):
    user = models.ForeignKey(userID, on_delete=models.CASCADE)
    # waiting on relational tables to import data from there


# andrew_user = userID(username="andrewbregman", firstName="Andrew", lastName="bregman", email="andrew.bregman@westpoint.edu", phone=8563832480, gradYear="2023-5-23", company="D2")


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
