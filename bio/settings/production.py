from .base import *

from dotenv import dotenv_values

DEBUG = True
CSRF_TRUSTED_ORIGINS = ['https://zwack.rocks']
ALLOWED_HOSTS = ['zwack.rocks']

env = dotenv_values()

SECRET_KEY = env['SECRET_KEY']

try:
    from .local import *
except ImportError:
    pass
