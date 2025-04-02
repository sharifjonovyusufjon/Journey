from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader
from .models import Travel
# Create your views here.

def main(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
