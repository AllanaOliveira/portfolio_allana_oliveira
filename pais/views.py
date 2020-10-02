from django.shortcuts import render, get_object_or_404

from pais.models import Pais, Religiao, Idioma, Turismo, PaisIdioma, PaisReligiao


def index(request):
    lista_de_paises = Pais.objects.all().order_by('nome')
    return render(request, 'pais/index.html', {'paises': lista_de_paises})

def show(request, id):
    pais = get_object_or_404(Pais, id=id)
    religioes = PaisReligiao.objects.filter(pais_id=id)
    idiomas = PaisIdioma.objects.filter(pais_id=id)
    turismos = Turismo.objects.filter(pais_id=id)
    return render(request, 'pais/show.html', {'pais': pais, 'religioes': religioes, 'idiomas': idiomas, 'turismos': turismos})