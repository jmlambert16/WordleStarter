# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, MISSING_COLOR

def wordle():
    # Check if word is from dictionary
    def check_word(s):
        guess = ""
        row = gw.get_current_row()  # Get current row
        hidden_word = Milestone_1.lower()  # Convert the hidden word to lowercase for comparison

        for col in range(N_COLS):
            letter = gw.get_square_letter(row, col)
            guess += letter

            if letter.lower() == hidden_word[col]:
                # Correct letter in correct position
                gw.set_square_color(row, col, CORRECT_COLOR)
            elif letter.lower() in hidden_word:
                # Letter is in the word but not in the correct position
                gw.set_square_color(row, col, MISSING_COLOR)
            else:
                # Incorrect letter
                gw.set_square_color(row, col, 'red')

        if guess.lower() == hidden_word:
            gw.show_message("Congratulations! You guessed the word.")
        else:
            gw.show_message("Keep trying!")

        # Increment current row by 1 each time enter is pressed
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
