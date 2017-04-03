#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure gamehandler
"""


from room1 import FirstAdventureGameRoom
from room2 import SecondAdventureGameRoom
from room3 import ThirdAdventureGameRoom
from room4 import FourthAdventureGameRoom
from room5 import FifthAdventureGameRoom
from room6 import SixthAdventureGameRoom
from room7 import SeventhAdventureGameRoom
from inventory import Inventory


class AdventureGame:
    "Adventure GameHandler"


    rooms = []
    currentRoom = None
    inventory = Inventory()
    debug = False


    def initialize(self):
        "Initialize the game"

        self.rooms = [
            [SeventhAdventureGameRoom(self), None, FourthAdventureGameRoom(self), FifthAdventureGameRoom(self)],
            [SixthAdventureGameRoom(self), SecondAdventureGameRoom(self), ThirdAdventureGameRoom(self), None],
            [None, FirstAdventureGameRoom(self), None, None]]

        print(chr(27) + "[2J" + chr(27) + "[;H")
        self.currentRoom = self.rooms[2][1]
        self.currentRoom.printImage()
        self.currentRoom.printInfo()


    def start(self):
        "Start the game"

        self.initialize()
        victory = False

        while not victory:
            victory = self.checkCommand()


    def checkCommand(self):
        "Check command"

        _input = input("--> ")
        args = self.cleanUpCommandArgs(_input.split(' '))
        victory = False

        if len(args) > 0:
            args1 = None
            args2 = None

            if len(args) > 1:
                args1 = args[1]

            if len(args) > 2:
                args2 = args[2]

            if(args[0] in ["i", "info"]):
                self.currentRoom.printInfo()
            elif(args[0] in ["h", "hjälp", "help"]):
                self.printHelp()
            elif(args[0] in ["fr", "fram", "forward"]):
                print("\nUse north, east, south or west instead!")
            elif(args[0] in ["ba", "bak", "back"]):
                print("\nUse north, east, south or west instead!")
            elif(args[0] in ["n", "north", "norr"]):
                victory = self.travelNorth()
            elif(args[0] in ["e", "east", "öst"]):
                victory = self.travelEast()
            elif(args[0] in ["s", "south", "söder"]):
                victory = self.travelSouth()
            elif(args[0] in ["w", "west", "väst"]):
                victory = self.travelWest()
            elif(args[0] in ["se", "see"]):
                self.currentRoom.printSee()
            elif(args[0] in ["l", "ledtråd", "clue", "hint"]):
                self.currentRoom.printClue()
            elif(args[0] in ["o", "objekt", "object"]):
                self.currentRoom.printObjects()
            elif(args[0] in ["ö", "öppna", "open"]):
                self.openObject(args1)
            elif(args[0] in ["t", "titta", "look", "check"]):
                self.checkObject(args1)
            elif(args[0] in ["s", "sparka", "kick"]):
                self.kickObject(args1)
            elif(args[0] in ["f", "flytta", "move"]):
                self.moveObject(args1)
            elif(args[0] in ["p", "prata", "talk"]):
                self.talkObject(args1, args2)
            elif(args[0] in ["inv", "inventarier", "inventory"]):
                self.inventory.read()
            elif(args[0] in ["ta", "take", "pick"]):
                self.pickupItem(args1)
            elif(args[0] in ["sl", "släpp", "drop"]):
                self.dropItem(args1)
            elif(args[0] in ["a", "använd", "use"]):
                self.useItem(args1)
            else:
                print("\nCommand not available")

        return victory


    def cleanUpCommandArgs(self, p_Args):
        "Clean up the args in a command"

        i = 0
        while i < len(p_Args):
            if p_Args[i] == '':
                del p_Args[i]
            else:
                i += 1

        return p_Args


    def printHelp(self):
        "Prints help"

        print("""Commands:
      i, info                       Prints the description of the room
      h, hjälp, help                Prints a list of commands
      n, norr, north                Travel to the room to the north
      e, east, öst                  Travel to the room to the east
      s, south, söder               Travel to the room to the south
      w, west, väst                 Travel to the room to the west
      se, see                       Prints relevant information about the room
      l, ledtråd, clue, hint        Prints a clue to solve the room

      o, objekt, object             List all the objects in the room
      ö, öppna, opened {o}        Open an object
      t, titta, look, check {o}   Print a description of the object
      s, sparka, kick {o}         Kick an object
      f, flytta, move {o}         Move an object
      p, prata, talk {o} {p}    Talk to an object where p is the phrase

      inv, inventarier, inventory   List all the items in your inventory
      ta, take, pick {o}          Take an object
      sl, släpp, drop {o}         Drop an object
      a, använd, use {o}          Use an object""")


    def getObjectByName(self, name):
        "Try to get an object in the current room or in the inventory"

        o = self.currentRoom.getObjectByName(name)

        if o == None:
            o = self.inventory.getObjectByName(name)

        return o


    def checkObject(self, name):
        "Print a desc of the object"

        if name == None:
            print("\nPlease enter the name of the object you want to check.")
            return

        o = self.getObjectByName(name)

        if o != None:
            o.check()
        else:
            print("\nObject {o} not found".format(o=name))


    def openObject(self, name):
        "Try to perform the action open on an object"

        if name == None:
            print("\nPlease enter the name of the object you want to open.")
            return

        o = self.getObjectByName(name)

        if o != None:
            openedByRoom = self.currentRoom.onObjectOpened(o)
            o.open(openedByRoom)
        else:
            print("\nObject {o} not found".format(o=name))


    def kickObject(self, name):
        "Try to perform the action kick on an object"

        if name == None:
            print("\nPlease enter the name of the object you want to kick.")
            return

        o = self.getObjectByName(name)

        if o != None:
            if not o.isPickedup():
                kickedByRoom = self.currentRoom.onObjectKicked(o)
                o.kick(kickedByRoom)
            else:
                print("\nYou can't move an object while it's in your inventory.")
        else:
            print("\nObject {o} not found".format(o=name))


    def moveObject(self, name):
        "Try to perform the action move on an object"

        if name == None:
            print("\nPlease enter the name of the object you want to move.")
            return

        o = self.getObjectByName(name)

        if o != None:
            if not o.isPickedup():
                movedByRoom = self.currentRoom.onObjectMoved(o)
                o.move(movedByRoom)
            else:
                print("\nYou can't move an object while it's in your inventory.")
        else:
            print("\nObject {o} not found".format(o=name))


    def talkObject(self, name, phrase):
        "Try to perform the action talk on an object"

        if name == None:
            print("\nPlease enter the name of the object you want to talk to.")
            return

        o = self.getObjectByName(name)

        if o != None:
            talkedByRoom = self.currentRoom.onObjectTalked(o, phrase)
            o.talk(talkedByRoom, phrase)
        else:
            print("\nObject {o} not found".format(o=name))


    def pickupItem(self, itemName):
        "Try to pickup an item from the inventory"

        if itemName == None:
            print("\nPlease enter the name of the object you want to pick up.")
            return

        o = self.currentRoom.removeObject(itemName)

        if o != None:
            if o.canPickup():
                self.inventory.add(o)
                print("\nYou have picked up the object \"{o}\"".format(o=o.getName()))
            else:
                print("\nObject \"{o}\" can not be picked up.".format(o=o.getName()))
        else:
            print("\nObject \"{o}\" could not be found.".format(o=o.getName()))


    def dropItem(self, itemName):
        "Try to drop an item from the inventory"

        if itemName == None:
            print("\nPlease enter the name of the object you want to drop.")
            return

        o = self.inventory.remove(itemName)

        if o != None:
            print("\nYou have dropped the object \"{o}\".".format(o=o.getName()))
            self.currentRoom.addObject(o)
        else:
            print("\nYou dont have the object \"{o}\" in your inventory.".format(o=itemName))


    def useItem(self, itemName):
        "Try to use an item from the inventory"

        if itemName == None:
            print("\nPlease enter the name of the object you want to use.")
            return

        o = self.inventory.getObjectByName(itemName)

        if o != None:
            usedByRoom = self.currentRoom.onObjectUsed(o)
            o.use(usedByRoom)
        else:
            print("Object \"{o}\" not found in the inventory.".format(o=itemName))


    def destroyItem(self, itemName):
        "Try to perm. destroy an item"

        self.inventory.remove(itemName)
        self.currentRoom.removeObject(itemName)


    def travelNorth(self):
        "Travel north"

        victory = False

        if self.currentRoom.north():
            victory = self.travel(0, 1)

        return victory


    def travelEast(self):
        "Travel east"

        victory = False

        if self.currentRoom.east():
            victory = self.travel(1, 0)

        return victory


    def travelSouth(self):
        "Travel south"

        victory = False

        if self.currentRoom.south():
            victory = self.travel(0, -1)

        return victory


    def travelWest(self):
        "Travel west"

        victory = False

        if self.currentRoom.west():
            victory = self.travel(-1, 0)

        return victory

    def travel(self, x, y):
        "Travel"

        victory = False
        currX = -1
        currY = -1

        for arr in self.rooms:
            try:
                index = arr.index(self.currentRoom)
                currY = index
                currX = self.rooms.index(arr)
            except Exception:
                pass

        self.currentRoom = self.rooms[currX - y][currY + x]

        if self.currentRoom != None:
            print(chr(27) + "[2J" + chr(27) + "[;H")
            self.currentRoom.printImage()
            self.currentRoom.printInfo()
        else:
            print("\nCongratulations! You have beaten the game!")
            victory = True

        return victory
