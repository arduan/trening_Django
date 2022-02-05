from django.db.models import Avg, Max, Min, Count, Sum
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import form_model
from .models import Patients


class Index(TemplateView):
    template_name = 'mysite/index.html'


class About(TemplateView):
    template_name = 'mysite/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['my_name'] = 'Иванов Виталий Иванович'
        context['my_email'] = 'arduan.ivanov@yandex.ru'
        return context


class PatientsListView(ListView):
    model = Patients
    template_name = 'patients_list.html'
    queryset = Patients.objects.all()
    counts = Patients.objects.count()


class PatientsDetailView(DetailView):
    model = Patients
    template_name = 'patients_detail.html'


class PatientStatisticsView(ListView):
    """
    Статистика по пациентам.
    """
    model = Patients
    template_name = 'patient_max.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['time_now'] = datetime.now()
        context['age_statistics'] = Patients.objects.aggregate(Max('age'), Min('age'), Avg('age'), Count('age'),
                                                               Sum('age'))
        return context


class MyCreateView(CreateView):
    """
    Создание записи в базу данных.
    """
    template_name = 'create.html'
    form_class = form_model
    success_url = '/patients_list/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Patients.objects.all()
        return context


class PacientUpdate(UpdateView):
    """
    Редактирование записи.
    """
    model = Patients
    fields = ['name', 'age', 'note', 'pulse', 'date']
    template_name = 'create.html'
    success_url = '/patients_list/'


class PacientDeleteView(DeleteView):
    model = Patients
    success_url = '/patients_list/'
    template_name = 'delete.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = Patients.objects.all()
        return context
