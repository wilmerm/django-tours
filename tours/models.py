from django.db import models
from django.utils.translation import gettext as _, gettext_lazy as _l
from django.contrib.auth import get_user_model


User = get_user_model()


class Tour(models.Model):
    name = models.CharField(
        _l('name'),
        max_length=100,
        unique=True,
    )
    description = models.CharField(
        max_length=200,
        blank=True,
    )
    url_names = models.CharField(
        _l('view name'),
        max_length=500,
        blank=True,
        help_text=_l('Comma separated list of url_name where you want it to be '
            'displayed. If not specified, it will be displayed on all pages.')
    )
    show_only_staff = models.BooleanField(
        _l('show only staff users'),
        default=False,
    )
    show_only_superuser = models.BooleanField(
        _l('show only staff users'),
        default=False,
    )
    start_date = models.DateField(
        _l('start date'),
        null=True,
        blank=True,
    )
    end_date = models.DateField(
        _l('end date'),
        null=True,
        blank=True,
    )
    timeout = models.PositiveIntegerField(
        default=1000,
    )
    use_modal_overlay = models.BooleanField(
        default=True,
    )
    is_active = models.BooleanField(
        default=True,
    )
    users_shown = models.ManyToManyField(
        User,
        verbose_name=_l('users shown'),
        editable=False,
    )

    class Meta:
        verbose_name = _l('tour')
        verbose_name_plural = _l('tours')

    def __str__(self):
        return self.name


class TourStep(models.Model):
    POSITION_TOP = 'TOP'
    POSITION_BOTTOM = 'BOTTOM'
    POSITION_LEFT = 'LEFT'
    POSITION_RIGHT = 'RIGHT'
    POSITION_CHOICES = (
        (POSITION_TOP, _l('Top')),
        (POSITION_BOTTOM, _l('Bottom')),
        (POSITION_LEFT, _l('left')),
        (POSITION_RIGHT, _l('Right')),
    )

    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='steps',
        verbose_name=_l('tour'),
    )
    step_id = models.CharField(
        _l('step id'),
        max_length=50,
    )
    title = models.CharField(
        _l('title'),
        max_length=100,
    )
    text = models.TextField(
        _l('text'),
        blank=True,
    )
    attach_to_selector = models.CharField(
        _l('element selector'),
        max_length=200,
    )
    attach_to_position = models.CharField(
        _l('attach to position'),
        max_length=10,
        default=POSITION_BOTTOM,
        choices=POSITION_CHOICES,
    )

    class Meta:
        verbose_name = _l('tour step')
        verbose_name_plural = _l('tour steps')

    def __str__(self):
        return '%s %s' % (self._meta.verbose_name.capitalize(), self.step_id)


class TourPage(models.Model):
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='pages',
        verbose_name=_l('tour'),
    )
    view_name = models.CharField(
        _l('view name'),
        max_length=100,
        unique=True,
    )
    view_args = models.JSONField(
        _l('view arguments'),
        default=list,
        blank=True,
    )
    view_kwargs = models.JSONField(
        _l('view keywords arguments'),
        default=dict,
        blank=True,
    )

    class Meta:
        verbose_name = _l('tour page')
        verbose_name_plural = _l('tour pages')

    def __str__(self):
        return '%s %s' % (self._meta.verbose_name.capitalize(), self.view_name)