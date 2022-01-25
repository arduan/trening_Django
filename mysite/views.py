from django.db.models import Avg, Max, Min, Count, Sum
from django.utils.datetime_safe import datetime

from django.views.generic import TemplateView, ListView, DetailView, DateDetailView
from .models import Patients
from .forms import ArticleForm


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
    model = Patients
    template_name = 'patient_max.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['time_now'] = datetime.now()
        context['age_statistics'] = Patients.objects.aggregate(Max('age'), Min('age'), Avg('age'), Count('age'),
                                                               Sum('age'))
        return context


class ArticleFormView(ListView):
    model = Patients
    template_name = 'form_view.html'
    form = ArticleForm
