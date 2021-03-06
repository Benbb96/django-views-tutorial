from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.conf import settings


def index(request):
    context = {'template': 'homepage',
               'title': 'Django Views Tutorial',
               'description': mark_safe(f'Demo for creating views in Django (View on <a href="{settings.GITHUB_REPO}">Github</a>).')}
    return render(request, 'homepage/index.html', context)

