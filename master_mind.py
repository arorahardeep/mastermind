#!/usr/bin/env python

"""

This is program implements master mind game
@author : Hardeep Arora
@date   : 03-Dec-2017

Rules of the game
    1. We have 8 colors in the game
    2. Computer selects random 4 colors
    3. You need to guess them in 12 chances
    4. Computer rates your guess as follows
       4a. Each color at right position is one red, each color at wrong position is one white
    5. Four Red means you won the game.

"""

import random


class GameConfig:

    def __init__(self):
        self.color_palette = ['red','orange','yellow','green','blue','pink','grey','white']
        self.size_palette = len(self.color_palette)
        self.chances = 12
        self.guess_colors = 4
        self.picked_board = []
        self.input_message = "Your Guess (4 colors):"
        self.win_message = "You won"
        self.loose_message = "You loose"
        self.init_state()

    def init_state(self):
        print("Choose from : ", self.color_palette)
        self.picked_board = random.sample(self.color_palette,self.guess_colors)

    def get_challenge(self):
        return self.picked_board


class GameLogic:

    def __init__(self):
        self.gc = GameConfig()

    def match(self, guess):
        red = 0
        white = 0
        for ind, col in enumerate(guess):
            try:
                col_ind = self.gc.picked_board.index(col)
                if col_ind == ind:
                    red = red + 1
                else:
                    white = white + 1
            except ValueError:
                pass

        return red, white

    def game_loop(self):
        for chance in range(0,self.gc.chances):
            print()
            print(str(chance + 1) + ": " + self.gc.input_message)
            guess = [str(x) for x in input().split()]
            red, white = self.match(guess)
            print("Result : Red - %i, White - % i"%(red,white))
            if red == 4:
                print(self.gc.win_message)
                return

        print(self.gc.loose_message)
        print(self.gc.picked_board)


class MasterMind:
    def __init__(self):
        self.gl = GameLogic()

    def play(self):
        self.gl.game_loop()


def main():
    MasterMind().play()

if __name__ == "__main__":
    main()
