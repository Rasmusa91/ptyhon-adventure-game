#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectMagicSword(AdventureGameObject):
    "Adventure Game Object"


    def getName(self):
        "Get the name of the object"

        return "MagicSword"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a magical sword. It sure could penetrate most creatures.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the sword.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou can't kick the sword.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't move the sword.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe sword respond... Not sure what you were expecting.")


    def use(self, usedByRoom):
        "Try to use the object"

        print("\nYou swing the sword fiercly in the air.")


    def canPickup(self):
        "Check if the object is pickupable"

        return True
