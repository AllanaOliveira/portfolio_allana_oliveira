from django.db import models

class Continente(models.Model):
    nome = models.CharField(max_length=100, db_index=True, unique=True)

    class Meta:
        db_table = 'continente'
        ordering = ('nome',)

    def __str__(self):
        return self.nome;

class Idioma(models.Model):
    nome = models.CharField(max_length=100, db_index=True, unique=True)

    class Meta:
        db_table = 'idioma'
        ordering = ('nome',)

    def __str__(self):
        return self.nome;

class Religiao(models.Model):
    nome = models.CharField(max_length=100, db_index=True, unique=True)
    descricao = models.TextField(blank=True)

    class Meta:
        db_table = 'religiao'
        ordering = ('nome',)

    def __str__(self):
        return self.nome;

class Perseguicao(models.Model):
    tipo = models.TextField(blank=True)
    descricao = models.TextField(blank=True)

    class Meta:
        db_table = 'perseguicao'

    def __str__(self):
        return self.tipo;

class Moeda(models.Model):
    nome = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='images/moedas/', default='')

    class Meta:
        db_table = 'moeda'

    def __str__(self):
        return self.nome;

class Pais(models.Model):
    nome = models.CharField(max_length=100, db_index= True, unique=True)
    sigla = models.CharField(max_length=5, db_index= True, unique=True)
    imagem = models.ImageField(upload_to='images/pais/', default='')
    continente = models.ForeignKey(Continente, on_delete=models.DO_NOTHING)
    moeda = models.ForeignKey(Moeda, on_delete=models.DO_NOTHING, default=1)
    populacao = models.CharField(max_length=50, default='')
    capital = models.CharField(max_length=100, default='')
    capital_sigla = models.CharField(max_length=5, default='')
    clima = models.TextField(blank=True)
    cristaos = models.TextField(blank=True)
    perseguido = models.ForeignKey(Perseguicao, on_delete=models.DO_NOTHING)
    curiosidades = models.TextField(blank=True)
    historia = models.TextField(blank=True)
    atualizado_em = models.DateField(default='')

    class Meta:
        db_table = 'pais'
        ordering = ('nome',)

    def __str__(self):
        return self.nome + " ("+self.sigla+")";

class PaisReligiao(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING)
    religiao = models.ForeignKey(Religiao, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'pais_religiao'

class PaisIdioma(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING)
    idioma = models.ForeignKey(Idioma, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'pais_idioma'

class Turismo(models.Model):
    nome = models.TextField(blank=True)
    descricao = models.TextField(blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.DO_NOTHING)
    imagem = models.ImageField(upload_to='images/turismo/')

    class Meta:
        db_table = 'turismo'