from django.db import models

# Create your models here.
class Conquista(models.Model):
    titulo = models.CharField(max_length=100, db_index= True, unique=True)
    descricao = models.TextField(default='')
    documento = models.FileField(upload_to='documentos/conquistas/', blank=True)
    localidade = models.CharField(max_length=250, default='')
    link = models.CharField(max_length=150, blank=True)
    data = models.DateField(default='')

    class Meta:
        db_table = 'conquista'
        ordering = ('data',)

    def __str__(self):
        return self.titulo;

    def definir_mes(self):
        meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
        return meses[self.data.month-1];