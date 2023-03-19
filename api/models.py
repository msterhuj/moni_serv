from django.db import models

class MoniAgent(models.Model):
    """
    Class to represent a Agent who push metric in db
    """
    name: models.CharField(max_length=255, unique=True, null=False)
    token: models.CharField(max_length=255, unique=True, null=False)
    active: models.BooleanField(default=True, null=False)
    created_at: models.DateTimeField(auto_now_add=True, null=False)
    updated_at: models.DateTimeField(auto_now=True, null=False)

class MoniMetric(models.Model):
    """
    Class representing metric received from agent
    """
    agent: models.ForeignKey(MoniAgent, on_delete=models.CASCADE, null=False)
    test_type: models.CharField(max_length=255, null=False)
    value: models.FloatField(null=False)
    created_at: models.DateTimeField(auto_now_add=True)
