from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn(request):
    return render(request, 'world/all_chai.html')