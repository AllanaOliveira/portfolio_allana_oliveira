from django.db import models

# Create your models here.
from django.db import models

class Avatar(models.Model):
    imagem = models.CharField(max_length=60)

    class Meta:
        db_table = 'avatar'

    def __str__(self):
        return self.imagem;

class PalavraVida(models.Model):
    nome = models.CharField(max_length=150)
    avatar = models.ForeignKey(Avatar, on_delete=models.DO_NOTHING)
    motivacao = models.TextField()
    localidade = models.CharField(max_length=250, default='')

    class Meta:
        db_table = 'palavra_vida'

    def __str__(self):
        return self.nome;