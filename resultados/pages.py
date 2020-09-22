from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demografico(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'escala', 'loterias']

class Pagos (Page):
    pass

class Resultados(Page):
    pass

page_sequence = [Demografico, Resultados, Pagos ]
