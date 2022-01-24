from django.urls import path

from mysite import views
from .views import PatientsDetailView, PatientsListView, About, Index, max_age

urlpatterns = [

    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('patients_list/', PatientsListView.as_view(), name='patients'),
    path('patients_list/', max_age, name='age_max'),
    path('patients_detail/<int:pk>/', PatientsDetailView.as_view(), name='detail'),

    ]
