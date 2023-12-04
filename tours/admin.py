from django.contrib import admin

from .models import Tour, TourStep, TourPage


class TourAdmin(admin.ModelAdmin):
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
    readonly_fields = (
        'users_shown',
    )
    search_fields = (
        'name__icontains',
        'description__icontains',
    )


class TourStepAdmin(admin.ModelAdmin):
    list_display = (
        'step_id',
        'tour',
        'title',
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


class TourPageAdmin(admin.ModelAdmin):
    list_display = (
        'view_name',
        'tour',
    )
    list_filter = (
        'view_name',
        'tour',
    )
    search_fields = (
        'view_name',
    )


admin.site.register(Tour, TourAdmin)
admin.site.register(TourStep, TourStepAdmin)
admin.site.register(TourPage, TourPageAdmin)