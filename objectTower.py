#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectTower(AdventureGameObject):
    "Adventure Game Object"


    def getName(self):
        "Get the name of the object"

        return "Tower"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a tall round tower, there is definetly something magical about it.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou try to find a door to the tower, but there is none. What..?")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou kick the tower, now your feet hurts.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou put all your force in pushing the tower, you're too weak. \
Or you know, it's building...")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe tower didn't respond.")


    def use(self, usedByRoom):
        "Try to use the object"
        pass


    def canPickup(self):
        "Check if the object is pickupable"

        return False
