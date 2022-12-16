from .base import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ["*"]
DATABASES = {
    "default": dj_database_url.parse("postgres://user:password@database:5432/database")
}
