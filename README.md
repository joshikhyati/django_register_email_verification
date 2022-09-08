
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


## Lets start Project 

<h4>Now let make a models in <b>"models.py"</b></h4>

This file we create model name register1 with Uname.Email,Gender,Age,Mobileno,password,is_verified,and Token feilds

```python
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


```python

from django.contrib import admin
from .models import register1


class register1Admin(admin.ModelAdmin):
    list_display = ('Uname', 'email','gender' ,'age','mobileno','password','is_verified','token')
admin.site.register(register1, register1Admin)
```

<h3>Make migrations and migrate them. </h3>

<h5>python manage.py makemigrations</h5>
<h5>python manage.py migrate</h5>

Now create superuser with folling commandline

```commandline
 python manage.py createsuperuser
 ```
 Than "Superuser" username, emailid, password to login in Admin 
 
 <h2>Edit "urls.py" file in project :</h2>  
 
 <hr>
 
 "urls.py\django_project
 
 ```python
 
 from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('django_app.urls')),
]

```

 <h2>Edit "views.py" file in django_app :</h2>
 
<h5>Signup or Register form  code </h5>
 
 ```python
 
from django.shortcuts import render,HttpResponse
from .models import register1
from django.contrib import messages
import uuid


def registerform(request):
    if request.method=="POST":
        Uname=request.POST['Uname']
        email=request.POST['email']
        gender=request.POST['gender']
        age=request.POST['age']
        mobileno=request.POST['mobileno']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        token=str(uuid.uuid4())
        

        if password==confirmpassword:
            if register1.objects.filter(Uname=Uname).exists():
                messages.error(request,'Username already exists')
            elif register1.objects.filter(email=email).exists():
                messages.error(request,'email already exists')
            else:
                user=register1.objects.create(Uname=Uname,email=email,gender=gender,age=age,mobileno=mobileno,password=password,token=token)
                user.save()
                 else:
            messages.error(request,'both password are not matching')

    else:
        return render(request,'register.html')
 ```

<h4>Register.html</h4>
 Make a form of signup this containe username,email,gender,age,mobileno,password feilds and submit button
 
 ```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {% load static %}  
    <link href="{% static 'assets/bootstrap.min.css' %}" rel="stylesheet">
    <link href="{% static 'assets/main.css' %}" rel="stylesheet">
    
    <title>documantion</title>
   </head>
<body>
   
 <section>
   <nav class="navbar bg">
     <a href="/" class="navbar-brand">Login</a>
   </nav>
 </section>
 <section class="bg-bg">
   <div class="container-fluid">
      <div class="row">
         <div class="col-md-6" >
           <div class="text">
            <h1>Wel-Come Page</h1>
            </div>
            </div>
            <div class="col-md-6">
               <div class="card">
               
                  <div class="card-title">
                     <h1>Login Here</h1>
                  </div>
                  <div class="card-body">
                     <form class="form" method="POST" action="{% url 'registerform' %}" enctype="multipart/form-data">
                        {% csrf_token %}
                        <label>User name</label><br>
                        <input type="text" class="form-control" name="Uname"><br>
                        <label>Email</label><br>
                        <input type="email" class="form-control" name="email"><br>
                        <label>Gender</label><br>
                        <input type="text" class="form-control" name="gender"><br>
                        <label>Age</label><br>
                        <input type="number" class="form-control" name="age"><br>
                        <label>Mobileno</label><br>
                        <input type="number" class="form-control" name=" mobileno"><br>
                        <label>Password</label><br>
                        <input type="password" class="form-control" name="password"><br><br>
                        <label>ConfirmPassword</label><br>
                        <input type="password" class="form-control" name="confirmpassword"><br><br>
                        
                        <input type="submit" class="btn btn-primary btn-block btn-lg" value="Login">
                    
                     </form>
                  </div>
               </div>
            </div>
           </div>
         </div>
 </section>
</body>
</html>
```

<h3>Mail sending</h3>
<hr>

Mail sending code in send mail subject, mailbody(link with token number),from emailid,to email.

```python
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
                domain_name=get_current_site(request).domain
                link=f'http://{domain_name}/verify/{token}',
                send_mail(
                        'Email Verification',
                        f'please click{link}to verify your email',
                        settings.EMAIL_HOST_USER,
                        [email],
                        fail_silently=False,
                        )
                return HttpResponse('email send')
```

<h2>Verify Mail</h2>

verify function verify mail with following code in "views.py"

```python
def verify(request,token):
    
    try:
        user=register1.objects.filter(token=token).first()
        if user:
            user.is_verified=True
            user.save()
            msg='your email has been verified'
            return render(request,'success.html',{'msg':msg})
        else:
            user.is_verified=False
            msg = 'Your acccount not verified'
            return render(request,'success.html',{'msg':msg})
    except Exception as e:
            msg=e
            return render(request,'success.html',{'msg':e})
            
def success(request):
   
    return render(request,'success.html')
```

<h4>Now lets create "urls.py" in django_app </h4>

Mapping of views function or we can also say path of url 

```python
from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registerform',views.registerform,name='registerform'),
    path('success/', views.success, name="success"),
    path('login/', views.login, name="login"),
    path('verify/<str:token>',views.verify),
]
```

After successfully verify mail or token redirect at "success.html" 
<h2>Success.html</h2>
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
   <h3>
    {{msg}}<a href="{% url 'loginform' %}">Click Here</a>to Login your Account
   </h3> 
</body>
</html>
```
<h2>Now you can run the server to see your app.</h2>

```commandline
python manage.py runserver
```
