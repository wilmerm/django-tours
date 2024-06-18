from django.shortcuts import get_object_or_404, render
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Tour


@login_required
@require_POST
def complete_tour_view(request: HttpRequest, pk):
    tour = get_object_or_404(Tour, pk=pk)
    tour.users_shown.add(request.user)
    tour.save()
    return JsonResponse({'ok': True})
