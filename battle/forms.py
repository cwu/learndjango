from django import forms
from poketest.models import *

class PartialBattleForm(forms.Form):
    player1 = forms.ModelChoiceField(queryset=PokeTrainer.objects)
    player2 = forms.ModelChoiceField(queryset=PokeTrainer.objects)

    def clean_player1(self):
        player1 = self.cleaned_data['player1']
        if player1.battles_1.all() or player1.battles_2.all():
            raise forms.ValidationError("%s cannot be in more than one battle" % (player1.name))

        return player1

    def clean_player2(self):
        player1 = PokeTrainer.objects.get(id=self.data['player1'])
        player2 = self.cleaned_data['player2']

        if player1 == player2:
            raise forms.ValidationError("Player cannot battle themselves")
        elif player2.battles_1.all() or player2.battles_2.all():
            raise forms.ValidationError("%s cannot be in more than one battle" % (player2.name))

        return player2



