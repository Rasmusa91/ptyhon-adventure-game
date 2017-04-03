#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectTroll(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States of the"
        alive = 1
        dead = 2


    state = State.alive


    def getName(self):
        "Get the name of the object"

        return "Troll"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a large fat troll.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open a troll")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou kick the troll. The troll kicks you back. You fly a few meters backwards.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nThe troll gets angry and throws you away.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe troll can't understand you. He growls back at you.")


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
