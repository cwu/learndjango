from django.shortcuts import render_to_response
from learndjango.poketest.models import *

def ajax_create_poke_info(request):
    name = request.POST['poke_name']
    return ''

def pokedex_show(request):
    pokedex_entries = PokeInfo.objects.all()
    params = {
        'pokemon': pokedex_entries,
    }
    return render_to_response('index_pokedex.html', params)

def pokedex_lookup(request, name):
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
            'found' : True,
            'pokemon' : {
                'name' : pokemon.name,
                'next' : next,
                'prev' : prev,
                'description': pokemon.description,
                'sprite' : {
                    'row': pokemon.sprite.row,
                    'col':  pokemon.sprite.col,
                },
            },
        }
    except (PokeInfo.DoesNotExist):
        params = {
            'found' : False,
            'name'  : name,
        }
    
    return render_to_response('pokedex.html', params)
