#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object rabbit
"""

from object import AdventureGameObject


class AdventureGameObjectRabbit(AdventureGameObject):
    "Adventure Game Object Rabbit"


    class State:
        "States of the rabbit"
        alive = 1
        dead = 2
        gutted = 3


    state = State.alive


    def getName(self):
        "Get the name of the object"

        return "Rabbit"


    def check(self):
        "Print an desc. of the object"

        if self.state == self.State.alive:
            print("\nYou see an alive, weak, little rabbit.")
            print("It would definitely make up a good meal!")
        elif self.state == self.State.dead:
            print("\nYou see a dead rabbit.")
            print("It's not realy edible yeat, though. You should gut it.")
        elif self.state == self.State.gutted:
            print("\nYou see a gutted rabbit. Maybe the bandits would like it.")


    def open(self, openedByRoom):
        "Try to open the object"

        if self.state == self.State.dead:
            self.state = self.State.gutted
            print("\nYou have gutted the rabbit!")
        else:
            print("\nYou can't open the rabbit.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        if self.state == self.State.alive:
            self.state = self.State.dead
            print("\nYou kicked the rabbit into a tree and it's now dead.")
        else:
            print("\nYou kicked the rabbit, it didn't really do any difference, though.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't move the rabbit.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nThe rabbit didn't respond... Not sure what you were expecting.")


    def use(self, usedByRoom):
        "Try to use the object"

        if usedByRoom:
            return

        if self.state == self.State.alive:
            self.state = self.State.dead
            print("\nYou snapped the rabbits neck.")
        elif self.state == self.State.dead:
            self.state = self.State.gutted
            print("\nYou gutted the rabbit.")
        elif self.state == self.State.gutted:
            print("\nThere is nothing left to do with the rabbit.")


    def canPickup(self):
        "Check if the object is pickupable"

        return True


    def getState(self):
        "Get the state of the rabbit"

        return self.state
