#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""


from abc import ABC, abstractmethod


class AdventureGameObject(ABC):
    "Adventure Game Object"


    pickedUp = False


    @abstractmethod
    def getName(self):
        "Get the name of the object"
        pass


    @abstractmethod
    def check(self):
        "Print an desc. of the object"
        pass


    @abstractmethod
    def open(self, openedByRoom):
        "Try to open the object"
        pass


    @abstractmethod
    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"
        pass


    @abstractmethod
    def kick(self, kickedByRoom):
        "Try to kick the object"
        pass


    @abstractmethod
    def move(self, movedByRoom):
        "Try to move the object"
        pass


    @abstractmethod
    def use(self, usedByRoom):
        "Try to use the object"
        pass


    @abstractmethod
    def canPickup(self):
        "Check if the object is pickupable"
        pass


    def pickup(self):
        "Try to pickup the object"

        self.pickedUp = True


    def drop(self):
        "Try to drop the object"

        self.pickedUp = False

    def isPickedup(self):
        "Check if an object is pickedup"

        return self.pickedUp
