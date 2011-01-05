from django.shortcuts import render_to_response
from learndjango.poketest.models import *

def ajax_create_poke_info(request):
    name = request.POST['poke_name']
    return ''

def pokedex_show(request):
    return render_to_response('pokedex_index.html')

def pokedex_lookup(request, name):
    pokemon = PokeInfo.objects.get(name__iexact=name)
    params = { 
        'pokemon' : {
            'name' : pokemon.name,
            'sprite' : {
                'uri':  pokemon.sprite.uri,
                'left': pokemon.sprite.col * 40 + 40,
                'top':  pokemon.sprite.row * 40,
            },
        },
    }
    return render_to_response('pokedex.html', params)
