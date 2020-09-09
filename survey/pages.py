from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demografico(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'escala', 'loterias']



class instrucciones(Page):
    pass

class instrucciones2(Page):
    pass

class Prueba (Page):
    form_model = 'player'
    form_fields = ['urnaprueba', 'urnapago' ]


class NormalWaitPage(WaitPage):
    pass

class ejercicio1 (Page):
    form_model = 'group'
    form_fields = ['urna1']

    def is_displayed(self):
        return self.player.id_in_group == 1


class ejercicio2 (Page):
    form_model = 'group'
    form_fields = ['urna2']

    def is_displayed(self):
        return self.player.id_in_group == 2

class ejercicio3 (Page):
    form_model = 'group'
    form_fields = ['urna3']

    def is_displayed(self):
        return self.player.id_in_group == 3

class ejercicio4 (Page):
    form_model = 'group'
    form_fields = ['urna4']

    def is_displayed(self):
        return self.player.id_in_group == 4

class ejercicio5 (Page):
    form_model = 'group'
    form_fields = ['urna5']

    def is_displayed(self):
        return self.player.id_in_group == 1


class ejercicio6 (Page):
    form_model = 'group'
    form_fields = ['urna6']

    def is_displayed(self):
        return self.player.id_in_group == 2

class ejercicio7 (Page):
    form_model = 'group'
    form_fields = ['urna7']

    def is_displayed(self):
        return self.player.id_in_group == 3

class ejercicio8 (Page):
    form_model = 'group'
    form_fields = ['urna8']

    def is_displayed(self):
        return self.player.id_in_group == 4

class Pagos (Page):
    pass


class ConsentimientoInformado(Page):
    form_model = 'player'
    form_fields = ['acepta']


class agradecimiento(Page):
    def is_displayed(self):
        return self.player.acepta =="no"


page_sequence = [ConsentimientoInformado, agradecimiento, instrucciones, Prueba, ejercicio1, NormalWaitPage, ejercicio2, NormalWaitPage, ejercicio3, NormalWaitPage, ejercicio4, NormalWaitPage, instrucciones2, ejercicio5, NormalWaitPage, ejercicio6, NormalWaitPage, ejercicio7, NormalWaitPage, ejercicio8, NormalWaitPage, Demografico, Pagos ]
