from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=15)
    date_created = models.DateTimeField()


class StashHistory(models.Model):
    action = models.CharField(max_length=15)
    date_created = models.DateTimeField()
    details = models.TextField(max_length=500)


class Stash(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    description = models.TextField(max_length=1000)
    history = models.ForeignKey(
        StashHistory, null=True, on_delete=models.SET_NULL
    )

