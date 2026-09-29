from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "department", "level", "created_at")
    search_fields = ("full_name", "email", "department")
    list_filter = ("level", "department")
