from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)


class Message(models.Model):
    value = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True,
                                blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
