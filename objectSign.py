#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure object
"""


from object import AdventureGameObject
import requests, json


class AdventureGameObjectSign(AdventureGameObject):
    "Adventure Game Object"


    def getName(self):
        "Get the name of the object"

        return "Sign"


    def check(self):
        "Print an desc. of the object"

        print("\nYou see a sign, the sign says:")
        self.getQuoteWebsite()


    def open(self, openedByRoom):
        "Try to open the object"

        if openedByRoom:
            return

        print("\nYou can't open the sign.")


    def kick(self, kickedByRoom):
        "Try to kick the object"

        print("\nYou can't kick the sign.")


    def move(self, movedByRoom):
        "Try to move the object"

        print("\nYou can't move the sign.")


    def talk(self, talkedByRoom, phrase):
        "Try to talk to the object"

        print("\nYou can't talk to the sign.")


    def use(self, usedByRoom):
        "Try to use the object"
        pass


    def canPickup(self):
        "Check if the object is pickupable"

        return False


    def getQuoteWebsite(self):
        "Get quote from website"

        url = "http://dbwebb.se/javascript/lekplats/get-marvin-quotes-using-ajax/quote.php"

        try:
            quoteJson = json.loads(self.getWebsiteContents(url))
            print("  {q}".format(q=quoteJson["quote"]))
        except Exception as e:
            print(e)


    def getWebsiteContents(self, url):
        "Gets contents from website"

        c = None

        try:
            req = requests.get(url)
            c = req.text
        except Exception as e:
            print(e)

        return c
