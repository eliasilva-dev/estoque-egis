from django.contrib import admin

# Register your models here.
from user.models import UserProfile

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display= ['user', 'phone_number', 'department']