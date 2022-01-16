from django.urls import path

from mysite import views


urlpatterns = [

    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    path('patients_list_view/', views.PatientsListView.as_view(), name='patients')
    ]
