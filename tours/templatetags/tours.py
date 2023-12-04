from django import template
from django.conf import settings
from django.http.request import HttpRequest
from django.db.models import Q

from tours.models import Tour, TourStep, TourPage
from tours.settings import TOUR_SHEPHERD_CSS, TOUR_SHEPHERD_JS


register = template.Library()


@register.inclusion_tag('tours/tags/tour.html')
def load_tours(request: HttpRequest):
    resolver_match = getattr(request, 'resolver_match', None)

    if resolver_match is not None:
        url_name = resolver_match.url_name

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
            'shepherd_css': TOUR_SHEPHERD_CSS,
            'shepherd_js': TOUR_SHEPHERD_JS,
            'DEBUG': settings.DEBUG,
        }
