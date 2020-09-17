from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class instrucciones(Page):
    pass

class Prueba (Page):
    form_model = 'player'
    form_fields = ['urnaprueba', 'urnapago' ]


class ConsentimientoInformado(Page):
    form_model = 'player'
    form_fields = ['acepta']


class agradecimiento(Page):
    def is_displayed(self):
        return self.player.acepta =="no"



page_sequence = [ConsentimientoInformado, agradecimiento, instrucciones, Prueba]
