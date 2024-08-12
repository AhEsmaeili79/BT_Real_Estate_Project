from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def about(requst):
    return render(requst,'pages/about.html')