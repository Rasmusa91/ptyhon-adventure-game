#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object bandits
"""

from object import AdventureGameObject


class AdventureGameObjectBandits(AdventureGameObject):
    "Adventure Game Object Bandit"


    class State:
        "States of the bandits"
        hungry = 1
        cooperative = 2


    state = State.hungry


    def getName(self):
        "Get the name of the object"

        return "Bandits"


    def check(self):
        "Print an desc. of the object"

        print("\nThe pack of hungry bandits. \
They're are armed with simple weapons, however, you'd be no match for them.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou approach the bandits with some strange intention to \"open\" them.")
        print("They don't feel like putting up with you, so they throws you away.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou approach the bandits and kicks one of them.")
        print("The bandits laughs at your weakness, but the laugh fades quickly, \
they get angry again and throws you away.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou try to forcefully move the bandits, but they won't budge.")
        print("The bandits gets tired of you and throws you away.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe bandits ignores you and yells to you to get lost.")


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
