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
    name_in_url = 'resultados'
    players_per_group = 8
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

    urna3 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )

    urna4 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )



    urna5 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )

    urna6 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )

    urna7 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )

    urna8 = models.StringField(
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
    urna11 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )
    urna12= models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )
    urna13 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )
    urna14 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )
    urna15 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )
    urna16 = models.StringField(
        choices=[['A', 'A'], ['B', 'B']],
        label='¿A qué urna pertenece la esfera?',
        widget=widgets.RadioSelect,
    )



class Player(BasePlayer):

    age = models.IntegerField(label='Edad:', min=18, max=90)

    random_id = models.IntegerField()

    gender = models.IntegerField(
        choices=[[0, 'Hombre'], [1, 'Mujer']],
        label='Género:',
        widget=widgets.RadioSelect,
    )
    escala = models.IntegerField(
        choices=[
            [0, 'Becado'],
            [2, 'Escala 1 (antigua)'],
            [4, 'Escala 2 (antigua)'],
            [6, 'Escala 3 (antigua)'],
            [9, 'Escala 4 (antigua)'],
            [13, 'Escala 5 (antigua)'],
            [1, 'Escala 1 (nueva)'],
            [3, 'Escala 2 (nueva)'],
            [5, 'Escala 3 (nueva)'],
            [7, 'Escala 4 (nueva)'],
            [8, 'Escala 5 (nueva)'],
            [10, 'Escala 6 (nueva)'],
            [11, 'Escala 7 (nueva)'],
            [12, 'Escala 8 (nueva)'],
            [14, 'Escala 9 (nueva)'],
        ],
        label='¿En qué escala de pago te encuentras?',
    )

    loterias = models.IntegerField(
        choices=[
            [0, 'Lotería 1'],
            [1, 'Lotería 2 '],
            [2, 'Lotería 3 '],
            [3, 'Lotería 4 '],
            [4, 'Lotería 5 '],
            [5, 'Lotería 6 '],

        ],
        label='¿Qué lotería prefiere?',
    )
