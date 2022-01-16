
from django.views.generic import TemplateView
from .models import Patients


class Index(TemplateView):
    template_name = 'mysite/index.html'




class About(TemplateView):
    template_name = 'mysite/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['title'] = 'О сайте'
        context['name'] = 'Иванов Виталий Иванович'

        return context