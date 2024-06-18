from django.urls import path

from .views import (
    complete_tour_view,
)

app_name = __package__

urlpatterns = [
    path('completetour/<int:pk>/', complete_tour_view, name='complete_tour'),
]
