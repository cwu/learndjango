from django.shortcuts import render_to_response
from poketest.models import *
from poketest.forms import *

def fork_get_post(request, GET=None, POST=None):
    if request.method == 'GET' and GET is not None:
        return GET(request)
    elif request.method == 'POST' and POST is not None:
        return POST(request)
    raise Http404

def ajax_create_poke_info(request):
    name = request.POST['poke_name']
    return ''


def poke_battle(request):

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

def show_trainer(request, name):
    try:
        trainer = PokeTrainer.objects.get(name=name)
    except (PokeTrainer.DoesNotExist):
        return render_to_response('not_found_trainer.html')

    params = {
        'trainer': {
            'name': trainer.name,
            'owned_pokemon': trainer.pokemon_set.all(),
        },
    }

    return render_to_response('trainer.html', params)

def new_trainer(request):
    if request.method == 'POST':
        form = PokeTrainerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            poketrainer = PokeTrainer(name=data['name'])
            poketrainer.save()
            return HttpResponseRedirect('/poke/trainer?t=' + str(poketrainer.id))
    else:
        form = PokeTrainerForm()

    return  render_to_response('new_trainer.html', { 'form': form })

