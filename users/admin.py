from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ["email", 'is_author', 'is_subscriber']

admin.site.register(User, UserAdmin)
