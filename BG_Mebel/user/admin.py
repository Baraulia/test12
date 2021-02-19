from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AdvUser

class AdvUserAdmin(UserAdmin):
    pass


admin.site.register(AdvUser, AdvUserAdmin)

# Register your models here.
