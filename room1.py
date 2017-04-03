#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure first room
"""


from room import AdventureGameRoom
from objectBandits import AdventureGameObjectBandits
from objectRabbit import AdventureGameObjectRabbit
from objectSign import AdventureGameObjectSign


class FirstAdventureGameRoom(AdventureGameRoom):
    "Adventure Game Room"


    def __init__(self, gameHandler):
        "Construct the room"

        AdventureGameRoom.__init__(self, gameHandler)

        self.objects = [
            AdventureGameObjectBandits(),
            AdventureGameObjectRabbit(),
            AdventureGameObjectSign()
        ]


    def printImage(self):
        "Prints an image of the room"

        print("------------------|   |-------------------")
        print("|t   t   t    t     b      t   t   t     |")
        print("|  t   t   t     b     b       t     t   |")
        print("|   t        S      b                    |")
        print("| t   p                    t       r   t |")
        print("|  t   t     t  t    t  t    t  t    t   |")
        print("------------------------------------------")
        print("- p: player")
        print("- b: bandit")
        print("- r: rabbit")
        print("- t: tree")
        print("- S: sign")


    def printInfo(self):
        "Prints information about the room"

        print("\nYou find yourself in a small field surrounded by a dense forest.")

        if self.getObjectByName("bandits").getState() != AdventureGameObjectBandits.State.cooperative:
            print("The only path leading anywhere of interest is north, \
but the path is blocked by a pack of hungry bandits.")
        else:
            print("The bandits will let you pass to the north!")


    def north(self):
        "Check if you can go north in the room"

        canPass = True

        if self.getObjectByName("bandits").getState() != AdventureGameObjectBandits.State.cooperative:
            canPass = False
            print("\nA pack of angry bandits are blocking the path to the north. They won't let you pass")

        #DEBUG
        if self.gameHandler.debug:
            canPass = True

        return canPass


    def east(self):
        "Check if you can go east in the room"

        print("\nThere is no point of interest to the east.")
        return False


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

        print("\nYou see quite a small field of grass, but north of you, there is a forest.")

        if self.getObjectByName("bandits").getState() != AdventureGameObjectBandits.State.cooperative:
            print("The path into the forset is blocked by a pack of hungry bandits.")
            print("When you focus hard enough you can also see a rabbit, how convenient, huh?")
        else:
            print("The bandits will let you pass to the north.")


    def printClue(self):
        "Print a clue to solve the room"

        if self.getObjectByName("rabbit") != None:
            print("\nWhy don't you try to feed the bandits to make them more cooperative? \
I'm sure they'd like that rabbit over there.")
        elif self.getObjectByName("bandits").getState() != AdventureGameObjectBandits.State.cooperative:
            print("\nYou need to kill and gut the rabbit before the bandits accepts it!")
        else:
            print("Go north! The bandits will let you pass!")


    def onObjectOpened(self, obj):
        "Callback when an object in the room has been opened"
        pass


    def onObjectUsed(self, obj):
        "Callback when an object in the room has been used"

        used = False

        if obj.getName().lower() == "rabbit" and obj.getState() == AdventureGameObjectRabbit.State.gutted:
            print("\nYou gave the gutted rabbit to the bandits.")
            print("The bandits are now a bit more cooperative and will \
now let you pass to the north!")
            self.gameHandler.destroyItem(obj.getName())
            self.getObjectByName("bandits").setState(AdventureGameObjectBandits.State.cooperative)
            used = True

        return used


    def onObjectKicked(self, obj):
        "Callback when an object in the room has been kicked"
        pass


    def onObjectMoved(self, obj):
        "Callback when an object in the room has been moved"
        pass


    def onObjectTalked(self, obj, phrase):
        "Callback when an object in the room has been kicked"
        pass
