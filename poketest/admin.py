from django.contrib import admin
from poketest.models import *

class PokeInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    ordering = ('id',)

admin.site.register(PokeInfo, PokeInfoAdmin)
admin.site.register(Pokemon)
admin.site.register(PokeMove)
admin.site.register(PokeTrainer)
admin.site.register(PokeBattle)
