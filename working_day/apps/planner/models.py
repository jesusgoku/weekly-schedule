# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from django.utils.translation import gettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


class TimeStampable(models.Model):
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)

    class Meta(object):
        abstract = True


@python_2_unicode_compatible
class WeeklySchedule(TimeStampable):
    name = models.CharField(_('Name'), max_length=255)
    code = models.CharField(_('Code'), unique=True, max_length=50)

    def __str__(self):
        return '{} ({})'.format(self.name, self.code)

    class Meta(object):
        verbose_name = _('Weekly schedule')
        verbose_name_plural = _('Weekly schedules')


WEEKDAY_CHOICES = (
    (0, _('Sunday')),
    (1, _('Monday')),
    (2, _('Tuesday')),
    (3, _('Wednesday')),
    (4, _('Thursday')),
    (5, _('Friday')),
    (6, _('Saturday')),
)


@python_2_unicode_compatible
class WorkingBlock(models.Model):
    weekly_schedule = models.ForeignKey(WeeklySchedule, verbose_name=_('Weekly schedule'))
    weekday = models.IntegerField(_('Weekday'), choices=WEEKDAY_CHOICES)
    start_time = models.TimeField(_('Start time'))
    end_time = models.TimeField(_('End time'))

    def __str__(self):
        return '{}: {} {} - {}'.format(
            self.weekly_schedule,
            WEEKDAY_CHOICES[self.weekday][1],
            self.start_time,
            self.end_time,
        )

    class Meta(object):
        verbose_name = _('Working block')
        verbose_name_plural = _('Working blocks')
