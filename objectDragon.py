#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectDragon(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States of the"
        notTalkedTo = 1
        talkedTo = 2
        riddleGiven = 3


    state = State.notTalkedTo


    def getName(self):
        "Get the name of the object"

        return "Dragon"


    def check(self):
        "Print an desc. of the object"

        print("\nIs that... A dragon? You only thought those existed in the fairy tales...")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the dragon")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nThe dragon laughs at you and throws you away.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou push and drag the dragon, but it won't budge.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        if talkedByRoom:
            return

        if self.state == self.State.notTalkedTo:
            print("\nHello there, you looks a bit shocked, never seen a dragon before, huh?")
            print("I'm the guardian of fire. Thank you for saving me from that horrible \
water gaze. I hate water...")
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

        print("What is red and burns you?")


    def checkAnswer(self, answer):
        "Check if answer is correct"

        return answer.lower() == "fire"
