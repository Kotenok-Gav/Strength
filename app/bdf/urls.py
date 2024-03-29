from django.urls import path
from .import views
from .views import download_file

urlpatterns = [
    path('', views.home, name='home'),
    path('bdf/', views.bdf_list, name='bdf_list'),
    path('download/', views.download_file, name='download_file'),
    path('run_msc_nastran/', views.run_msc_nastran, name='run_msc_nastran'),
]
