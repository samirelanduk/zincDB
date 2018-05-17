import os
import binascii

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = binascii.hexlify(os.urandom(24)).decode()

VERSION = "0.4.0"

ALLOWED_HOSTS = []

DEBUG = True

ROOT_URLCONF = "core.urls"

INSTALLED_APPS = [
 "django.contrib.contenttypes",
 "django.contrib.staticfiles",
 "core",
 "zinc"
]

MIDDLEWARE = [
 "django.middleware.common.CommonMiddleware",
 "django.middleware.csrf.CsrfViewMiddleware",
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "../static"))

USE_TZ = False

TEMPLATES = [{
 "BACKEND": "django.template.backends.django.DjangoTemplates",
 "APP_DIRS": True,
}]

DATABASES = {"default": {
 "ENGINE": "django.db.backends.sqlite3",
 "NAME": os.path.join(BASE_DIR, "data", "zinc.sqlite3")
}}