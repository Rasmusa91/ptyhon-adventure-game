#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Adventure game!!!
"""


import getopt, sys
from game import AdventureGame


def printHelp():
    "Prints help"

    print("Description:")
    print("Use the command line to navigate the game to the last room.")

    print("""Options:
  -h, --help                       Prints the available commands
  -i, --info                       Prints a description about the game
  -v, --version                    Prints the current version
  -a, --about                      Prints information about the author
  -c, --cheat                      Prints the shortest path through the game""")


def printVersion():
    "Prints version"

    print("Version 1.0")


def printInfo():
    "Prints info"

    print("Welcome to the adventure game!")
    print("The game is played in some kind of fantasy world where you have \
to complete tasks in 7 different \"rooms\" to complete the game.")
    print("In each rooms you'll need to complete a sequence of tasks in order to gain access to the next room.")


def printCheat():
    "Prints cheat"

    print("Room 1:")
    print("  kick rabbit")
    print("  open rabbit")
    print("  pick rabbit")
    print("  use rabbit")
    print("  north")

    print("Room 2:")
    print("  move log")
    print("  kick log")
    print("  east")

    print("Room 3:")
    print("  pick fishingrod")
    print("  use fishingrod (until you get a fish)")
    print("  use fish")
    print("  talk waterelemental")
    print("  talk waterelemental")
    print("  talk waterelemental water")
    print("  north")

    print("Room 4:")
    print("  use waterstone")
    print("  talk dragon")
    print("  talk dragon")
    print("  talk dragon fire")
    print("  east")

    print("Room 5:")
    print("  talk wizard")
    print("  talk wizard")
    print("  (win game)")
    print("  west")

    print("Room 4:")
    print("  south")

    print("Room 3:")
    print("  west")

    print("Room 2:")
    print("  use magicsword")
    print("  west")

    print("Room 6:")
    print("  use firestone")
    print("  talk tree")
    print("  talk tree")
    print("  talk tree grass")
    print("  use naturestone")
    print("  open temple")
    print("  north")

    print("Room 7:")
    print("  drop firestone")
    print("  drop waterstone")
    print("  drop naturestone")
    print("  north")


def printAbout():
    "Print about me"

    print("My name is Rasmus Appeqlvist and I'm the author of this game. I'm a student at BTH and I like programming!")


def main():
    "Main function"

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hivac", ["help", "info", "version", "about", "cheat"])

        if False:
            print(args)

        for opt, arg in opts:
            if False:
                print(arg)

            if opt in ("-h", "--help"):
                printHelp()
                sys.exit(0)
            if opt in ("-i", "--info"):
                printInfo()
                sys.exit(0)
            if opt in ("-v", "--version"):
                printVersion()
                sys.exit(0)
            if opt in ("-a", "--about"):
                printAbout()
                sys.exit(0)
            if opt in ("-c", "--cheat"):
                printCheat()
                sys.exit(0)

    except Exception as e:
        print(e)
        sys.exit(1)

    print(chr(27) + "[2J" + chr(27) + "[;H")
    printInfo()

    input("\nPress enter to continue...")

    game = AdventureGame()
    game.start()

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nExiting...')
        sys.exit(0)
