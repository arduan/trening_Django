from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView
from .models import Patients


class Index(TemplateView):
    template_name = 'mysite/index.html'


class About(TemplateView):
    template_name = 'mysite/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['my_name'] = 'Иванов Виталий Иванович'
        return context


class PatientsListView(generic.ListView):
    model = Patients
    template_name = 'patients_list.html'
    queryset = Patients.objects.all()


class PatientsDetailView(generic.DetailView):
    model = Patients
    template_name = 'patients_detail.html'
