
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'mysite/index.html'


class About(TemplateView):
    template_name = 'mysite/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['title'] = 'О сайте'
        context['name'] = 'Бесплатные объявления'
        context['description'] = 'Lorem lkj jlkjd kjf; eiuiufhasjkldk авплжд Это просто текст'
        return context