from django.db import models




class register1(models.Model):
    Uname=models.CharField(max_length=100)
    email=models.CharField(max_length=150)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    mobileno=models.IntegerField()
    password=models.CharField(max_length=20)
    is_verified=models.BooleanField(default=False)
    token=models.CharField(max_length=100,default=None)

def __str__(self):
        
    return self.Uname 