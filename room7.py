#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure room
"""


from room import AdventureGameRoom
from objectAltar import AdventureGameObjectAltar
from objectDoor import AdventureGameObjectDoor

class SeventhAdventureGameRoom(AdventureGameRoom):
    "Adventure Game Room"


    def __init__(self, gameHandler):
        "Construct the room"

        AdventureGameRoom.__init__(self, gameHandler)

        self.objects = [
            AdventureGameObjectAltar(),
            AdventureGameObjectDoor()
        ]

    def printImage(self):
        "Prints an image of the room"

        print("------------------------------------------")
        print("|               ---D---                  |")
        print("|                 [a]                    |")
        print("|                                        |")
        print("|                     p                  |")
        print("|                                        |")
        print("------------------|    |------------------")
        print("- p: player")
        print("- D: big door")
        print("- a: altar")


    def printInfo(self):
        "Prints information about the room"

        print("\nYou find yourself in the temple.")
        print("Infront of you there is an altar with inscriptions on it.")
        print("Behind the altar there is a large door.")


    def north(self):
        "Check if you can go north in the room"

        canEnter = True

        if self.getObjectByName("door").getState() == AdventureGameObjectDoor.State.closed:
            print("\nThe door is locked.")
            canEnter = False



        return canEnter


    def east(self):
        "Check if you can go east in the room"

        print("\nThere is no point of interest to the east.")
        return False


    def south(self):
        "Check if you can go south in the room"

        return True


    def west(self):
        "Check if you can go west in the room"

        print("\nThere is no point of interest to the west.")
        return False


    def printSee(self):
        "Check if you can see anything spec. in the room"

        print("\nYou see an altar with inscriptions and a huge door.")


    def printClue(self):
        "Print a clue to solve the room"

        if self.getObjectByName("door").getState() != AdventureGameObjectDoor.State.open:
            print("\nDrop your stones.")
        else:
            print("\nYou can proceed to the north.")



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
        return used

    def addObject(self, obj):
        "Adds an object to the room"

        AdventureGameRoom.addObject(self, obj)

        canUnlock = True

        if not self.getObjectByName("FireStone"):
            canUnlock = False

        if not self.getObjectByName("WaterStone"):
            canUnlock = False

        if not self.getObjectByName("NatureStone"):
            canUnlock = False

        if canUnlock:
            print("\nYou have placed all the magical stones on the altar.")
            print("The altar absorbs the stones and the huge door unlocks.")
            self.getObjectByName("door").setState(AdventureGameObjectDoor.State.opened)
            self.removeObject("WaterStone")
            self.removeObject("FireStone")
            self.removeObject("NatureStone")
