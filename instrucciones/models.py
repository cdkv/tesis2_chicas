from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random



class Constants(BaseConstants):
    name_in_url = 'instrucciones'
    players_per_group = None
    num_rounds = 1
    lista = ['A', 'B']


#class Subsession(BaseSubsession):

    #def creating_session(self):
        #if self.round_number == 1:
            #for p in self.get_players():
                #p.participant.vars['lista'] = random.choice(['A', 'B'])

class Subsession(BaseSubsession):
    def creating_session(self):
        for g in self.get_groups():
            g.myrandom = random.choice(Constants.lista)

        for p in self.get_players():
            p.random_id = random.randint(1, 27)


class Group(BaseGroup):
    myrandom = models.StringField()



class Player(BasePlayer):
    random_id = models.IntegerField()




    urnaprueba = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A que urna crees corresponde esta esfera?',
        widget=widgets.RadioSelect,
    )

    urnapago = models.IntegerField(min=5, max=5,    label='De haber acertado cuanto le correspondería',    )

    acepta = models.StringField(choices=['No', 'Sí'], widget=widgets.RadioSelectHorizontal,)
