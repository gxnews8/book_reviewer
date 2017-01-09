from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','email','date_of_birth','photo','about_me','created_at','updated_at']
admin.site.register(Profile, ProfileAdmin)
