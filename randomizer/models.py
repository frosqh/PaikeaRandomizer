from django.db import models
from django.utils import timezone
from django.conf import settings


def user_directory_path(instance, filename):
    return settings.MEDIA_ROOT+'/'+instance.author.authorName+'/'+filename


class Game(models.Model):
    name = models.CharField(max_length=50, default='Game')
    speed = models.ForeignKey(Speed, on_delete=models.CASCADE)
    length = models.ForeignKey(Length, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=user_directory_path)


class Player(models.Model):
    name = models.CharField(max_length=20, default='Roger')


class Speed(models.Model):
    name = models.CharField(max_length=20, default='Normal')


class Length(models.Model):
    name = models.IntegerField(default=0)


class GameByPlayer(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
