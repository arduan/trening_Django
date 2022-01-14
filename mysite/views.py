from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def index(request):
    ip = request.META.get('REMOTE_ADDR')
    context = {
        'name': 'Виталий',
        'age': 26,
        'ip': ip,
    }
    return render(request, 'mysite/index.html', context)


# class About(View):
#     def get(self, request):
#         return render(request, 'mysite/about.html', {})


class About(TemplateView):
    template_name = 'mysite/about.html'

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context['title'] = 'О сайте'
        context['name'] = 'Бесплатные объявления'
        context['description'] = 'Lorem lkj jlkjd kjf; eiuiufhasjkldk'
        return context