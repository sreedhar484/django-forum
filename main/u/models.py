from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import math
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='pics',default='default.png')
    bio = models.TextField(default=None,blank=True)
    role = (('student', 'Student'), ('alumni', 'Alumni'))
    acc_type = models.CharField(max_length=10, choices=role, default='student')
    noque = models.IntegerField(default=0)
    noans = models.IntegerField(default=0)
    noposts = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Question(models.Model):
    username = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    discription = models.TextField(default=None)
    quedata = models.DateTimeField(auto_now_add=True,auto_now=False)

class Queans(models.Model):
    username = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,default=None,on_delete=models.CASCADE)
    answer = models.TextField(default=None)
    photo = models.ImageField(default=None,upload_to='pics')
    video = models.FileField(default=None,upload_to='video')
    pdf = models.FileField(default=None,upload_to='pdf')
    ansdata = models.DateTimeField(auto_now_add=True,auto_now=False)


class Article(models.Model):
    username = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    discription = models.TextField(default=None)
    photo = models.ImageField(default=None,upload_to='pics')
    video = models.FileField(default=None,upload_to='video')
    pdf = models.FileField(default=None,upload_to='pdf')
    artdata = models.DateTimeField(auto_now_add=True,auto_now=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    view = models.IntegerField(default=0)


class Posts(models.Model):
    photo = models.ImageField(default=None,upload_to='posts')
    title = models.CharField(default=None,max_length=100)
    discription = models.TextField(default=None)

class Slide(models.Model):
    photo = models.ImageField(upload_to='slide')
    title = models.CharField(default=None,max_length=100)
    discription = models.TextField(default=None)

class Quiz(models.Model):
    question = models.TextField(default=None)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.question

class python(models.Model):
    question = models.TextField(default=None)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.question
    
class java(models.Model):
    question = models.TextField(default=None)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.question

class c(models.Model):
    question = models.TextField(default=None)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.question

class html(models.Model):
    question = models.TextField(default=None)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.question

class javascript(models.Model):
    question = models.TextField(default=None)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.question
    
class Quizres(models.Model):
    username = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    score = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    quizdate = models.DateTimeField(auto_now_add=True,auto_now=False)
    total = models.CharField(max_length=100)