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
    name            = models.CharField(max_length=50)
    current_pokemon = models.ForeignKey('Pokemon',null=True)

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

    def attack(self, pokemon, move):
        if move != self.move_1 and move != self.move_2:
            raise Exception("Illegal move")
        if pokemon.hp_left == 0:
            raise Exception("Cannot attack a fainted pokemon")

        damage = int( 0.2 * self.level * move.power )
        pokemon.hp_left = max(0, pokemon.hp_left - damage)

    def restore_hp(self, hp=1000):
        self.hp_left = max(self.max_hp, self.hp_left + hp)

    def is_fainted(self):
        return self.hp_left <= 0

    def __unicode__(self):
        return self.info.name;

class PokeBattle(models.Model):
    player1         = models.ForeignKey(PokeTrainer,related_name="player1")
    player2         = models.ForeignKey(PokeTrainer,related_name="player2")
    pokemon1        = models.ForeignKey(Pokemon,related_name="pokemon1")
    pokemon2        = models.ForeignKey(Pokemon,related_name="pokemon2")
    current_player  = models.ForeignKey(PokeTrainer,related_name="current_turn")
    history         = models.CharField(max_length=1000,blank=True)

    def move(self, move):
        if self.current_player == self.player1:
            attacking, defending = self.pokemon1, self.pokemon2
        else:
            attacking, defending = self.pokemon2, self.pokemon1

        attacking.attack(defending, move)

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1


    def __unicode__(self):
        return u'%s vs %s' % (self.player1.name, self.player2.name)

