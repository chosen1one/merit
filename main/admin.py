from django.contrib import admin
from .models import UserExtention, Merit, Record
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class AdminRecord(admin.ModelAdmin): 
    list_display = ["id", "student", "teacher", "merit", "comment"]

class AdminMerit(admin.ModelAdmin):
    list_display = ["code", "points", "description"]

admin.site.register(Merit, AdminMerit)
admin.site.register(Record, AdminRecord)


class ExtentionInline(admin.StackedInline):
    model = UserExtention
    can_delete = False
    verbose_name_plural = "userextention"

class UserAdmin(BaseUserAdmin):
    inlines = [ExtentionInline]
    list_display = ['username', 'email', 'first_name', 'last_name', 'grade']
    
    def grade(self, x):
        return x.userextention.usertype()
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)