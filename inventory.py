#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Inventory
"""


class Inventory:
    "Handle the inventory"


    objects = []


    def read(self):
        "Read the inventory"

        if len(self.objects) > 0:
            print("\nInventory:")
            for item in self.objects:
                print("  {item}".format(item=item.getName()))
        else:
            print("\nYou don't have any items in your inventory")


    def add(self, item):
        "Add item to inventory"

        self.objects.append(item)


    def remove(self, item):
        "Remove item from inventory"

        o = self.getObjectByName(item)

        if o != None:
            index = self.objects.index(o)
            del self.objects[index]

        return o


    def getObjectByName(self, itemName):
        "Gets an object by name"

        o = None

        for obj in self.objects:
            if obj.getName().lower() == itemName.lower():
                o = obj

        return o
