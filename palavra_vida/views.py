from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from palavra_vida.forms import PalavraVidaForm
from palavra_vida.models import PalavraVida, Avatar

def index(request):
    palavras_vida = PalavraVida.objects.all()
    return render(request, 'palavra_vida/index.html', { 'palavras_vida': palavras_vida })

def cadastra_motivacao(request):
    avatares = Avatar.objects.all().order_by('id')
    if request.POST:
        motivacao_form = PalavraVidaForm(request.POST)

        if motivacao_form.is_valid():
            motivacao = motivacao_form.save(commit=False)
            motivacao.save()
            messages.add_message(request, messages.INFO, 'Palavra de Vida cadastrada com sucesso!')
            return render(request, 'palavra_vida/cadastra_motivacao.html', {'form': motivacao_form, 'avatares': avatares})
    else:
        motivacao_form = PalavraVidaForm()

    return render(request, 'palavra_vida/cadastra_motivacao.html', {'form': motivacao_form, 'avatares': avatares})