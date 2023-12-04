from django import forms

from .models import Tour, TourStep, TourPage


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = (
            'name',
            'description',
            'show_only_staff',
            'show_only_superuser',
            'start_date',
            'end_date',
            'is_active',
        )


class TourStepForm(forms.ModelForm):
    class Meta:
        model = TourStep
        fields = (
            'step_id',
            'title',
            'text',
            'attach_to_selector',
            'attach_to_position',
        )

    def __init__(self, *args, **kwargs):
        tour = kwargs.pop('tour')
        super().__init__(*args, **kwargs)
        self.instance.tour = tour


class TourPageForm(forms.ModelForm):
    class Meta:
        model = TourPage
        fields = (
            'view_name',
            'view_args',
            'view_kwargs'
        )

    def __init__(self, *args, **kwargs):
        tour = kwargs.pop('tour')
        super().__init__(*args, **kwargs)
        self.instance.tour = tour