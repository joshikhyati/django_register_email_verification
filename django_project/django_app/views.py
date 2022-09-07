'''
This project doing email verification work.
'''

from django.shortcuts import render,HttpResponse
from .models import register1
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
import uuid
from django.core.mail import send_mail
from django.conf import settings

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
        else:
            messages.error(request,'both password are not matching')

    else:
        return render(request,'register.html')

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

def loginform(request):   
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

