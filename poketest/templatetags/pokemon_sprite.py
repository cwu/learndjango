from django import template
from learndjango.poketest.models import (PokeInfo,Pokemon)

register = template.Library()

@register.filter(name='sprite')
def sprite(pokemon):
    if pokemon.__class__ == PokeInfo:
        id_zero = pokemon.id - 1
    elif pokemon.__class__ == Pokemon:
        id_zero = pokemon.info_id - 1
    elif pokemon.__class__ == dict:
        id_zero = pokemon['sprite']['row'] * 25 + pokemon['sprite']['col']
    else:
        raise TypeError("Unknown Class called into filter sprite: " + pokemon.__class__.__name__)
    return str(id_zero / 25) + "_" + str(id_zero % 25)
