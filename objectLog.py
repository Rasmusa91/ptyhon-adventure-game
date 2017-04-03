#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object log
"""

from object import AdventureGameObject


class AdventureGameObjectLog(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States of the bandits"
        originalSpot = 1
        underRock = 2
        finalSpot = 3


    state = State.originalSpot


    def getName(self):
        "Get the name of the object"

        return "Log"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a long, thick, steady log.")


    def open(self, openedByRoom):
        "Try to open the object"

        if openedByRoom:
            return

        print("\nYou can't open the log.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        if kickedByRoom:
            return

        if self.state != self.State.underRock:
            print("\nYou can't kick the log right now.")


    def move(self, movedByRoom):
        "Try to move the object"

        if movedByRoom:
            return

        if self.state != self.State.originalSpot:
            print("\nYou can't move the log right now.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe log didn't respond... Not sure what you were expecting.")


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
