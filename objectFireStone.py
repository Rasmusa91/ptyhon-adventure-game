#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectFireStone(AdventureGameObject):
    "Adventure Game Object"


    def getName(self):
        "Get the name of the object"

        return "FireStone"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see red gemstone with an inprint of a fire.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the fire stone.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou can't kick the fire stone.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't mvoe the fire stone.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe fire stone didn't respond... Not sure what you were expecting.")


    def use(self, usedByRoom):
        "Try to use the object"
        
        if usedByRoom:
            return


        print("\nYou're not really sure what the item is used for.")


    def canPickup(self):
        "Check if the object is pickupable"

        return True
