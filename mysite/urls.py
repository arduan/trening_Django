from django.urls import path

from mysite import views
from .views import PatientsDetailView, PatientsListView

urlpatterns = [

    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('patients_list_view/', PatientsListView.as_view(), name='patients'),
    path('patients_list_view/<int:pk>/', PatientsDetailView.as_view(), name='patients-detail'),

    ]
