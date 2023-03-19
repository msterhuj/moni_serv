from django.contrib import admin

from .models import MoniAgent, MoniMetric

admin.site.register(MoniAgent)
admin.site.register(MoniMetric)