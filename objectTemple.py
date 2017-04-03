#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectTemple(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States of the bandits"
        overgrown = 1
        closed = 2
        canEnter = 3


    state = State.overgrown


    def getName(self):
        "Get the name of the object"

        return "Temple"


    def check(self):
        "Print an desc. of the object"

        if self.state == self.State.overgrown:
            print("\nYou see a temple, it's overgrown by the nature.")
        elif self.state == self.State.closed:
            print("\nYou see a temple, its entrance is closed.")
        else:
            print("\nYou see a temple, it's clear to enter.")


    def open(self, openedByRoom):
        "Try to open the object"

        if openedByRoom:
            return

        if self.state == self.State.overgrown:
            print("\nThe roots is blocking the entrance, it can't be opened.")
        elif self.state == self.State.closed:
            print("\nYou opened the door to the temple.")
            self.state = self.State.canEnter
        elif self.state == self.State.canEnter:
            print("\nThe door to the temple is already opened.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou kick the boulder, now your feet hurt. I'm not sure what you were expecting...")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't move the temple.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nYou can't talk to the temple.")


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
