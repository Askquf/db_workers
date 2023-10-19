from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=20, null=False)
    surname = models.CharField(max_length=20, null=False)

class Shift(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='shifts')
    date = models.DateTimeField(null=False)


