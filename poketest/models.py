from django.db import models

class PokeSprite(models.Model):
    uri = models.CharField(max_length=200)
    row = models.IntegerField()
    col = models.IntegerField()

class PokeInfo(models.Model):
    name = models.CharField(max_length=100)
    sprite = models.ForeignKey(PokeSprite)

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

