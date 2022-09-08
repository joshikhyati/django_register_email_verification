
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

![alt tag](https://user-images.githubusercontent.com/93461145/189059166-a4b5fa1c-7f5f-4555-82d4-4a09b65ada39.png)


