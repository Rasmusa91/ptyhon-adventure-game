#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure room
"""


from abc import ABC, abstractmethod


class AdventureGameRoom(ABC):
    "Adventure Game Room"

    gameHandler = None
    objects = []


    def __init__(self, gameHandler):
        "Construct the room"

        self.gameHandler = gameHandler


    @abstractmethod
    def printInfo(self):
        "Prints information about the room"
        pass


    @abstractmethod
    def north(self):
        "Check if you can go north in the room"
        pass


    @abstractmethod
    def east(self):
        "Check if you can go east in the room"
        pass


    @abstractmethod
    def south(self):
        "Check if you can go south in the room"
        pass


    @abstractmethod
    def west(self):
        "Check if you can go west in the room"
        pass


    @abstractmethod
    def printSee(self):
        "Check if you can see anything spec. in the room"
        pass


    @abstractmethod
    def printClue(self):
        "Print a clue to solve the room"
        pass


    def printObjects(self):
        "Print all found objects"

        if len(self.objects) > 0:
            print("\nObjects found:")
            for obj in self.objects:
                print("  {o}".format(o=obj.getName()))
        else:
            print("\nNo objects found")


    def getObjectByName(self, name):
        "Try to get an item by name"

        name = name.lower()
        o = None

        for obj in self.objects:
            if(obj.getName().lower() == name.lower()):
                o = obj
                break

        return o


    def addObject(self, obj):
        "Adds an object to the room"

        self.objects.append(obj)


    def removeObject(self, obj):
        "Tries to remove an object from the room"

        o = self.getObjectByName(obj)

        if o != None:
            if o in self.objects:
                index = self.objects.index(o)
                del self.objects[index]

        return o


    @abstractmethod
    def onObjectOpened(self, obj):
        "Callback when an object in the room has been opened"
        pass


    @abstractmethod
    def onObjectUsed(self, obj):
        "Callback when an object in the room has been used"
        pass


    @abstractmethod
    def onObjectKicked(self, obj):
        "Callback when an object in the room has been kicked"
        pass


    @abstractmethod
    def onObjectMoved(self, obj):
        "Callback when an object in the room has been moved"
        pass


    @abstractmethod
    def onObjectTalked(self, obj, phrase):
        "Callback when an object in the room has been talked to"
        pass
