from django.db import models
from django.urls import reverse


class RdbmsManager(models.Model):
    name = models.CharField(max_length=200)
    host = models.TextField()
    username = models.TextField()
    password = models.TextField()
    type = models.TextField()
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('rdbms-manager-list')
