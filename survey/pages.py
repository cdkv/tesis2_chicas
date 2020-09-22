from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class Resultados(Page):
    def vars_for_template(self):
        return dict(player_in_all_rounds=self.player.in_all_rounds())

    def is_displayed(self):
        return self.round_number == 5




class NormalWaitPage(WaitPage):
    pass

class ejercicio1 (Page):
    form_model = 'group'
    form_fields = ['urna1']

    def before_next_page(self):
        self.player.urnausada = self.group.myrandom
        self.player.urnadecidida1 = self.group.urna1
        if self.player.rondaapagar == self.round_number:
            if self.group.urna1 == self.group.myrandom:
                self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.round_number <= 5


class ejercicio2 (Page):
    form_model = 'group'
    form_fields = ['urna2']

    def before_next_page(self):
        self.player.urnausada = self.group.myrandom
        self.player.urnadecidida1 = self.group.urna2
        if self.player.rondaapagar == self.round_number:
            if self.group.urna2 == self.group.myrandom:
                self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.round_number <= 5



class ejercicio3 (Page):
    form_model = 'group'
    form_fields = ['urna3']
    def before_next_page(self):
        self.player.urnausada = self.group.myrandom
        self.player.urnadecidida1 = self.group.urna3
        if self.player.rondaapagar == self.round_number:
            if self.group.urna3 == self.group.myrandom:
                self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 3 and self.round_number <= 5


class ejercicio4 (Page):
    form_model = 'group'
    form_fields = ['urna4']
    def before_next_page(self):
        self.player.urnausada = self.group.myrandom
        self.player.urnadecidida1 = self.group.urna4
        if self.player.rondaapagar == self.round_number:
            if self.group.urna4 == self.group.myrandom:
                self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 4 and self.round_number <= 5

class ejercicio5 (Page):
    form_model = 'group'
    form_fields = ['urna5']
    def before_next_page(self):
        self.player.urnausada = self.group.myrandom
        self.player.urnadecidida1 = self.group.urna5
        if self.player.rondaapagar == self.round_number:
            if self.group.urna5 == self.group.myrandom:
                self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 5 and self.round_number <= 5

class ejercicio6 (Page):
    form_model = 'group'
    form_fields = ['urna6']

    def before_next_page(self):
        self.player.urnausada = self.group.myrandom
        self.player.urnadecidida1 = self.group.urna6
        if self.player.rondaapagar == self.round_number:
            if self.group.urna6 == self.group.myrandom:
                self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 6 and self.round_number <= 5



page_sequence = [ejercicio1, NormalWaitPage, ejercicio2, NormalWaitPage, ejercicio3, NormalWaitPage, ejercicio4, NormalWaitPage, ejercicio5, NormalWaitPage, ejercicio6, NormalWaitPage]
