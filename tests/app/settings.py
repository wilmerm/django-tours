DEBUG = True
SECRET_KEY = "Thanks for using django-tours"
ALLOWED_HOSTS = ['*']

USE_TZ = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "db.sqlite3"
    }
}

INSTALLED_APPS = (
    # Default Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "tests",

    # 1. `python -m build`
    # 2. `pip uninstall django-tours`
    # 3. `pip install dist/django-tours-VERSION.tar.gz` or `pip install dist/*tar.gz`
    "tours",
)

ROOT_URLCONF = "tests.app.urls"

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # required for django.contrib.admin
    "django.contrib.messages.middleware.MessageMiddleware",  # required for django.contrib.admin
)

STATIC_URL = "/static/"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

TOURS_SHEPHERD_JS = 'https://cdn.jsdelivr.net/npm/shepherd.js@latest/dist/js/shepherd.min.js'
TOURS_SHEPHERD_CSS = 'https://cdn.jsdelivr.net/npm/shepherd.js@latest/dist/css/shepherd.css'