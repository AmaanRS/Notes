from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import User_profile
from .models import Note

class User_profileInline(admin.StackedInline):
    model = User_profile

class CustomUserAdmin(UserAdmin):
    inlines = [User_profileInline]

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, CustomUserAdmin)  # Register User with custom admin

admin.site.register(User_profile)  # Register User_profile model separately

admin.site.register(Note)

