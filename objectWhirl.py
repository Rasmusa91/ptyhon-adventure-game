#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectWhirl(AdventureGameObject):
    "Adventure Game Object"


    def getName(self):
        "Get the name of the object"

        return "Whirl"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a large whirl in the pond.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the whirl.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou can't reach the whirl.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't move the whirl.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe whirl didn't respond... Not sure what you were expecting.")


    def use(self, usedByRoom):
        "Try to use the object"
        pass


    def canPickup(self):
        "Check if the object is pickupable"

        return False
