from django.contrib import admin

from .forms import TourForm, TourStepForm
from .models import Tour, TourStep


class TourAdmin(admin.ModelAdmin):
    form = TourForm
    fields = (
        'name',
        'description',
        'url_names',
        'show_only_staff',
        'show_only_superuser',
        'start_date',
        'end_date',
        'timeout',
        'use_modal_overlay',
        'is_active',
        'users_shown',
    )
    list_display = (
        'name',
        'show_only_staff',
        'show_only_superuser',
        'start_date',
        'end_date',
        'is_active',
    )
    list_filter = (
        'show_only_staff',
        'show_only_superuser',
        'start_date',
        'end_date',
        'is_active',
    )
    search_fields = (
        'name__icontains',
        'description__icontains',
    )


class TourStepAdmin(admin.ModelAdmin):
    form = TourStepForm
    list_display = (
        'title',
        'step_id',
        'tour',
    )
    list_filter = (
        'tour',
    )
    search_fields = (
        'title__icontains',
        'text__icontains',
        'step_id__iexact',
        'attach_to_selector__iexact',
    )


admin.site.register(Tour, TourAdmin)
admin.site.register(TourStep, TourStepAdmin)