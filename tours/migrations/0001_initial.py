# Generated by Django 5.0.6 on 2024-06-18 14:54

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=200)),
                ('url_names', models.CharField(blank=True, help_text='Comma separated list of url_name where you want it to be displayed. If not specified, it will be displayed on all pages.', max_length=500, verbose_name='url names')),
                ('show_only_staff', models.BooleanField(default=False, verbose_name='show only staff users')),
                ('show_only_superuser', models.BooleanField(default=False, verbose_name='show only superusers')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('timeout', models.PositiveIntegerField(default=1000)),
                ('use_modal_overlay', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('users_shown', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='users shown')),
            ],
            options={
                'verbose_name': 'tour',
                'verbose_name_plural': 'tours',
            },
        ),
        migrations.CreateModel(
            name='TourStep',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('step_id', models.CharField(max_length=50, verbose_name='step id')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('text', models.TextField(blank=True, verbose_name='text')),
                ('attach_to_selector', models.CharField(max_length=200, verbose_name='element selector')),
                ('attach_to_position', models.CharField(choices=[('TOP', 'Top'), ('BOTTOM', 'Bottom'), ('LEFT', 'left'), ('RIGHT', 'Right')], default='BOTTOM', max_length=10, verbose_name='attach to position')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='tours.tour', verbose_name='tour')),
            ],
            options={
                'verbose_name': 'tour step',
                'verbose_name_plural': 'tour steps',
            },
        ),
    ]
