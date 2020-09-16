from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demografico(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'escala', 'loterias']

class instrucciones2(Page):
    pass

class NormalWaitPage(WaitPage):
    pass

class ejercicio1 (Page):
    form_model = 'group'
    form_fields = ['urna1']

    def before_next_page(self):
        if self.group.urna1 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 1


class ejercicio2 (Page):
    form_model = 'group'
    form_fields = ['urna2']

    def before_next_page(self):
        if self.group.urna2 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 2

class ejercicio3 (Page):
    form_model = 'group'
    form_fields = ['urna3']

    def before_next_page(self):
        if self.group.urna3 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 3

class ejercicio4 (Page):
    form_model = 'group'
    form_fields = ['urna4']

    def before_next_page(self):
        if self.group.urna4 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 4

class ejercicio5 (Page):
    form_model = 'group'
    form_fields = ['urna5']

    def before_next_page(self):
        if self.group.urna5 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 1


class ejercicio6 (Page):
    form_model = 'group'
    form_fields = ['urna6']

    def before_next_page(self):
        if self.group.urna6 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 2

class ejercicio7 (Page):
    form_model = 'group'
    form_fields = ['urna7']

    def before_next_page(self):
        if self.group.urna7 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 3

class ejercicio8 (Page):
    form_model = 'group'
    form_fields = ['urna8']

    def before_next_page(self):
        if self.group.urna8 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 4

class Pagos (Page):
    pass







class Resultados(Page):
    pass

page_sequence = [ejercicio1, NormalWaitPage, ejercicio2, NormalWaitPage, ejercicio3, NormalWaitPage, ejercicio4, NormalWaitPage, instrucciones2, ejercicio5, NormalWaitPage, ejercicio6, NormalWaitPage, ejercicio7, NormalWaitPage, ejercicio8, NormalWaitPage, Demografico, Resultados, Pagos ]
