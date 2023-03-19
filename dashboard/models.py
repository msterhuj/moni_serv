from django.db import models
from api.models import MoniMetric

class Page(models.Model):
    """
    class representing a page regrouping all metrics
    """
    title: models.CharField("title", max_length=255, unique=True, null=False)
    slug: models.SlugField(max_length=255, unique=True, null=False)
    default_root_page: models.BooleanField(default=False, null=False)
    description: models.TextField(null=False)
    created_at: models.DateTimeField(auto_now_add=True, null=False)
    updated_at: models.DateTimeField(auto_now=True, null=False)

class PageMetricGroup(models.Model):
    """
    class representing a group of metrics
    """
    page: models.ForeignKey(Page, on_delete=models.CASCADE, null=False)
    name: models.CharField(max_length=255, null=False)
    description: models.TextField(null=True)
    created_at: models.DateTimeField(auto_now_add=True, null=False)
    updated_at: models.DateTimeField(auto_now=True, null=False)
    metric = models.ManyToManyField(MoniMetric)


class PageIncident(models.Model):
    """
    class representing an incident
    """
    page_metric: models.ForeignKey(Page, on_delete=models.CASCADE, null=False)
    name: models.CharField(max_length=255, null=False)
    description: models.TextField(null=True)
    created_at: models.DateTimeField(auto_now_add=True, null=False)
    updated_at: models.DateTimeField(auto_now=True, null=False)
