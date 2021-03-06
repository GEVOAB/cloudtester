from os import environ

EXTENSION_APPS = ['cloudcapturer']
SESSION_CONFIGS = [
    dict(
        name='test',
        display_name="test",
        num_demo_participants=1,
        app_sequence=[
            'starter',
            'last'
        ],
        time_to_start='2021-01-20 15:34 MSK'
    ),
    dict(
        name='test2',
        display_name="test2",
        num_demo_participants=10,
        app_sequence=[
            'cloudcapturer'
        ]
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
TIME_ZONE = 'US/Eastern'
ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'eg7^n(irl1!k#wr-kef#)r90(9cc8ysq16xx8t3zbhz1@qw4(^'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
