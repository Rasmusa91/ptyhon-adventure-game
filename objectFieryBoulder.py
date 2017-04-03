#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectFieryBoulder(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States of the bandits"
        originalSpot = 1
        finalSpot = 2


    state = State.originalSpot


    def getName(self):
        "Get the name of the object"

        return "FieryBoulder"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a large boulder on fire.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the fiery boulder...")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou kick the fiery boulder, now your feet are burning, good job.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou try to move the boulder, but it burns your hands.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe fiery boulder didn't respond... Not sure what you were expecting.")


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
