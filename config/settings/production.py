from .base import *
import dj_database_url

DEBUG = False
SECRET_KEY = get_env_variable("SECRET_KEY")
ALLOWED_HOSTS = ["rileymathews.com"]
CSRF_COOKIE_DOMAIN = "rileymathews.com"
CSRF_TRUSTED_ORIGINS = ["https://rileymathews.com"]
DATABASES = {
    "default": dj_database_url.parse(get_env_variable("DATABASE_URL")),
}

try:
    from .local import *
except ImportError:
    pass
