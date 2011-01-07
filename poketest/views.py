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

