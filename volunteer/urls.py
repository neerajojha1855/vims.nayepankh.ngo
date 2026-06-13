from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import VolunteerViewSet, TaskViewSet
from .views import export_volunteers_csv

router = DefaultRouter()
router.register(r'api/volunteers', VolunteerViewSet)
router.register(r'api/tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('export/', export_volunteers_csv, name='export_volunteers'),
]