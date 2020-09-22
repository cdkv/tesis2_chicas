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
    name_in_url = 'survey'
    players_per_group = 6
    num_rounds = 5
    lista = ['A', 'B']


#class Subsession(BaseSubsession):

    #def creating_session(self):
        #if self.round_number == 1:
            #for p in self.get_players():
                #p.participant.vars['lista'] = random.choice(['A', 'B'])

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()

        for g in self.get_groups():
            g.myrandom = random.choice(Constants.lista)

        for p in self.get_players():
            p.random_id = random.randint(1, 27)
            if self.round_number == 1:
                p.rondaapagar = random.randint(1, Constants.num_rounds)
            else:
                p.rondaapagar = p.in_round(1).rondaapagar


class Group(BaseGroup):
    myrandom = models.StringField()

    urna1 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna crees que pertenece la esfera?',
        widget=widgets.RadioSelect,
    )

    urna2 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna crees que pertenece la esfera?',
        widget=widgets.RadioSelect,
    )

    urna3 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna crees que pertenece la esfera?',
        widget=widgets.RadioSelect,
    )

    urna4 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿AA qué urna crees que pertenece la esfera?',
        widget=widgets.RadioSelect,
    )



    urna5 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna crees que pertenece la esfera?',
        widget=widgets.RadioSelect,
    )

    urna6 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna crees que pertenece la esfera?',
        widget=widgets.RadioSelect,
    )


class Player(BasePlayer):

    random_id = models.IntegerField()

    urnadecidida1 = models.StringField()

    urnausada = models.StringField()

    rondaapagar = models.IntegerField()









