from django.urls import path, include


urlpatterns = [
    path('tours/', include('tours.urls')),
]
