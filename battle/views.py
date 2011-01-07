from django.shortcuts import render_to_response
from django.utils import simplejson
from django.http import HttpResponse
from poketest.models import *
from battle.forms import *

def ajaxResponse(params):
    return HttpResponse(simplejson.dumps(params), mimetype="application/javascript")

def ajaxError(msg):
    return HttpResponse(simplejson.dumps({ 'errors' : { 'msg' : msg }, 'success': False }),
                        mimetype="application/javascript",
                        status=400)

def ajaxSuccess(params=None):
    if params is None:
        params = {}
    return ajaxResponse(params.update( { 'success' : True } ))

def ajaxMissingParam(paramName):
    return ajaxError('missing parameter ' + paramName)


def new(request):
    if request.method == 'POST':
        pass
    else:
        pass

def ajax_move(request):
    # should pass in move info id to check for race conditions
    for value in [ 'battle_id', 'move' ]:
        if not value in request.POST:
            return ajaxMissingParam(value)
    
    battle_id = request.POST['battle_id']
    move_num = request.POST['move']

    try:
        battle = PokeBattle.objects.get(id=battle_id)
    except PokeBattle.DoesNotExist:
        return ajaxError("Battle does not exist")

    if move_num == '1':
        move = battle.current_player.current_pokemon.move_1
    elif move_num == '2':
        move = battle.current_player.current_pokemon.move_2
    else:
        return ajaxError("Invalid move")

    battle.move(move)

    battle.save()
    battle.pokemon1.save()
    battle.pokemon2.save()

    return ajaxSuccess( { 'data': { 'foo' : 'goo' } })


def battle(request, battle_id):

    battle = PokeBattle.objects.get(id=battle_id)

    params = {
        'battle': battle,
        'player': battle.player1,
        'opponent': battle.player2,
        'battle_history': 'Battle Started!'
    }
    return render_to_response('battle.html', params)

def s_battle(request):
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
