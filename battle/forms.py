from django import forms
from poketest.models import *

class PartialBattleForm(forms.ModelForm):
    class Meta:
        model = PokeBattle
        fields = ('player1', 'player2')
