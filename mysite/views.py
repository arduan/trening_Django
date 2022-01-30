from django.db.models import Avg, Max, Min, Count, Sum
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from django.views.generic import TemplateView, ListView, DetailView

from .forms import form_model, UniverseForm, AddPatientForm
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
    model = Patients
    template_name = 'patient_max.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['time_now'] = datetime.now()
        context['age_statistics'] = Patients.objects.aggregate(Max('age'), Min('age'), Avg('age'), Count('age'),
                                                               Sum('age'))
        return context


def add_page(request):
    if request.method == 'POST':
        form = AddPatientForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('form3')
            except:
                form.add_error(None, 'Ошибка добавления данных')

        else:
            form = AddPatientForm()

        return render(request, 'form_index3.html', {'form': form})


def my_form(request):
    form = form_model(request.POST)
    return render(request, 'form_view.html', {'form': form})


def index_form(request):
    context = {'form': UniverseForm()}
    return render(request, 'form_index.html', context)


def index_form3(request):
    context = {'form': AddPatientForm}
    return render(request, 'form_index3.html', context)
