from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse('<h1>hello im fine thx and you?</h1>')