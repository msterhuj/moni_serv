from django.contrib import admin

from dashboard.models import Page, PageMetricGroup, PageIncident

admin.site.register(Page)
admin.site.register(PageMetricGroup)
admin.site.register(PageIncident)
