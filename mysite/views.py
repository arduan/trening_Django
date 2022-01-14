from django.shortcuts import render
from django.views import View


def index(request):
    ip = request.META.get('REMOTE_ADDR')
    context = {
        'name': 'Виталий',
        'age': 26,
        'ip': ip,
    }
    return render(request, 'mysite/index.html', context)


class About(View):
    def get(self, request):
        return render(request, 'mysite/about.html', {})
