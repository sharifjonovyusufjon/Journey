from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from .models import Travel
# Create your views here.

def main(request):
    travels = Travel.objects.all().values()[:4]
    template = loader.get_template('home.html')
    context = {
        'travels': travels,
    }
    return HttpResponse(template.render(context, request))
