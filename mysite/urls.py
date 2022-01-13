from django.urls import path
from mysite.views import about

urlpatterns = [

    path('about/', about, name='about'),
    ]
