import environ

from prenatal.settings.base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOST = env.list("ALLOWED_HOST")

DATABASES = {
    "default": env.db(),



}