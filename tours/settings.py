
from django.conf import settings
from django.core.exceptions import AppRegistryNotReady


DEFAULT_SHEPHERD_JS = 'https://cdn.jsdelivr.net/npm/shepherd.js@latest/dist/js/shepherd.min.js'
DEFAULT_SHEPHERD_CSS = 'https://cdn.jsdelivr.net/npm/shepherd.js@latest/dist/css/shepherd.css'

TOUR_SHEPHERD_JS = getattr(settings, 'TOUR_SHEPHERD_JS', DEFAULT_SHEPHERD_JS)
TOUR_SHEPHERD_CSS = getattr(settings, 'TOUR_SHEPHERD_CSS', DEFAULT_SHEPHERD_CSS)

