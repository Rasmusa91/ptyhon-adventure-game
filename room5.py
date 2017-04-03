#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure room
"""


from room import AdventureGameRoom
from objectMagicSword import AdventureGameObjectMagicSword
from objectWizard import AdventureGameObjectWizard
from objectTower import AdventureGameObjectTower
from tictactoe import TicTacToe


class FifthAdventureGameRoom(AdventureGameRoom):
    "Adventure Game Room"


    def __init__(self, gameHandler):
        "Construct the room"

        AdventureGameRoom.__init__(self, gameHandler)

        self.objects = [
            AdventureGameObjectWizard(),
            AdventureGameObjectTower()
        ]

        if self.gameHandler.debug:
            self.gameHandler.inventory.add(AdventureGameObjectMagicSword())


    def printImage(self):
        "Prints an image of the room"

        print("------------------------------------------")
        print("|                    w    w     w   w    |")
        print("-                      w   w  w o o o w  |")
        print("    p                    wizard o   o    |")
        print("-                      w     w  o o o w  |")
        print("|                   w  w   w    w  w     |")
        print("------------------------------------------")
        print("- p: player")
        print("- w: water")
        print("- wizard: wizard")
        print("- o: tower")


    def printInfo(self):
        "Prints information about the room"

        print("\nYou're at the edge of the lands, sorrounded by the water angry.")
        print("Infront of you, you see a huge tower.")
        print("At the bottom of the tower you can see some stairs.")

        if self.getObjectByName("Wizard") != None:
            print("On the bottom of the stairs, there sits a wizard.")


    def north(self):
        "Check if you can go north in the room"

        print("\nThere is no point of interest to the north.")
        return False


    def east(self):
        "Check if you can go east in the room"

        print("\nThere is no point of interest to the east.")
        return False


    def south(self):
        "Check if you can go south in the room"

        print("\nThere is no point of interest to the south.")
        return False


    def west(self):
        return True


    def printSee(self):
        "Check if you can see anything spec. in the room"

        if self.getObjectByName("Wizard") != None:
            print("\nYou see a huge tower and a wizard at the bottom of the tower stairs.")
        else:
            print("\nThere is just a huge tower here which you can't enter. I guess you'd have to go back.")


    def printClue(self):
        "Print a clue to solve the room"

        print("\nWin a game against the wizard!")


    def onObjectOpened(self, obj):
        "Callback when an object in the room has been opened"

        used = False
        return used


    def onObjectUsed(self, obj):
        "Callback when an object in the room has been used"

        used = False
        return used


    def onObjectKicked(self, obj):
        "Callback when an object in the room has been kicked"

        used = False
        return used


    def onObjectMoved(self, obj):
        "Callback when an object in the room has been moved"

        used = False
        return used


    def onObjectTalked(self, obj, phrase):
        "Callback when an object in the room has been kicked"

        used = False

        if obj != None and obj.getName() == "Wizard" and obj.getState() == AdventureGameObjectWizard.State.readyForGame:
            ttt = TicTacToe()
            winner = ttt.start()

            if winner == 1:
                print("\nCongratulations, you won!")
                print("Take this magic sword, it will pierce anything, even a troll!")
                print("Good bye now!")
                print("\nThe wizard teleports away.")
                self.gameHandler.inventory.add(AdventureGameObjectMagicSword())
                self.removeObject("Wizard")
            elif winner == 2:
                print("\nThe wizard wins")
                print("Just talk to me if you want to try again, I got all the time in the world.")
            else:
                print("\nIt's a tie!")
                print("Just talk to me if you want to try again, I got all the time in the world.")

            used = True

        return used
