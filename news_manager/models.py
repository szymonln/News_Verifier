from django.db import models

# Create your models here.


class NewsProvider(models.Model):
    name = models.CharField(max_length=100, default=None)
    base_url = models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.name) + ": " + str(self.base_url)

