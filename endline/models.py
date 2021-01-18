from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.utils.translation import gettext_lazy as _


class Constants(BaseConstants):
    name_in_url = 'endline'
    players_per_group = None
    num_rounds = 1
    EDUCATION_CHOICES = [
        [1, _('Primary or lower education')],
        [2, _('Secondary (lower or upper) education')],
        [3, _('A-levels or post-secondary non-tertiary education')],
        [4, _('Uncompleted tertiary education')],
        [5, _('Tertiary education (Bachelor, Master or Diploma degrees)')],
        [6, _('PhD or more than two diplomas or science degrees')],
    ]
    INCOME_CHOICES = [
        [1, _('Not enough money even for food')],
        [2, _('Enough for food, but not enough to buy clothes and shoes')],
        [3, _('Enough for clothes and shoes, but not enough for the purchase of small household appliances')],
        [4,
         _("Enough money for small purchases, but buying expensive things (a computer, "
           "washing machine, refrigerator) requires savings or credit."
           )],
        [5,
         _(
             "There is enough money to buy for a house, but to buy a car, a summer "
             "residence, an apartment you need to save or take a loan")],
        [6, _("We can afford any purchases without restrictions and loans")]
    ]
    RELIGION_CHOICES =[(1, _('Atheist')),
                        (2, _('Spiritual but not religious')),
                        (3, _('Orthodox Christian')),
                        (4, _('Catholic')),
                        (5, _('Muslim')),
                        (6, _('Buddhist')),
                        (7, _('Protestant')),
                        (8, _('Jewish')),
                        (9, _('Another religion not mentioned here'))]
    RELIGION_ATTENDANCE_CHOICES = [
        (1, _('At least once a week')),
        (2, _('Once or twice a month')),
        (3, _('A few times a year')),
        (4, _('Seldom / never')),
        (5, _('No answer, I am atheist'))
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sex = models.IntegerField(
        choices=[(0, _('Male')), (1, _('Female'))],
        verbose_name=_("Please indicate your gender"),
        widget=widgets.RadioSelect)

    birth = models.IntegerField(
        min=18,
        max=102,
        verbose_name=_("How old are you?")
    )

    education = models.IntegerField(
        verbose_name=_('What is the highest level of education that you have achieved?'),
        choices=Constants.EDUCATION_CHOICES,
        widget=widgets.RadioSelect)

    income = models.IntegerField(
        label=_("""Which statement most accurately describes your family’s financial situation?"""),
        choices=Constants.INCOME_CHOICES,
        widget=widgets.RadioSelect)

    religion = models.IntegerField(
        verbose_name=_("Which of these labels best matches your religious views?"),
        choices=Constants.RELIGION_CHOICES,
        widget=widgets.RadioSelect)

    religious_attendance = models.IntegerField(
        verbose_name=_("How frequently do you attend religious services?"),
        choices=Constants.RELIGION_ATTENDANCE_CHOICES,
        widget=widgets.RadioSelect)

    feedback = models.LongStringField(
        verbose_name=_("Do you have any feedback for us?  Did you enjoy the study?  Any complaints?"))
