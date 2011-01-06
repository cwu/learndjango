from django.db import models

class PokeInfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400,blank=True)
    
    def __unicode__(self):
        return self.name

    def sprite():
        return { 'row': (self.id-1) / 25, 'col': (self.id-1) % 25 }

class PokeMove(models.Model):
    name        = models.CharField(max_length=50)
    power       = models.IntegerField()
    accuracy    = models.IntegerField()

    def __unicode__(self):
        return self.name

class PokeTrainer(models.Model):
    name        = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Pokemon(models.Model):
    info = models.ForeignKey(PokeInfo)
    level     = models.IntegerField()
    max_hp    = models.IntegerField()
    hp_left   = models.IntegerField()
    move_1    = models.ForeignKey(PokeMove,related_name="pokemon1")
    move_2    = models.ForeignKey(PokeMove,related_name="pokemon2")
    trainer   = models.ForeignKey(PokeTrainer, null=True)

    def __unicode__(self):
        return self.info.name;

class PokeBattle(models.Model):
    player1         = models.ForeignKey(PokeTrainer,related_name="player1")
    player2         = models.ForeignKey(PokeTrainer,related_name="player2")
    pokemon1        = models.ForeignKey(Pokemon,related_name="pokemon1")
    pokemon2        = models.ForeignKey(Pokemon,related_name="pokemon2")
    current_player  = models.ForeignKey(PokeTrainer,related_name="current_turn")
    history         = models.CharField(max_length=1000,blank=True)

    def __unicode__(self):
        return u'%s vs %s' % (self.player1.name, self.player2.name)

