from django.db import models


from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()

    def __str__(self):

        return self.name

class Log(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=30)
    packet_count = models.IntegerField()
    average_time = models.FloatField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.host

