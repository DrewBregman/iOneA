from django.db import models
import datetime
from partial_date import PartialDate
from django import forms
from phone_field import PhoneField
from projects.models import Project
from django.contrib.auth.models import User

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


#class User(models.Model):
 #   name = models.CharField(max_length=50)

  #  def __str__(self):
   #     return self.name


#class userID(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
   # username = models.CharField(max_length=25, null=False, blank=False, unique=True)

  
    #email =  models.EmailField()
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

    #def __str__(self):
        #return self.username
    # def __str__(self):
    #   return self.firstName
    # def __str__(self):
    #   return self.lastName


    




# andrew_user = userID(username="andrewbregman", firstName="Andrew", lastName="bregman", email="andrew.bregman@westpoint.edu", phone=8563832480, gradYear="2023-5-23", company="D2")

