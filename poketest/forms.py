from django import forms

class PokeTrainerForm(forms.Form):
    name = forms.CharField()

