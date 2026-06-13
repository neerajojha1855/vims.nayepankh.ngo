from django.contrib import admin
from .models import Volunteer, Task

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'status', 'joined_date')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'skills')
    list_filter = ('status', 'availability')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'duration')
    search_fields = ('title', 'required_skills')
    filter_horizontal = ('assigned_volunteers',)