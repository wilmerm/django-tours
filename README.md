# django-tours

Django app to display tours with shepherdjs

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

This project is licensed under the MIT License.

## Proyect Status

This project is under development

## Contribution 💗

If you find value in this project and would like to show your support, please consider making a donation via PayPal:

[Donate on PayPal](https://paypal.me/martinezwilmer?country.x=DO&locale.x=es_XC)

Your generosity helps us to continue improving and maintaining this project. We appreciate every contribution, however small. Thanks for being part of our community!
