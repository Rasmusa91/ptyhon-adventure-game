#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectNatureStone(AdventureGameObject):
    "Adventure Game Object"


    def getName(self):
        "Get the name of the object"

        return "NatureStone"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see green gemstone with an inprint of a leaf.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the nature stone.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou can't kick the nature stone.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't mvoe the nature stone.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe nature stone didn't respond... Not sure what you were expecting.")


    def use(self, usedByRoom):
        "Try to use the object"
        
        if usedByRoom:
            return

        print("\nYou're not really sure what the item is used for.")


    def canPickup(self):
        "Check if the object is pickupable"

        return True
