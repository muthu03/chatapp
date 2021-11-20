from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# this is topic model
# a topic can have multiple rooms whereas a room can have only one topic


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    # each team has more message so one to many
    # user is sending msg imported from django
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # whenever team is deleted the hole msg is deleted
    # one room many msges
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # this is for msg
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
