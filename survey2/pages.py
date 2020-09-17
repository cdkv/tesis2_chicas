from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class instrucciones2(Page):
    def is_displayed(self):
        return self.round_number == 3

class Resultados(Page):
    def is_displayed(self):
        return self.round_number == 2

class NormalWaitPage(WaitPage):
    pass

class ejercicio1 (Page):
    form_model = 'group'
    form_fields = ['urna1']

    def before_next_page(self):
        if self.group.urna1 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number <= 2


class ejercicio2 (Page):
    form_model = 'group'
    form_fields = ['urna2']

    def before_next_page(self):
        if self.group.urna2 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number <= 2

class ejercicio9 (Page):
    form_model = 'group'
    form_fields = ['urna9']

    def before_next_page(self):
        if self.group.urna9 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number >= 3

class ejercicio10 (Page):
    form_model = 'group'
    form_fields = ['urna10']

    def before_next_page(self):
        if self.group.urna10 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number >= 3




page_sequence = [ejercicio1, NormalWaitPage, ejercicio2, NormalWaitPage, Resultados, instrucciones2, ejercicio9, NormalWaitPage, ejercicio10, NormalWaitPage ]
