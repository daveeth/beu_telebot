from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view_test(request):
    return HttpResponse('<h1 style="background-color:red; color:white" >Under Development, folks</h1>')

def home_view(request):
    return render(request, "app/base.html")