from django.urls import path

from mysite import views
# from mysite.views import about

urlpatterns = [

    # path('about/', about, name='about'),
    path('about/', views.About.as_view(), name='about'),
    ]
