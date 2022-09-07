from unicodedata import name
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('registerform',views.registerform,name='registerform'),
    path('success/', views.success, name="success"),
    path('loginform/', views.loginform, name="loginform"),
    path('verify/<str:token>',views.verify),
]