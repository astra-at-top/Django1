from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ["id","name","email","rollno","slug","date"]