from django import forms
from django.apps import apps

from .models import Tour, TourStep


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = (
            'name',
            'description',
            'url_names',
            'show_only_staff',
            'show_only_superuser',
            'start_date',
            'end_date',
            'is_active',
        )
        widgets = {
            'description': forms.Textarea(),
            'url_names': forms.Textarea(),
        }


class TourStepForm(forms.ModelForm):
    class Meta:
        model = TourStep
        fields = (
            'tour',
            'step_id',
            'title',
            'text',
            'attach_to_selector',
            'attach_to_position',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if apps.is_installed('tinymce'):
            from tinymce.widgets import TinyMCE
            self.fields['text'].widget = TinyMCE()
