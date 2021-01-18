from otree.api import Currency as c, currency_range
# from tester.generic_pages import oTreePage as Page
from ._builtin import  WaitPage, Page
from .models import Constants

import re
import csv
import random


class Endline(Page):
    form_model = 'player'
    form_fields = ['sex', 'birth',  'education', 'income', 'religion', 'religious_attendance', ]

page_sequence = [
        Endline,
]
