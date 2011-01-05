from django.db import models

class PokeInfo(models.Model):
    name = models.CharField(max_length=100)

class PokeSprite(models.Model):
    sprint_uri = models.CharField(max_length=200)
    sprite_row = models.IntegerField()
    sprite_col = models.IntegerField()
    poke_info  = models.ForeignKey(PokeInfo)

class PokeMoveInfo(models.Model):
    name        = models.CharField(max_length=50)
    power       = models.IntegerField()
    accuracy    = models.IntegerField()

class Pokemon(models.Model):
    poke_info = models.ForeignKey(PokeInfo)
    level     = models.IntegerField()
    max_hp    = models.IntegerField()

class PokeMove(models.Model):
    pokemon     = models.ForeignKey(Pokemon)
    poke_move   = models.ForeignKey(PokeMoveInfo)

