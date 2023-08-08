from .base import *
import dj_database_url

DEBUG = False
SECRET_KEY = get_env_variable("SECRET_KEY")
ALLOWED_HOSTS = ["test.home.rileymathews.com"]
CSRF_COOKIE_DOMAIN="test.home.rileymathews.com"
CSRF_TRUSTED_ORIGINS=["test.home.rileymathews.com"]
DATABASES = {
    "default": dj_database_url.parse(get_env_variable("DATABASE_URL")),
}

try:
    from .local import *
except ImportError:
    pass
