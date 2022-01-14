from django.urls import path

from mysite import views
# from mysite.views import about

urlpatterns = [

    path('', views.Index.as_view(), name='index'),
    path('about/', views.About.as_view(), name='about'),
    ]
