from django.db import models
from django.core.validators import MaxValueValidator,RegexValidator, MaxLengthValidator
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    sno= models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = RichTextField()
    slug = models.CharField(max_length=200)
    post_image = models.ImageField(upload_to='post image')
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class About(models.Model):
    sno= models.AutoField(primary_key=True)
    content = RichTextField()
    logo = models.ImageField(upload_to='president_images', default='none')   
    time = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sno= models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    content = RichTextField()    
    time = models.DateTimeField(auto_now_add=True)
    president = models.ImageField(upload_to='president_images', default='none')
    def __str__(self):
        return self.name

class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.IntegerField(validators=[MaxValueValidator(999999999999)])
    desc = models.TextField()
    time = models.DateTimeField(auto_now_add = True)  
    def __str__(self):
        return self.name

class Membership(models.Model):
    sno = models.AutoField(primary_key = True)
    status = models.BooleanField(default = False)
    name = models.CharField(max_length=40)
    father = models.CharField(max_length=40)
    date =models.CharField(max_length=10,validators=[MaxLengthValidator(10),RegexValidator(r'^\d{2}[-\/]\d{2}[-\/]\d{4}$', 'Date format must be MM-DD-YYYY or MM/DD/YYYY')])
    dep = models.CharField(max_length=40)
    year = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.IntegerField(validators=[MaxValueValidator(999999999999)])
    file = models.ImageField(upload_to='members_images/', default='none')
    time = models.DateTimeField(auto_now_add = True)    
    def __str__(self):
        return self.name


class Notes(models.Model):
    sno = models.AutoField(primary_key = True)
    status = models.BooleanField(default = False)
    name = models.CharField(max_length=40)    
    dep = models.CharField(max_length=40)
    year = models.CharField(max_length=40)
    semester =  models.CharField(max_length=40)
    subject = models.CharField(max_length=40)
    teacher = models.CharField(max_length=40)
    phone = models.IntegerField(default = 0, blank = True, null = True)
    file = models.FileField(upload_to='Notes', default='none')
    time = models.DateTimeField(auto_now_add = True)    
    def __str__(self):
        return self.name   

            

class Survey(models.Model):
    topic = models.CharField(default = "", max_length=50)

class Data(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=40)    
    dept = models.CharField(max_length=40)    
    rollno = models.CharField(max_length=40, unique=True)    
    year = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class Questions(models.Model):
    sno = models.AutoField(primary_key = True)
    question1 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer1 = models.CharField(default = "",max_length=50,blank= True , null=True)
    question2 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer2 = models.CharField(default = "",max_length=50,blank= True , null=True)
    question3 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer3= models.CharField(default = "",max_length=50,blank= True , null=True)
    question4 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer4 = models.CharField(default = "",max_length=50,blank= True , null=True)
    question5 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer5 = models.CharField(default = "",max_length=50,blank= True , null=True)
    question6 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer6 = models.CharField(default = "",max_length=50,blank= True , null=True)
    question7 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer7 = models.CharField(default = "",max_length=50,blank= True , null=True)
    question8 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer8 = models.CharField(default = "",max_length=50,blank= True , null=True)
    question9 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer9 = models.CharField(default = "",max_length=50,blank= True , null=True)
    question10 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer10 = models.CharField(default = "",max_length=50,blank= True , null=True)
    question11 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer11 = models.CharField(default = "",max_length=50,blank= True , null=True)
    question12 = models.CharField(default = "", max_length=50,blank= True , null=True)
    answer12 = models.CharField(default = "",max_length=50,blank= True , null=True)
