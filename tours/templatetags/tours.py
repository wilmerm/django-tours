from django import template
from django.conf import settings
from django.http.request import HttpRequest
from django.db.models import Q

from tours.models import Tour, TourStep
from tours.settings import TOURS_SHEPHERD_CSS, TOURS_SHEPHERD_JS


register = template.Library()


@register.inclusion_tag('tours/tags/tours.html')
def load_tours(request: HttpRequest):
    url_name = getattr(getattr(request, 'resolver_match', None), 'url_name', None)

    if url_name:
        # Filter active tours related to the current view
        tours = Tour.objects.filter(
            Q(url_names='') |
            Q(url_names__contains=url_name)
        ).exclude(
            is_active=False,
        )

        if getattr(request.user, 'is_authenticated', False):
            tours = tours.exclude(users_shown=request.user)

        if not getattr(request.user, 'is_superuser', False):
            tours = tours.exclude(show_only_superuser=True)

        if not getattr(request.user, 'is_staff', False):
            tours = tours.exclude(show_only_staff=True)

        return {
            'request': request,
            'tours': tours,
            'shepherd_css': TOURS_SHEPHERD_CSS,
            'shepherd_js': TOURS_SHEPHERD_JS,
            'DEBUG': settings.DEBUG,
        }
