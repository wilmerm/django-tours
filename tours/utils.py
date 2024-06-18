from django.contrib.auth import get_user_model
from django.utils import timezone

from tours.models import Tour, TourStep


User = get_user_model()


def get_all_tour_for_user(user):
    """
    Gets all active and visible tours for a specific user.

    This feature filters tours that are currently active and whose start and end
    date include the current date and time. It also excludes tours that have
    already been shown to the user or those that are configured to be visible
    only to staff or super users if the user does not belong to these groups.

    Args:
        ``user`` (User): The user for which the tours will be obtained.
    """
    now = timezone.localtime()
    qs = Tour.objects.filter(
        is_active=True,
        start_date__lte=now,
        end_date__gte=now,
    ).exclude(
        users_shown=user,
    )

    if not user.is_staff:
        qs = qs.exclude(show_only_staff=True)
    if not user.is_superuser:
        qs = qs.exclude(show_only_superuser=True)

    return qs
