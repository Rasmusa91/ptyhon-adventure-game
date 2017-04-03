#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectWaterGazer(AdventureGameObject):
    "Adventure Game Object"


    def getName(self):
        "Get the name of the object"

        return "WaterGazer"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a water gazer sprouting water all over the place.")
        print("Behind it, you can almost see an entrance to a cave.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open a water gazer...")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou kick the water, now you're wet...")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't move the water gazer.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe water gazer didn't respond... Not sure what you were expecting.")


    def use(self, usedByRoom):
        "Try to use the object"
        pass


    def canPickup(self):
        "Check if the object is pickupable"

        return False
