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
    trainer   = models.ForeignKey(PokeTrainer,blank=True,null=True)

    def attack(self, pokemon, move):
        if move != self.move_1 and move != self.move_2:
            raise Exception("Illegal move")
        if pokemon.hp_left == 0:
            raise Exception("Cannot attack a fainted pokemon")

        damage = int( 0.2 * self.level * move.power )
        pokemon.hp_left = max(0, pokemon.hp_left - damage)

        return damage

    def save(self):
        if self.move_1 == self.move_2:
            raise Exception, "Move 1 and 2 must be different"

        super(Pokemon, self).save()

    def restore_hp(self, hp=1000):
        self.hp_left = max(self.max_hp, self.hp_left + hp)

    def is_fainted(self):
        return self.hp_left <= 0

    def __unicode__(self):
        return self.info.name;

class PokeBattle(models.Model):
    player1         = models.ForeignKey(PokeTrainer,related_name="battles_1")
    player2         = models.ForeignKey(PokeTrainer,related_name="battles_2")
    current_player  = models.ForeignKey(PokeTrainer,related_name="current_turn")
    history         = models.CharField(max_length=1000,blank=True)

    def move(self, move):
        current_player = self.current_player
        if self.current_player == self.player1:
            attacking, defending = self.player1.current_pokemon, self.player2.current_pokemon
            other_player = self.player2
        else:
            attacking, defending = self.player2.current_pokemon, self.player1.current_pokemon
            other_player = self.player1

        damage = attacking.attack(defending, move)

        self.current_player = other_player

        commentary = "%s's %s attacked %s with %s doing %d damage\n" %(current_player.name, current_player.current_pokemon.info.name, other_player.current_pokemon.info.name, move.name, damage)

        
        self.history = (commentary + self.history)[:1000]

        return commentary

    def save(self):
        if self.player1 == self.player2:
            raise Exception, "Player 1 and 2 must be different"

        super(PokeBattle, self).save()


    def __unicode__(self):
        return u'%s vs %s' % (self.player1.name, self.player2.name)

