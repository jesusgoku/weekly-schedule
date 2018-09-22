# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from working_day.apps.planner.models import WeeklySchedule, WorkingBlock


@admin.register(WeeklySchedule)
class WeeklyScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkingBlock)
class WorkingBlockAdmin(admin.ModelAdmin):
    pass
