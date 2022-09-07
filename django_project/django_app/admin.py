from django.contrib import admin
from .models import register1



class register1Admin(admin.ModelAdmin):
    list_display = ('Uname', 'email','gender' ,'age','mobileno','password','is_verified','token')
admin.site.register(register1, register1Admin)