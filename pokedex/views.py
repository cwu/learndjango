from django.shortcuts import render_to_response
from poketest.models import *

def show(request):
    pokedex_entries = PokeInfo.objects.all()
    params = {
        'pokemon': pokedex_entries,
    }
    return render_to_response('index_pokedex.html', params)

def lookup(request, name):
    try:
        pokemon = PokeInfo.objects.get(name__iexact=name)
        try:
            prev = PokeInfo.objects.get(id=pokemon.id-1).name
        except (PokeInfo.DoesNotExist):
            prev = None

        try:
            next = PokeInfo.objects.get(id=pokemon.id+1).name
        except (PokeInfo.DoesNotExist):
            next = None

        params = { 
            'next' : next,
            'prev' : prev,
            'pokemon' : pokemon,
        }
    except (PokeInfo.DoesNotExist):
        return render_to_response('pokemon_not_found.html',  { 'name'  : name })
    
    return render_to_response('pokedex.html', params)
