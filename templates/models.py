# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import pre_save
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

## Models

class List(models.Model):
	#uri = models.URLField()
	isPrivate = models.BooleanField(default = True)
	title = models.CharField(max_length = 50, default='Title')
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	creationDate = models.DateTimeField(default = timezone.now)
	lastModificationDate = models.DateTimeField(default = timezone.now) #parsing
	authorizedModerators = models.CharField(max_length = 2000, default=('\n')) #parsing
	score = models.IntegerField(default=0)
	description = models.CharField(max_length=500, blank=True)
	def __str__(self):
	    return self.title + " by " + str(self.creator)

class Item(models.Model):
	listeId = models.ForeignKey(List, on_delete = models.CASCADE)
	creatorId = models.ForeignKey(User)
	content = models.CharField(max_length = 200)
	creationDate = models.DateTimeField(default = timezone.now)
	lastModificationDate = models.DateTimeField(default = timezone.now)
	score = models.IntegerField(default=0)
	def __str__(self):
	    return self.content + " in " + self.listeId.uri + " by " + str(self.creatorId)

class Alerts(models.Model):
	listeId = models.ForeignKey(List, on_delete = models.CASCADE)
	user = models.ForeignKey(User)
	
## Signals reaction

def check(sender, **kwargs):
	#print(kwargs)
	#print(sender)

	if (sender==Item):
		instance = kwargs['instance']
		if(instance.pk is None):
			instance.score=0
			instance.creationDate = timezone.now()
		instance.lastModificationDate = timezone.now()
	elif (sender==List):
		instance = kwargs['instance']
		if(instance.pk is None):
			instance.score=0
			instance.creationDate = timezone.now()
		instance.lastModificationDate = timezone.now()
	#elif (sender==User):
		#print('This is a username :P')
	#else:
		#print('We don\'t care')

pre_save.connect(check, weak=False)
