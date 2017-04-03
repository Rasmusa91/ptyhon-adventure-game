#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectAltar(AdventureGameObject):
    "Adventure Game Object"


    def getName(self):
        "Get the name of the object"

        return "Altar"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see an altar with 3 inscriptions on it.")
        print("The inscriptions is the icons of a water drop, a leaf and a fire.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the altar.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou can't kick the altar.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't move the altar.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nYou can't talk to the altar.")


    def use(self, usedByRoom):
        "Try to use the object"
        pass


    def canPickup(self):
        "Check if the object is pickupable"

        return False
