#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure room
"""


from random import randint
from room import AdventureGameRoom
from objectFish import AdventureGameObjectFish
from objectFishingRod import AdventureGameObjectFishingRod
from objectWaterElemental import AdventureGameObjectWaterElemental
from objectWaterfall import AdventureGameObjectWaterfall
from objectWaterStone import AdventureGameObjectWaterStone
from objectWhirl import AdventureGameObjectWhirl
from objectSign import AdventureGameObjectSign


class ThirdAdventureGameRoom(AdventureGameRoom):
    "Adventure Game Room"


    def __init__(self, gameHandler):
        "Construct the room"

        AdventureGameRoom.__init__(self, gameHandler)

        self.objects = [
            AdventureGameObjectFishingRod(),
            AdventureGameObjectWaterfall(),
            AdventureGameObjectWhirl(),
            AdventureGameObjectSign()
        ]

    def printImage(self):
        "Prints an image of the room"

        print("------------------------------------------")
        print("|                          WATERFALL w w |")
        print("-                           w   w     w  |")
        print("  p                           ==f= w     |")
        print("-               S               w   w O  |")
        print("|                            w       w   |")
        print("------------------------------------------")
        print("- p: player")
        print("- w: water")
        print("- =: wharf")
        print("- f: fishing rod")
        print("- waterfall: waterfall")
        print("- S: sign")

    def printInfo(self):
        "Prints information about the room"

        print("\nYou find yourself at a small pond, there is a small wharf at the said pond.")
        print("At the wharf you spot a fishing rod.")
        print("In the water you can also see a mysterious whirl.")
        print("To the north, there is an huge majestic waterfall.")

        if self.getObjectByName("Waterfall").getState() == AdventureGameObjectWaterfall.State.canPass:
            print("You can see 2 paths, one path leading to the west and one path leading through the waterfall.")
        else:
            print("You can only see one path leading out of here and that's to the west.")


    def north(self):
        "Check if you can go north in the room"

        canPass = True

        if self.getObjectByName("Waterfall").getState() != AdventureGameObjectWaterfall.State.canPass:
            print("There is a huge waterfall in the north, you can't possible pass through it.")
            canPass = False

        if self.gameHandler.debug:
            canPass = True

        return canPass


    def east(self):
        "Check if you can go east in the room"

        print("There is no point of interest to the east.")
        return False


    def south(self):
        "Check if you can go south in the room"

        print("There is no point of interest to the south.")
        return False


    def west(self):
        "Check if you can go west in the room"

        return True


    def printSee(self):
        "Check if you can see anything spec. in the room"

        print("\nYou can see a huge waterfall to the north and a path to the west.")
        print("There is a wharf near the pond with a fishing rod!")
        print("In the water you can see a large whirl.")


    def printClue(self):
        "Print a clue to solve the room"

        if self.getObjectByName("Waterfall").getState() == AdventureGameObjectWaterfall.State.canPass:
            print("\nEverything is complete! You can now travel north!")
        elif self.getObjectByName("WaterElemental") != None:
            print("\nAnswer the water elementals riddle.")
        elif self.getObjectByName("WaterElemental") != None:
            print("\nAnswer the water elementals riddle.")
        elif self.gameHandler.inventory.getObjectByName("FishingRod") != None:
            print("\nUse the fishing rod to do some fishing!")
        else:
            print("\nWhy don't you pick up the fishing rod and start fishing?")


    def onObjectOpened(self, obj):
        "Callback when an object in the room has been opened"

        used = False
        return used


    def onObjectUsed(self, obj):
        "Callback when an object in the room has been used"

        used = False

        if obj.getName() == "FishingRod":
            if self.gameHandler.inventory.getObjectByName("Fish") == None \
               and (randint(1, 100) < 30 or self.gameHandler.debug):
                self.gameHandler.inventory.add(AdventureGameObjectFish())
                print("\nYou caught a fish!")
            else:
                print("\nNo luck this time, try again!")

            used = True

        if obj.getName() == "Fish":
            if self.getObjectByName("Whirl") != None:
                self.gameHandler.destroyItem("Fish")
                self.removeObject("Whirl")
                self.addObject(AdventureGameObjectWaterElemental())
                print("\nYou threw the fish into the whirl. From the whirl, a Water Elemental ascends.")
                used = True

        return used


    def onObjectKicked(self, obj):
        "Callback when an object in the room has been kicked"

        used = False

        if obj.getName() == "Fish" and not obj.isPickedup():
            if self.getObjectByName("Whirl") != None:
                self.gameHandler.destroyItem("Fish")
                self.removeObject("Whirl")
                self.addObject(AdventureGameObjectWaterElemental())
                print("\nYou kicked the fish into the whirl. From the whirl, a Water Elemental ascends.")
                used = True

        return used


    def onObjectMoved(self, obj):
        "Callback when an object in the room has been moved"

        used = False

        if obj.getName() == "Fish" and not obj.isPickedup():
            if self.getObjectByName("Whirl") != None:
                self.gameHandler.destroyItem("Fish")
                self.removeObject("Whirl")
                self.addObject(AdventureGameObjectWaterElemental())
                print("\nYou moved the fish into the whirl. From the whirl, a Water Elemental ascends.")
                used = True

        return used


    def onObjectTalked(self, obj, phrase):
        "Callback when an object in the room has been kicked"

        used = False

        if obj.getName() == "WaterElemental" and phrase != None \
           and self.getObjectByName("WaterElemental").getState() == AdventureGameObjectWaterElemental.State.riddleGiven:
            if obj.checkAnswer(phrase):
                print("\nCorrect! I'll open up a path for you through the waterfall in the north.")
                print("I'll also give you this water stone, it contains great value.")
                print("Goodbye, my friend!")
                print("\nThe water elemental descens into the water.")
                self.getObjectByName("Waterfall").setState(AdventureGameObjectWaterfall.State.canPass)
                self.gameHandler.inventory.add(AdventureGameObjectWaterStone())
                self.removeObject("WaterElemental")
            else:
                print("\nSorry, wrong answer!")

            used = True

        return used
