from django.shortcuts import render


def index(request):
    ip = request.META.get('REMOTE_ADDR')
    context = {
        'name': 'Виталий',
        'age': 26,
        'ip': ip,
    }
    return render(request, 'mysite/index.html', context)

def about(request):
    context = {'last_name': 'Иванов'}

    return render(request, 'mysite/about.html', context)

