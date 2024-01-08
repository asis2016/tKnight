from django.db import models
from django.urls import reverse


class VaultManager(models.Model):
    name = models.CharField(max_length=200)
    username = models.TextField()
    password = models.TextField()
    url = models.TextField()
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('vault-manager-list')
