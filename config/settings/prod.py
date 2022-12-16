from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ["rileymathews.fly.dev"]
DATABASES = {
    "default": dj_database_url.parse(get_env_variable("DATABASE_URL"))
}
SECRET_KEY = get_env_variable("SECRET_KEY")
CSRF_COOKIE_DOMAIN = "rileymathews.fly.dev"
CSRF_TRUSTED_ORIGINS = ["https://rileymathews.fly.dev"]
