from django.contrib import admin

from pais.models import Pais, Continente, Idioma, Religiao, Perseguicao, PaisReligiao, PaisIdioma, Turismo, Moeda

admin.site.register(Continente)
admin.site.register(Idioma)
admin.site.register(Religiao)
admin.site.register(Perseguicao)
admin.site.register(Pais)
admin.site.register(PaisReligiao)
admin.site.register(PaisIdioma)
admin.site.register(Turismo)
admin.site.register(Moeda)