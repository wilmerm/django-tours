
from django.shortcuts import render

from tours.forms import TourForm, TourStepForm


def index_view(request):
    context = {
        'tour_form': TourForm,
        'tourstep_form': TourStepForm,
    }
    return render(request, 'index.html', context)