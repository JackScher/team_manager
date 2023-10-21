from django.db import models


class Person(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"{self.email}"
