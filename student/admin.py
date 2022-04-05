from django.contrib import admin
from .models import student, Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display=["name"]
    search_fields=["name"]

admin.site.register(Department, DepartmentAdmin)

class studentAdmin(admin.ModelAdmin):
    list_display=["name", "deparment"]
    list_filter=["deparment"]
    search_fields=["name"]

admin.site.register(student, studentAdmin)
