from django.contrib import admin
from .models import UserExtention, Merit, Record

class AdminRecord(admin.ModelAdmin): 
    list_display = ["id", "student", "teacher", "merit", "comment"]

class AdminUserExtention(admin.ModelAdmin):
    list_display = ["id", "user", "grade"]

class AdminMerit(admin.ModelAdmin):
    list_display = ["code", "points", "description"]

admin.site.register(UserExtention, AdminUserExtention)
admin.site.register(Merit, AdminMerit)
admin.site.register(Record, AdminRecord)

