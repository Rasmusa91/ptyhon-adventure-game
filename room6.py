#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure room
"""


from room import AdventureGameRoom
from objectTree import AdventureGameObjectTree
from objectTemple import AdventureGameObjectTemple
from objectNatureStone import AdventureGameObjectNatureStone


class SixthAdventureGameRoom(AdventureGameRoom):
    "Adventure Game Room"


    def __init__(self, gameHandler):
        "Construct the room"

        AdventureGameRoom.__init__(self, gameHandler)

        self.objects = [
            AdventureGameObjectTree(),
            AdventureGameObjectTemple()
        ]

        if self.gameHandler.debug:
            self.gameHandler.inventory.add(AdventureGameObjectNatureStone())


    def printImage(self):
        "Prints an image of the room"

        print("------------------------------------------")
        print("|               | t |                    |")
        print("|               |---|                    -")
        print("|                                 p       ")
        print("|        BT                              -")
        print("|                                        |")
        print("------------------------------------------")
        print("- p: player")
        print("- BT: big tree")
        print("- t: temple")


    def printInfo(self):
        "Prints information about the room"

        print("\nYou find yourself in a glade.")

        if self.getObjectByName("tree"):
            if self.getObjectByName("tree").getState() == AdventureGameObjectTree.State.burning:
                print("In the middle of the glade you see a huge burning tree.")
                print("You can almost hear the tree screaming.")
            else:
                print("In the middle of the glade you see a huge tree, which seems to be alive.")

        if self.getObjectByName("temple").getState() == AdventureGameObjectTemple.State.overgrown:
            print("To the north you can see a temple, but its entrance is block by overgrowth.")
        else:
            print("To the north you can see a temple.")


    def north(self):
        "Check if you can go north in the room"

        canEnter = True

        if self.getObjectByName("temple").getState() == AdventureGameObjectTemple.State.overgrown:
            print("\nThe temple to the north is blocked by overgrowth.")
            canEnter = False

        elif self.getObjectByName("temple").getState() == AdventureGameObjectTemple.State.closed:
            print("\nThe door to the temple in the north is closed.")
            canEnter = False

        if self.gameHandler.debug:
            canEnter = True

        return canEnter


    def east(self):
        "Check if you can go east in the room"

        return True


    def south(self):
        "Check if you can go south in the room"

        print("\nThere is no point of interest to the south.")
        return False


    def west(self):
        "Check if you can go west in the room"

        print("\nThere is no point of interest to the west.")
        return False


    def printSee(self):
        "Check if you can see anything spec. in the room"

        print("\nYou see a huge burning tree and an overgrown temple.")


    def printClue(self):
        "Print a clue to solve the room"

        if self.getObjectByName("tree").getState() == AdventureGameObjectTree.State.burning:
            print("\nUse your water stone or fire stone to put out the fire.")
        elif self.getObjectByName("tree").getState() != None:
            print("\nSolve the riddle from the tree.")
        elif self.getObjectByName("temple").getState() == AdventureGameObjectTemple.State.overgrown:
            print("\nUse the nature stone or the fire stone to clear the temples overgrowth.")
        elif self.getObjectByName("temple").getState() == AdventureGameObjectTemple.State.closed:
            print("\nOpen the door to the temple!")
        else:
            print("\nYou can now move to the north!")


    def onObjectOpened(self, obj):
        "Callback when an object in the room has been opened"

        used = False
        return used


    def onObjectUsed(self, obj):
        "Callback when an object in the room has been used"

        used = False

        if obj.getName() == "FireStone":
            if self.getObjectByName("tree").getState() == AdventureGameObjectTree.State.burning:
                print("\nThe fire stone absorbs the fire from the tree.")
                print("The tree... It looks alive, almost like it expects you to talk to it.")
                self.getObjectByName("tree").setState(AdventureGameObjectTree.State.notTalkedTo)
                used = True
            elif self.getObjectByName("temple").getState() == AdventureGameObjectTemple.State.overgrown:
                print("\nYou burn the roots covering the temple. You can now reach the door to the temple.")
                self.getObjectByName("temple").setState(AdventureGameObjectTemple.State.closed)
                used = True

        if obj.getName() == "WaterStone" \
           and self.getObjectByName("tree").getState() == AdventureGameObjectTree.State.burning:
            print("\nThe water stone summons a huge amount of water on the tree. The fire is exstinguished.")
            print("The tree... It looks alive, almost like it expects you to talk to it.")
            self.getObjectByName("tree").setState(AdventureGameObjectTree.State.notTalkedTo)
            used = True

        if obj.getName() == "NatureStone" \
           and self.getObjectByName("temple").getState() == AdventureGameObjectTemple.State.overgrown:
            print("\nThe nature stone absorbs the roots covering the temple. You can now reach the door to the temple.")
            self.getObjectByName("temple").setState(AdventureGameObjectTemple.State.closed)
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

        if obj.getName() == "Tree" and phrase != None \
           and self.getObjectByName("tree").getState() == AdventureGameObjectTree.State.riddleGiven:
            if obj.checkAnswer(phrase):
                self.gameHandler.inventory.add(AdventureGameObjectNatureStone())
                self.removeObject("Tree")
                print("\nGood job!")
                print("I'll grant you the nature stone.")
                print("Good bye my friend.")
                print("\nThe tree wanders into the deep forest.")
            else:
                print("\nSorry, wrong answer!")

            used = True

        return used
