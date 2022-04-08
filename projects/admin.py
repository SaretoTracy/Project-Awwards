from django.contrib import admin
from .models import Profile,Projects

# Register your models here.
class PhotosAdmin(admin.ModelAdmin):

    admin.site.register(Projects)
    admin.site.register(Profile)
    
    