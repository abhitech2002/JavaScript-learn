from django.shortcuts import render
from .models import ChaiVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def learn(request):
    chai_varities = ChaiVarity.objects.all()
    return render(request, 'world/all_chai.html', {'chai_varities': chai_varities})

def detail(request, chai_id):
    chai = get_object_or_404(ChaiVarity, pk=chai_id)
    return render(request, 'world/detail.html', {'chai': chai})

def chai_store_view(request):
    return render(request, 'world/chai_stores.html')