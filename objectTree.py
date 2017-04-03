#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectTree(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States of the"
        burning = 1
        notTalkedTo = 2
        talkedTo = 3
        riddleGiven = 4


    state = State.burning


    def getName(self):
        "Get the name of the object"

        return "Tree"


    def check(self):
        "Print an desc. of the object"

        if self.state == self.State.burning:
            print("\nThe tree is on fire! You think you can hear screams, but you're not sure... It's a tree...")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the tree")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou cant kick the tree.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't move the tree.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        if talkedByRoom:
            return

        if self.state == self.State.burning:
            print("\nYou can't talk to the burning tree.")
        elif self.state == self.State.notTalkedTo:
            print("\nHello there, I'm the guardian of nature, thank you for saving me from the fire.")
            print("I sure thought I was done for...")
            print("As a reward, I'll grant you a riddle, if you answer correctly, you'll be rewarded.")
            print("Talk to me again when you're ready for your riddle!")
            self.state = self.State.talkedTo
        elif self.state == self.State.talkedTo:
            print("\nAlright, here we go")
            self.printRiddle()
            self.state = self.State.riddleGiven
        else:
            print("\nAlright, here we go again")
            self.printRiddle()


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

    def printRiddle(self):
        "Print the riddle"

        print("What is green and on the ground? It tickles you if you're barefoot.")


    def checkAnswer(self, answer):
        "Check if answer is correct"

        return answer.lower() == "grass"
