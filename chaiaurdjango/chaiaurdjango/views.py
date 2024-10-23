from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the chaiaurdjango index.")

def about(request):
    return HttpResponse("Hello, world. You're at the chaiaurdjango about.")

def contact(request):
    return HttpResponse("Hello, world. You're at the chaiaurdjango contact.")