#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectFishingRod(AdventureGameObject):
    "Adventure Game Object"


    def getName(self):
        "Get the name of the object"

        return "FishingRod"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a fishing rod. It's brown and even has some lures!")


    def open(self, openedByRoom):
        "Try to open the object"

        if openedByRoom:
            return

        print("\nYou can't open the fishing rod")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        if kickedByRoom:
            return

        print("\nYou can't kick the fishing rod.")


    def move(self, movedByRoom):
        "Try to move the object"

        if movedByRoom:
            return

        print("\nYou can't move the fishing rod")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe fishing rod didn't respond... Not sure what you were expecting.")


    def use(self, usedByRoom):
        "Try to use the object"

        if usedByRoom:
            return

        print("\nThere is no where to fish...")


    def canPickup(self):
        "Check if the object is pickupable"

        return True
