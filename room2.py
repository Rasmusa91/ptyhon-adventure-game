#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure second room
"""


from room import AdventureGameRoom
from objectTroll import AdventureGameObjectTroll
from objectLog import AdventureGameObjectLog
from objectBoulder import AdventureGameObjectBoulder
from objectSign import AdventureGameObjectSign


class SecondAdventureGameRoom(AdventureGameRoom):
    "Adventure Game Room"


    def __init__(self, gameHandler):
        "Construct the room"

        AdventureGameRoom.__init__(self, gameHandler)

        self.objects = [
            AdventureGameObjectLog(),
            AdventureGameObjectTroll(),
            AdventureGameObjectBoulder(),
            AdventureGameObjectSign()
        ]


    def printImage(self):
        "Prints an image of the room"

        print("------------------------------------------")
        print("|  t   t      t     t     t      t       |")
        print("-         t      t           t           -")
        print("  troll                                  b")
        print("-            S                   l       -")
        print("|  t      t         p     t              |")
        print("------------------|   |-------------------")
        print("- p: player")
        print("- troll: troll")
        print("- l: log")
        print("- b: boulder")
        print("- t: tree")
        print("- S: sign")


    def printInfo(self):
        "Prints information about the room"

        print("\nYou find yourself in the middle of the forest.")
        print("You see 3 paths that you find interesting.")
        print("The south leads back to the bandits.")
        if self.getObjectByName("Troll"):
            print("The west is blocked by a ugly troll. You are no match to this troll in your current state.")
        else:
            print("The path to the west is now clear as you have slayed the troll.")

        if self.getObjectByName("boulder").getState() != AdventureGameObjectBoulder.State.finalSpot:
            print("The east is blocked by a big boulder, maybe you could find something to help you move it?")
        else:
            print("The path to the east is now clear as you have moved the boulder.")


    def north(self):
        "Check if you can go north in the room"

        print("\nThere is no point of interest to the north.")
        return False


    def east(self):
        "Check if you can go east in the room"

        canPass = self.getObjectByName("boulder").getState() == AdventureGameObjectBoulder.State.finalSpot

        if not canPass:
            print("\nThere is a large boulder blocking the path to the east.")

        #DEBUG
        if self.gameHandler.debug:
            canPass = True

        return canPass


    def south(self):
        "Check if you can go south in the room"

        return True


    def west(self):
        "Check if you can go west in the room"

        canPass = self.getObjectByName("Troll") == None

        if not canPass:
            print("\nA troll is blocking the path to the west.")

        #DEBUG
        if self.gameHandler.debug:
            canPass = True

        return canPass


    def printSee(self):
        "Check if you can see anything spec. in the room"

        print("\nAll you can see is trees, so many trees... There is 3 paths you can take. South, north and east.")
        print("The path to the south leads back to the bandits.")

        if self.getObjectByName("boulder").getState() != AdventureGameObjectBoulder.State.finalSpot:
            print("The path to the east is blocked by a huge boulder.")
            print("You do however see a long branch and wonder if this could be used in your advantage.")
        else:
            print("The path the east is clear.")

        if self.getObjectByName("Troll") != None:
            print("The path to the west is blocked by a troll.")
        else:
            print("The path to the west is now clear.")


    def printClue(self):
        "Print a clue to solve the room"

        if self.getObjectByName("Troll") != None:
            print("\nThe path is now clear, you can go to the west")
        elif self.gameHandler.inventory.getObjectByName("MagicSword") != None:
            print("\nThe magic sword could easily kill this troll.")
        elif self.getObjectByName("boulder").getState() != AdventureGameObjectBoulder.State.finalSpot:
            print("\nYou should travel east in order to find something to deal with this troll.")
        else:
            print("\nWhy don't you move the large branch underneath the boulder and kick it to move the rock?")


    def onObjectOpened(self, obj):
        "Callback when an object in the room has been opened"
        pass


    def onObjectUsed(self, obj):
        "Callback when an object in the room has been used"

        used = False

        if obj.getName() == "MagicSword":
            print("\nYou slayed the troll with your magical sword!")
            print("The path to the west is now clear.")
            self.removeObject("Troll")
            used = True

        return used


    def onObjectKicked(self, obj):
        "Callback when an object in the room has been kicked"
        used = False

        if obj.getName().lower() == "log" and obj.getState() == AdventureGameObjectLog.State.underRock:
            obj.setState(AdventureGameObjectLog.State.finalSpot)
            self.getObjectByName("boulder").setState(AdventureGameObjectBoulder.State.finalSpot)
            print("\nWith a bit of force you kicked the log, buding the boulder just enough for you to pass through.")
            used = True

        return used


    def onObjectMoved(self, obj):
        "Callback when an object in the room has been moved"

        used = False

        if obj.getName().lower() == "log" and obj.getState() == AdventureGameObjectLog.State.originalSpot:
            obj.setState(AdventureGameObjectLog.State.underRock)
            print("\nYou moved the log to underneath the boulder.")
            used = True

        return used


    def onObjectTalked(self, obj, phrase):
        "Callback when an object in the room has been kicked"
        pass
