from django.db import models
from django.contrib.auth.models import User

class Volunteer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True
    )
    address = models.TextField(blank=True)
    dob = models.DateField(
        null=True,
        blank=True
    )
    skills = models.TextField(
        blank=True,
        help_text='Comma separated list of skilss'
    )
    availability = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g., weekends, mornings, afternoons, evenings"
    )
    status = models.BooleanField(
        default=True,
        verbose_name="Active"
    )
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        name = self.user.get_full_name()
        return f"{name} ({self.user.username})" if name else self.user.username

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    duration = models.CharField(
        max_length=50,
        help_text="in hours"
    )
    required_skills = models.TextField(blank=True)
    assigned_volunteers = models.ManyToManyField(
        Volunteer,
        blank=True,
        related_name='tasks'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title