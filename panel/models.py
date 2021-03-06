from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import AbstractUser


class Videos(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to='video')

    def __str__(self):
        return self.caption



class Exercises(models.Model):
    caption = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    exercise = models.FileField(upload_to='exercise')

    def __str__(self):
        return self.caption


class Responses(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='response')

    def __str__(self):
        return self.title



#class Responses(models.Model):
 #   caption = models.CharField(max_length=100)
  #  date = models.DateTimeField(auto_now=True)
   # response = models.FileField(upload_to='response')
#class Student_Login(models.Model):
 #   email_address = models.EmailField(max_length=50)
  #  student_number = models.IntegerField(default=False)
   # password = models.IntegerField(max_length=20, default=False)
#class Teacher_Login(models.Model):
  #  email_address = models.EmailField(max_length=50)
 #   password = models.IntegerField(max_length=20, default=False)
#class Results(models.Model):
 #   student_number = models.DecimalField(max_digits=610399300, decimal_places=0, null=False)
  #  date = models.DateTimeField(auto_now=True)
   # file = models.FileField()
   # score = models.DecimalField(max_digits=100, decimal_places=2, null=True)
#class Watch_Videos(models.Model):
   # title = models.CharField(max_length=50, null=True)
#class Upload_Exercises(models.Model):
 #   title = models.CharField(max_length=50, null=True)
  #  definition = models.TextField(max_length=100)
   # deadline  = models.DateTimeField(default=timezone.now)

    #def __str__(self):
     #   return self.title
#class Upload_Videos(models.Model):
    #title = models.CharField(max_length=50, null=True)
  #  definition = models.TextField(max_length=100)
   # video_file = models.FileField(upload_to='videos/', null=True)

#    def __str__(self):
   #     return self.title

