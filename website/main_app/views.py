from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'main_app/home.html',context )