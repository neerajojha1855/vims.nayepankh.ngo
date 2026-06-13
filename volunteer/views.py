import csv
from django.http import HttpResponse
from .models import Volunteer, Task
from django.views.generic import TemplateView
from django.shortcuts import render

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['volunteers'] = Volunteer.objects.all().order_by('-joined_date')
        context['total_volunteers'] = Volunteer.objects.count()
        context['active_volunteers'] = Volunteer.objects.filter(status=True).count()
        context['tasks'] = Task.objects.all().order_by('date')
        context['total_tasks'] = Task.objects.count()

        return context


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