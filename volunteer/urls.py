from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import VolunteerViewSet, TaskViewSet
from .views import export_volunteers_csv, export_volunteers_pdf

router = DefaultRouter()
router.register(r'volunteers', VolunteerViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('export/', export_volunteers_csv, name='export_volunteers'),
    path('export/pdf/', export_volunteers_pdf, name='export_volunteers_pdf'),
]