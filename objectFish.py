#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectFish(AdventureGameObject):
    "Adventure Game Object"


    def getName(self):
        "Get the name of the object"

        return "Fish"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a fish. It's blue.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the fish")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        if kickedByRoom:
            return

        print("\n You can't do that right now.")


    def move(self, movedByRoom):
        "Try to move the object"

        if movedByRoom:
            return

        print("\nThere is no where to move the fish.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe fish didn't respond... Not sure what you were expecting.")


    def use(self, usedByRoom):
        "Try to use the object"

        if usedByRoom:
            return

        print("\n You can't use the fish right now.")


    def canPickup(self):
        "Check if the object is pickupable"

        return True
