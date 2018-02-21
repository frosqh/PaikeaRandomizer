from django.db import models
from django.utils import timezone
from django.conf import settings


def user_directory_path(instance, filename):
    return settings.MEDIA_ROOT+'/'+instance.author.authorName+'/'+filename


class Player(models.Model):
    name = models.CharField(max_length=20, default='Roger')


class Speed(models.Model):
    name = models.CharField(max_length=20, default='Normal')


class Time(models.Model):
    name = models.IntegerField(default=0)


class Game(models.Model):
    name = models.CharField(max_length=50, default='Game')
    speed = models.ForeignKey(Speed, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=user_directory_path)


class GameByPlayer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
