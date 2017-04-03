#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectWaterElemental(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States of the"
        notTalkedTo = 1
        talkedTo = 2
        riddleGiven = 3


    state = State.notTalkedTo


    def getName(self):
        "Get the name of the object"

        return "WaterElemental"


    def check(self):
        "Print an desc. of the object"

        print("\nIt's nothing like you have ever experienced before...")
        print("In front of you, there is a magical creature, which mass seems to be made up by water.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the water elemental")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nThe water elemental is too far away.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nThe water elemental is too far away.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        if talkedByRoom:
            return

        if self.state == self.State.notTalkedTo:
            print("\nHello, my name is (something you couldn't understand).")
            print("I'm the guardian over the sea. As you have spared that innocent fish \
I'll let you answer a riddle. If your answer is correct, I'll greatly reward you!")
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

        print("What is blue and drowns you?")


    def checkAnswer(self, answer):
        "Check if answer is correct"

        return answer.lower() == "water"
