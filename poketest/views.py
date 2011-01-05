from django.shortcuts import render_to_response

def ajax_create_poke_info(request):
    name = request.POST['poke_name']

    if (

def pokedex_lookup(request):
    return render_to_response('pokedex.html', params)
