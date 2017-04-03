#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectWaterfall(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States of the"
        blocking = 1
        canPass = 2


    state = State.blocking


    def getName(self):
        "Get the name of the object"

        return "Waterfall"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a majestic waterfall.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the waterfall.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou go to the waterfall and splash your feet in it.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't move the waterfall.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe waterfall didn't respond... Not sure what you were expecting.")


    def use(self, usedByRoom):
        "Try to use the object"
        pass


    def canPickup(self):
        "Check if the object is pickupable"

        return False


    def getState(self):
        "Get the current state"

        return self.state


    def setState(self, state):
        "Set the current state"

        self.state = state
