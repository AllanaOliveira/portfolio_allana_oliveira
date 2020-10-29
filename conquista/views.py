from django.shortcuts import render

# Create your views here.
from conquista.models import Conquista

def index(request):
    linha_do_tempo = Conquista.objects.all().order_by('data')
    return render(request, 'conquista/index.html', {'linhas_do_tempo': linha_do_tempo })