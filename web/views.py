from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from blog import settings
from web.models import Publication


def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html', context={
        'email': 'admin@test.com',
        'phone': '+1 234 567 890'
    })


def publications(request):
    publications_objects = Publication.objects.all().order_by('-date')
    return render(request, 'publications.html', context={'publications': publications_objects})


def publication(request, number):
    try:
        publications_object = Publication.objects.get(id=number)
    except Publication.DoesNotExist:
        return redirect('/publications')

    return render(request, 'publication.html', context={'publication': publications_object})


def publish(request):
    if request.method == 'POST':
        password = request.POST.get('password', '')
        title = request.POST.get('title', '')
        text = request.POST.get('text', '')

        if not password or not title or not text:
            return render(request, 'publish.html', {'error': 'Есть пустое поле'})
        if password != settings.PUBLICATION_PASSWORD:
            return render(request, 'publish.html', {'error': 'Не правильный пароль'})

        publication = Publication(text=text, title=title)
        publication.save()

        return redirect('/publication/' + str(publication.id))

    return render(request, 'publish.html')
