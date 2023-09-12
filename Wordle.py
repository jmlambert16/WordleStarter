# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Milestone_1
    Milestone_1 = random.choice(FIVE_LETTER_WORDS)
    for col, letter in enumerate(Milestone_1):
        row = 0
        gw.set_square_letter(row, col, letter)
        

# Startup code

if __name__ == "__main__":
    wordle()

