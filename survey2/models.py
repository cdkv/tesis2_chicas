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
    name_in_url = 'survey2'
    players_per_group = 2
    num_rounds = 4
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

    urna1 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )

    urna2 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )


    urna9 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )
    urna10= models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )


class Player(BasePlayer):


    random_id = models.IntegerField()



