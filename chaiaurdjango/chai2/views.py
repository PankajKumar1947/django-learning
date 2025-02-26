from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety

# Create your views here.
def allChai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai2/all_chai.html', {'chais': chais})

def chaiDetail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai2/chai_detail.html', {'chai': chai})