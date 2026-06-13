import csv
from django.http import HttpResponse
from .models import Volunteer, Task
from django.shortcuts import render

def export_volunteers_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="volunteers_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Name', 'Phone', 'Skills', 'Status', 'Joined Date'])

    volunteers = Volunteer.objects.all()
    for volunteer in volunteers:
        writer.writerow([
            volunteer.user.username,
            volunteer.user.get_full_name(),
            volunteer.phone_number,
            volunteer.skills,
            'Active' if volunteer.status else 'Inactive',
            volunteer.joined_date.strftime('%d-%m-%Y')
        ])
    
    return response
        