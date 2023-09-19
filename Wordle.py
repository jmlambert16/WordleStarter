# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    #Check if word is from dictionary
    def check_word(s):
        word = ""
        row = gw.get_current_row() #sets current row 
        for col, letter in enumerate(Milestone_1):
            letter = gw.get_square_letter(row, col)
            word = word + letter
        lowercase = word.lower()

        if lowercase in FIVE_LETTER_WORDS:
            gw.show_message("Yep")
            
            #if word is dictionary then it changes green
            for col, letter in enumerate(Milestone_1):
                gw.set_square_color(row, col, 'green')
        else:
            gw.show_message("Not in word list")
            #if word is not in dictionary then it changes red
            for col, letter in enumerate(Milestone_1):
                gw.set_square_color(row, col, 'red')

        #Increments current row by 1 each time enter is pressed
        row += 1
        gw.set_current_row(row)


    gw = WordleGWindow()
    gw.add_enter_listener(check_word)

    # Milestone_1
    Milestone_1 = random.choice(FIVE_LETTER_WORDS)
    for col, letter in enumerate(Milestone_1):
        row = 0
        gw.set_square_letter(row, col, letter)






        

# Startup code

if __name__ == "__main__":
    wordle()
