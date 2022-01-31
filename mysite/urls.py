from django.urls import path

from mysite import views
from .views import PatientsDetailView, PatientsListView, About, Index, PatientStatisticsView, MyCreateView


urlpatterns = [

    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('patients_list/', PatientsListView.as_view(), name='patients'),
    path('patients_detail/<int:pk>/', PatientsDetailView.as_view(), name='detail'),
    path('patients_max/', PatientStatisticsView.as_view(), name='max'),
    path('form_view/',  MyCreateView.as_view(), name='form'),
    path('index_form/',  MyCreateView.as_view(), name='form2'),
    path('index_form3/', MyCreateView.as_view(), name='form3'),
    path('create/', MyCreateView.as_view(), name='create'),


    ]