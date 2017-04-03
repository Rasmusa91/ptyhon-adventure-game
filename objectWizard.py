#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""

from object import AdventureGameObject


class AdventureGameObjectWizard(AdventureGameObject):
    "Adventure Game Object"


    class State:
        "States of the"
        notTalkedTo = 1
        readyForGame = 2


    state = State.notTalkedTo


    def getName(self):
        "Get the name of the object"

        return "Wizard"


    def check(self):
        "Print an desc. of the object"

        print("\nIt's a wizard... For some reason he looks like you always thought \
a wizard would look like. Blue robe with stars imprints, pointy hat that matches the robe. \
He also has small glasses and a wand with a star upon it.")


    def open(self, openedByRoom):
        "Try to open the object"

        print("\nYou can't open the wizard.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nThe wizard cries a bit, but recovers quickly.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou push the wizard to the ground. He quickly gets up with a grunt.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        if talkedByRoom:
            return

        if self.state == self.State.notTalkedTo:
            print("\nHello there strange fella'. Do you fancy a game of TicTacToe?")
            print("I'm still unbeaten, so if you beat me, I'll make it worth your while.")
            print("Talk to me again when you're ready for the game!")
            self.state = self.State.readyForGame


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
