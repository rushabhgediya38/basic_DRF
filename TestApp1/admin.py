from django.contrib import admin

# Register your models here.

from .models import Course, CourseCategory

admin.site.register(Course)
admin.site.register(CourseCategory)
