#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectBoulder(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States of the bandits"
        originalSpot = 1
        finalSpot = 2


    state = State.originalSpot


    def getName(self):
        "Get the name of the object"

        return "Boulder"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a large gray boulder.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open a boulder...")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou kick the boulder, now your feet hurt. I'm not sure what you were expecting...")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou try to move the boulder, but it won't budge.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe boulder didn't respond... Not sure what you were expecting.")


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
