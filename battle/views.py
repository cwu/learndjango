from django.shortcuts import render_to_response
from poketest.models import *

def battle(request):
    params = {
        'player': {
            'name': 'YOU',
            'pokemon': {
                'name'   : 'Bulbasaur',
                'sprite' : {
                    'row': 0,
                    'col': 0,
                },
                'hp_left': 30,
                'max_hp' : 40,
            },
        },
        'opponent': {
            'name': 'CPU',
            'pokemon': {
                'name'   : 'Ivysaur',
                'sprite' : {
                    'row': 0,
                    'col': 1,
                },
                'hp_left': 20,
                'max_hp' : 40,
            },
        },
        'battle_history': 'Battle Started!'
    }
    return render_to_response('battle.html', params)
