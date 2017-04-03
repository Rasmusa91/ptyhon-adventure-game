#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tic tac toe game
"""

from random import randint

class TicTacToe:
    "TicTacToe gamehandler"

    m_Board = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

    m_Turn = 0

    def start(self):
        "Start the game"

        winner = -1

        while True:
            self.printBoard()

            if self.m_Turn == 0 or (self.m_Turn > 0 and self.m_Turn % 2 == 0):
                self.playerTurn()
            else:
                self.aiTurn()

            winner = self.checkVictory()
            if winner != -1:
                break

            self.m_Turn += 1

        self.printBoard()

        return winner

    def printBoard(self):
        "Print the board"

        print(chr(27) + "[2J" + chr(27) + "[;H")
        print("Play some TicTacToe!\n")

        print(" x 1 2 3 ")
        print("y  _ _ _ ")
        print("1 |{a}|{b}|{c}|".format(a=self.getBoardMarker(0, 0),
                                       b=self.getBoardMarker(1, 0),
                                       c=self.getBoardMarker(2, 0)))
        print("2 |{a}|{b}|{c}|".format(a=self.getBoardMarker(0, 1),
                                       b=self.getBoardMarker(1, 1),
                                       c=self.getBoardMarker(2, 1)))
        print("3 |{a}|{b}|{c}|".format(a=self.getBoardMarker(0, 2),
                                       b=self.getBoardMarker(1, 2),
                                       c=self.getBoardMarker(2, 2)))

    def getBoardMarker(self, x, y):
        "Get the marker accordingly"

        marker = "_"

        if (self.m_Board[y][x] == 1):
            marker = "x"
        elif (self.m_Board[y][x] == 2):
            marker = "o"

        return marker

    def playerTurn(self):
        "Let the player make a turn"

        print("\nIt's your turn (x)! Place a marker on the board (x,y)")

        move = None
        while move == None:

            move = input("\nAction: ")
            move = self.posFromString(move)

            if move == None:
                print("Invalid action, please use the format of \"x,y\" and an integer between 1 and 3")

            elif self.m_Board[move[1]][move[0]] != 0:
                print("There is already a marker on that position")
                move = None

        self.m_Board[move[1]][move[0]] = 1 if self.m_Turn % 2 == 0 else 2

    def posFromString(self, pos):
        "Convert a string pos to an array of positions"

        res = None
        x = -1
        y = -1
        pos = pos.replace(' ', '')
        pos = pos.split(',')

        if len(pos) == 2:
            try:
                x = int(pos[0])
                y = int(pos[1])
            except ValueError:
                pass

            if x >= 1 and x <= 3 and y >= 1 and y <= 3:
                res = [x - 1, y - 1]

        return res

    def aiTurn(self):
        "Let the ai make a turn"

        print("\nIt's the wizards turn (o)!")
        input("\nPress enter to continue...")

        move = None

        while move == None or self.m_Board[move[1]][move[0]] != 0:
            move = [randint(1, 3) - 1, randint(1, 3) - 1]

        self.m_Board[move[1]][move[0]] = 1 if self.m_Turn % 2 == 0 else 2

    def checkVictory(self):
        "Check if someone has won"

        winner = self.checkStraightVictory()

        if(winner == -1):
            winner = self.checkCrossVictory()

        if(winner == -1):
            winner = self.checkDraw()

        return winner

    def checkStraightVictory(self):
        "Check staight victory"

        for i in [0, 1]:
            for j in [0, 1, 2]:

                curr = -1

                if i == 0:
                    curr = self.m_Board[0][j]
                elif i == 1:
                    curr = self.m_Board[j][0]

                if curr == 0:
                    continue

                for k in [1, 2]:
                    if i == 0 and self.m_Board[k][j] == curr:
                        continue
                    elif i == 1 and self.m_Board[j][k] == curr:
                        continue
                    else:
                        curr = -1

                if curr != -1:
                    return curr

        return -1

    def checkCrossVictory(self):
        "Check cross victory"

        curr = self.m_Board[0][0]
        if curr != 0 and self.m_Board[1][1] == curr:
            if self.m_Board[2][2] == curr:
                return curr

        curr = self.m_Board[2][0]
        if curr != 0 and self.m_Board[1][1] == curr:
            if self.m_Board[2][0] == curr:
                return curr

        return -1

    def checkDraw(self):
        "Check row if victory"

        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                if self.m_Board[j][i] == 0:
                    return -1

        return 0
