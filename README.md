# django-tours

Django app to display tours with [shepherdjs](https://shepherdjs.dev/)

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")

![django-tours-1](https://github.com/wilmerm/django-tours/assets/44853160/d7a8c20f-ddb1-4f93-b287-e143813aef95)

## Instalation

```bash
pip install django-tours
```

## Use

### Add to installed applications

```py
# settings.py

INSTALLED_APPS = [
    # ...
    'tours',
    # ...
]
```

### Optional configuration:

**If you want to set default variables, you can add the following in your settings.py file:**

```py
# settings.py

DEFAULT_SHEPHERD_JS = 'https://cdn.jsdelivr.net/npm/shepherd.js@latest/dist/js/shepherd.min.js'
DEFAULT_SHEPHERD_CSS = 'https://cdn.jsdelivr.net/npm/shepherd.js@latest/dist/css/shepherd.css'
```

### Add the URLs

```py
urlpatterns = [
    # ...
    path('tours/', include('tours.urls')),
    # ...
]
```

### Run the migrations

```py
python manage.py migrate
```

### Load tours into the template

```django
{% load tours %}

{% load_tours request %}
```

## Licence

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## Proyect Status

This project is under development

## Contribution 💗

If you find value in this project and would like to show your support, please consider making a donation via PayPal:

[Donate on PayPal](https://paypal.me/martinezwilmer?country.x=DO&locale.x=es_XC)

Your generosity helps us to continue improving and maintaining this project. We appreciate every contribution, however small. Thanks for being part of our community!
