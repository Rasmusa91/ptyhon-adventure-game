#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectDoor(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States"
        closed = 1
        opened = 2


    state = State.opened


    def getName(self):
        "Get the name of the object"

        return "Door"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a large door with strange marks carved all over it.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nThe door won't budge.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou can't kick the door.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't move the door.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nYou can't talk to the door.")


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
