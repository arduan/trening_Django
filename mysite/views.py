from django.shortcuts import render


def index(request):
    context = {
        'name': 'Виталий',
        'age': 26,
    }
    return render(request, 'mysite/index.html', context)

def about(request):
    context = {'last_name': 'Иванов'}

    return render(request, 'mysite/about.html', context)

