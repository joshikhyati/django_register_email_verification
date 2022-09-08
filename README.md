
<h1 style='text-align:center'>Email-Verification for Django</h1>



Email verification for new signups or new users is a two-step verification process and adds a layer for security for valid users.
<hr>

## Requirements

+ Python >= 3.10.7
+ Django >= 4.1

## Setup

Start a project by the following command –

```commandline
 django-admin startproject django_project
 ```
 Change directory to project –
 
 ```commandline
  cd django_project
 ```
 
 Now,Start server by the following command
 
 ```commandline
   python manage.py runserver
  ```
  
  After running above command you get following url 
  
  ```commandline
    http://127.0.0.1:8000/ as URL.
    ```
    
   Click on URL link to  check whether the server is running or not.
   
   To stop server by pressing
   
   ```commandline
      ctrl-c
 ```
 
 Let’s create an app now called the “django_app”. 
 
 ```commandline
   python manage.py startapp django_app
```


<h4>Goto django_app/ folder and create a folder templates with files index.html, login.html,register.html,success.html files.</h4>


<h4>Goto django_app/ folder and create a folder Static with another folder assets in it bootstrap.min.css and main.css files.</h4>


## Settings parameters

<h5> settings.py </h5>


<h5>configure email settings in setting.py:</h5>

![alt tag](https://user-images.githubusercontent.com/93461145/189059671-2f93c5df-39e6-45ae-8c11-49c101934b9c.png)

<h5> setting for templates folder</h5>

![alt tag](https://user-images.githubusercontent.com/93461145/189061313-ff4ea5e9-0e39-4cb7-9365-034484d682c2.png)

<h5> setting for static folder to use css,js file in project</h5>

![alt tag](https://user-images.githubusercontent.com/93461145/189061799-ef256ac8-9e49-4a90-a614-dc037e62152c.png)

<h5>place your email and password here.</h5>

![alt tag](https://user-images.githubusercontent.com/93461145/189062996-cb2313f2-1544-44f8-85d4-76cec5327435.png)

<h4>Now let make a models in <b>"models.py"</b></h4>

This file we create model name register1 with Uname.Email,Gender,Age,Mobileno,password,is_verified,and Token feilds

```commandline
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
```
Now display a model in adminpanel we write code in "Admin.py"


```commandline

from django.contrib import admin
from .models import register1


class register1Admin(admin.ModelAdmin):
    list_display = ('Uname', 'email','gender' ,'age','mobileno','password','is_verified','token')
admin.site.register(register1, register1Admin)
```

<h3>Make migrations and migrate them. </h3>

<h5>python manage.py makemigrations</h5>
<h5>python manage.py migrate</h5>
