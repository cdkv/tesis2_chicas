from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demografico(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'escala', 'loterias']

    def is_displayed(self):
        return self.round_number == 4

class instrucciones2(Page):
    def is_displayed(self):
        return self.round_number == 3



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

class ejercicio3 (Page):
    form_model = 'group'
    form_fields = ['urna3']

    def before_next_page(self):
        if self.group.urna3 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 3 and self.round_number <= 2

class ejercicio4 (Page):
    form_model = 'group'
    form_fields = ['urna4']

    def before_next_page(self):
        if self.group.urna4 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 4 and self.round_number <= 2

class ejercicio5 (Page):
    form_model = 'group'
    form_fields = ['urna5']

    def before_next_page(self):
        if self.group.urna5 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 5 and self.round_number <= 2


class ejercicio6 (Page):
    form_model = 'group'
    form_fields = ['urna6']

    def before_next_page(self):
        if self.group.urna6 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 6 and self.round_number <= 2

class ejercicio7 (Page):
    form_model = 'group'
    form_fields = ['urna7']

    def before_next_page(self):
        if self.group.urna7 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 7 and self.round_number <= 2

class ejercicio8 (Page):
    form_model = 'group'
    form_fields = ['urna8']

    def before_next_page(self):
        if self.group.urna8 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 8 and self.round_number <= 2

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

class ejercicio11 (Page):
    form_model = 'group'
    form_fields = ['urna11']

    def before_next_page(self):
        if self.group.urna11 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 3 and self.round_number >= 3

class ejercicio12 (Page):
    form_model = 'group'
    form_fields = ['urna12']

    def before_next_page(self):
        if self.group.urna12 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 4 and self.round_number >= 3

class ejercicio13 (Page):
    form_model = 'group'
    form_fields = ['urna13']

    def before_next_page(self):
        if self.group.urna13 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 5 and self.round_number >= 3

class ejercicio14 (Page):
    form_model = 'group'
    form_fields = ['urna14']

    def before_next_page(self):
        if self.group.urna14 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 6 and self.round_number >= 3

class ejercicio15 (Page):
    form_model = 'group'
    form_fields = ['urna15']

    def before_next_page(self):
        if self.group.urna15 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 7 and self.round_number >= 3

class ejercicio16 (Page):
    form_model = 'group'
    form_fields = ['urna16']

    def before_next_page(self):
        if self.group.urna16 == self.group.myrandom:
            self.player.payoff = self.player.payoff + 5

    def is_displayed(self):
        return self.player.id_in_group == 8 and self.round_number >= 3

class Pagos (Page):
    def is_displayed(self):
        return self.round_number == 4




class Resultados(Page):
    def is_displayed(self):
        return self.round_number == 4

page_sequence = [ejercicio1, NormalWaitPage, ejercicio2, NormalWaitPage, ejercicio3, NormalWaitPage, ejercicio4, NormalWaitPage, ejercicio5, NormalWaitPage, ejercicio6, NormalWaitPage, ejercicio7, NormalWaitPage, ejercicio8, instrucciones2, ejercicio9, NormalWaitPage, ejercicio10, NormalWaitPage, ejercicio11, NormalWaitPage, ejercicio12, NormalWaitPage, ejercicio13, NormalWaitPage, ejercicio14, NormalWaitPage, ejercicio15, NormalWaitPage, ejercicio16, NormalWaitPage, Demografico, Resultados, Pagos ]
