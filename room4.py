#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure room
"""


from room import AdventureGameRoom
from objectWaterGazer import AdventureGameObjectWaterGazer
from objectDragon import AdventureGameObjectDragon
from objectFieryBoulder import AdventureGameObjectFieryBoulder
from objectFireStone import AdventureGameObjectFireStone
from objectSign import AdventureGameObjectSign


class FourthAdventureGameRoom(AdventureGameRoom):
    "Adventure Game Room"


    def __init__(self, gameHandler):
        "Construct the room"

        AdventureGameRoom.__init__(self, gameHandler)

        self.objects = [
            AdventureGameObjectWaterGazer(),
            AdventureGameObjectFieryBoulder(),
            AdventureGameObjectSign()
        ]

        if self.gameHandler.debug:
            self.gameHandler.inventory.add(AdventureGameObjectFireStone())


    def printImage(self):
        "Prints an image of the room"

        print("------------------------------------------")
        print("|              o  o                      |")
        print("|            o      o                    -")
        print("|              o  o                     F ")
        print("|                X           S           -")
        print("|                    p                   |")
        print("-----------------|    |-------------------")
        print("- p: player")
        print("- o: volcano")
        print("- X: gazer")
        print("- F: fiery boulder")
        print("- S: sign")


    def printInfo(self):
        "Prints information about the room"

        print("\nYou find yourself at the bottom of a volcano.")
        if self.getObjectByName("WaterGazer"):
            print("There is water sprouting all over the place from a water gazer.")

        if self.getObjectByName("FieryBoulder"):
            print("You can see two paths, one path leads to the south and one path to the east, \
bit the path to the east is blocked by a fiery rock.")
        else:
            print("You see 2 paths, one to the south and one to the east.")


    def north(self):
        "Check if you can go north in the room"

        print("\nThere is no point of interest to the north.")
        return False


    def east(self):
        "Check if you can go east in the room"

        canPass = True

        if self.getObjectByName("FieryBoulder"):
            print("\nYou can't travel to the east as its path is blocked by a fiery boulder.")
            canPass = False

        if self.gameHandler.debug:
            canPass = True

        return canPass


    def south(self):
        "Check if you can go south in the room"

        return True


    def west(self):
        print("\nThere is no point of interest to the west.")
        return False


    def printSee(self):
        "Check if you can see anything spec. in the room"

        print("\nYou see a large volcano, you think you can see a cave entrance into the volcano, \
but the entrance is blocked by a huge water gazer.")
        print("To the east you can see a path, but it's blocked by a fiery boulder.")


    def printClue(self):
        "Print a clue to solve the room"

        if not self.getObjectByName("FieryBoulder"):
            print("\nYou can not proceed to the east.")
        elif self.getObjectByName("Dragon"):
            print("\nAnswer the the dragons riddle!")
        else:
            print("\nWhy don't you use your water stone?")


    def onObjectOpened(self, obj):
        "Callback when an object in the room has been opened"

        used = False
        return used


    def onObjectUsed(self, obj):
        "Callback when an object in the room has been used"

        used = False

        if obj.getName() == "WaterStone":
            if self.getObjectByName("WaterGazer") != None:
                self.removeObject("WaterGazer")
                self.addObject(AdventureGameObjectDragon())
                print("\nThe water stone absorbs all the water.")
                print("You can now clearly see an entrance into the volcano.")
                print("From the entrance, a huge majestic dragon approaches you.")
                print("The dragon just stands there, like it wants to talk to you.")
                used = True

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

        if obj.getName() == "Dragon" and phrase != None \
           and self.getObjectByName("Dragon").getState() == AdventureGameObjectDragon.State.riddleGiven:
            if obj.checkAnswer(phrase):
                self.gameHandler.inventory.add(AdventureGameObjectFireStone())
                self.removeObject("Dragon")
                self.removeObject("FieryBoulder")
                print("\nGood job! I will now destroy to the fiery rock over there, so \
you can proceed your journey.")
                print("I'll also grant you the fire stone.")
                print("Good bye my friend.")
                print("\nThe dragon returns into its cave.")
            else:
                print("\nSorry, wrong answer!")

            used = True

        return used
