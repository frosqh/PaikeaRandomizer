#!/usr/bin/env python3
# coding: utf-8
# author: Romain BRANDY

"""Fonctionnalités principales de PaikeaRandomizer.

Ce fichier contient les fonctions principales pour le programme d'aléa pour le
choix d'un jeu parmi une liste pré-remplie à la main dans models.py.
"""

import random
from randomizer.models import *


def getRequestedGames(speed, time, players):
    """Retourne une liste de jeu compatible avec les critères en entrée.

    speed : Vitesse du jeu ('Lent', 'Rapide')
    time : Durée d'une partie (entier en minute)
    players : Liste de noms de joueurs voulant jouer.
    """
    requested_games = Game.objects.all()

    if players is not None:
        for elm in players:
            games = GameByPlayer.objects.filter(player=Player.objects.get(
                name=elm)).select_related('game')
            requested_games = requested_games & games

    if speed is not None:
        requested_games.filter(speed=Speed.objects.get(name=speed))

    if time is not None:
        requested_games.filter(time=Time.objects.get(name=time))

    return requested_games


def randomize(list_games):
    """Retourne un élément aléatoire d'une liste en entrée."""
    return random.choice(list_games)
