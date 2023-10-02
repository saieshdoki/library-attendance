from django.db import models

# Create your models here.



class Attendance(models.Model):
    rollno=models.CharField(max_length=15)
    name=models.CharField(max_length=100,default='ABC')
    start=models.TimeField()
    end=models.TimeField()
    date=models.DateField()
    total=models.BigIntegerField(default=000000)
    month=models.CharField(max_length=50,default='November')
class vacancies1(models.Model):
    id1=models.BigIntegerField(default=1)
    vac=models.BigIntegerField()
class Books(models.Model):
    Name=models.CharField(max_length=100)
    dept=models.CharField(max_length=10)
    availability=models.IntegerField()
class student(models.Model):
    name=models.CharField(max_length=50)
    rollno=models.CharField(max_length=10)
    phone=models.BigIntegerField()
    email=models.EmailField()
    b1=models.CharField(max_length=500,default='NA')
    due1=models.DateField()
    b2=models.CharField(max_length=500,default='NA')
    due2=models.DateField()
    b3=models.CharField(max_length=500,default='NA')
    due3=models.DateField()
class papers(models.Model):
    dept=models.CharField(max_length=100)
    paper=models.FileField(upload_to='static/')
class papers1(models.Model):
    dept1=models.CharField(max_length=100)
    paper1=models.URLField()

