
from django.views.generic import TemplateView
from .models import Patients


class Index(TemplateView):
    template_name = 'mysite/index.html'

    def context_data_patient(self):
        return Patients.objects.order_by('name')


class About(TemplateView):
    template_name = 'mysite/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['title'] = 'О сайте'
        context['name'] = 'Бесплатные объявления'
        context['description'] = 'Lorem lkj jlkjd kjf; eiuiufhasjkldk авплжд Это просто текст'
        dic_name = {'name': 'Виталий', 'last_name': 'Иванов'}
        context = dic_name
        return context