from django.db.models import Avg, Max
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, DateDetailView
from .models import Patients


class Index(TemplateView):
    template_name = 'mysite/index.html'


class About(TemplateView):
    template_name = 'mysite/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['my_name'] = 'Иванов Виталий Иванович'
        return context


class PatientsListView(ListView):
    model = Patients
    template_name = 'patients_list.html'
    queryset = Patients.objects.all()
    counts = Patients.objects.count()
    age_max = Patients.objects.all().aggregate(Max('age'))


class PatientsDetailView(DetailView):
    model = Patients
    template_name = 'patients_detail.html'


