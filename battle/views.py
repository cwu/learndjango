from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.http import *
from poketest.models import *
from battle.forms import *

def ajaxResponse(params,status=200):
    return HttpResponse(simplejson.dumps(params), mimetype="application/javascript",status=status)

def ajaxError(msg):
    return HttpResponse(simplejson.dumps({ 'errors' : { 'msg' : msg }, 'success': False }),
                        mimetype="application/javascript",
                        status=400)

def ajaxSuccess(params=None):
    if params is None:
        params = {}
    params.update( { 'success' : True } )
    return ajaxResponse(params)

def ajaxMissingParam(paramName):
    return ajaxError('missing parameter ' + paramName)


@login_required
def new(request):
    if request.method == 'POST':
        form = PartialBattleForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            battle = PokeBattle(player1=data['player1'],
                                player2=data['player2'],
                                current_player=data['player1'],
                                history = "Battle Started!!1")
            battle.save()
            return HttpResponseRedirect(reverse('learndjango.battle.views.battle', kwargs={'battle_id': battle.id}))
    else:
        form = PartialBattleForm()
    return render_to_response("new_battle.html", { 'form' : form })

@login_required
def ajax_move(request):
    # should pass in move info id to check for race conditions
    for value in [ 'battle_id', 'move' ]:
        if value not in request.POST:
            return ajaxMissingParam(value)
    
    battle_id = request.POST['battle_id']
    move_num = request.POST['move']

    try:
        battle = PokeBattle.objects.get(id=battle_id)
    except PokeBattle.DoesNotExist:
        return ajaxError("Battle does not exist")

    current_player = battle.current_player
    next_player = battle.player2 if current_player == battle.player1 else battle.player1
    if move_num == '1':
        move = battle.current_player.current_pokemon.move_1
    elif move_num == '2':
        move = battle.current_player.current_pokemon.move_2
    else:
        return ajaxError("Invalid move")

    try:
        commentary = battle.move(move)
    except Exception, e:
        return ajaxError(e.message)

    battle.save()
    battle.player1.current_pokemon.save()
    battle.player2.current_pokemon.save()

    response = {
        'data' : {
            'poke1': {
                'name' : battle.player1.current_pokemon.info.name,
                'hp_left': battle.player1.current_pokemon.hp_left,
                'max_hp' : battle.player1.current_pokemon.max_hp,
            },
            'poke2': {
                'name' : battle.player2.current_pokemon.info.name,
                'hp_left': battle.player2.current_pokemon.hp_left,
                'max_hp' : battle.player2.current_pokemon.max_hp,
            },
            'current_player' : next_player.name,
            'move1' : battle.current_player.current_pokemon.move_1.name,
            'move2' : battle.current_player.current_pokemon.move_2.name,
            'battle_lines' :  commentary,
        },
    }

    return ajaxSuccess(response)


@login_required
def battle(request, battle_id):

    battle = PokeBattle.objects.get(id=battle_id)

    params = {
        'battle': battle,
        'player': battle.player1,
        'opponent': battle.player2,
    }
    return render_to_response('battle.html', params)
