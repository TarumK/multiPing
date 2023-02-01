from django.db import models


from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()

    def __str__(self):

        return self.name
