from .base import *
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-gpe5hjugr*8n_26^oshs%z)ze3wj-rzm(-isv%n@&c6lu2s#vh"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DATABASES = {
    "default": dj_database_url.parse("postgres://user:password@database:5432/database"),
}

INSTALLED_APPS += ["livereload"]
MIDDLEWARE += ["livereload.middleware.LiveReloadScript"]


try:
    from .local import *
except ImportError:
    pass
