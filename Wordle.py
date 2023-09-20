import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, MISSING_COLOR
import tkinter as tk
import threading

def wordle():
    grayscale_mode = False  # Variable to track grayscale mode

    # Check if word is from dictionary
    def check_word(s):
        nonlocal grayscale_mode  # Access the outer grayscale_mode variable
        guess = ""
        row = gw.get_current_row()  # Get current row
        hidden_word = Milestone_1.lower()  # Convert the hidden word to lowercase for comparison

        for col in range(N_COLS):
            letter = gw.get_square_letter(row, col)
            guess += letter

            if letter.lower() == hidden_word[col]:
                # Correct letter in correct position
                if grayscale_mode:
                    gw.set_square_color(row, col, 'gray1')
                else:
                    gw.set_square_color(row, col, CORRECT_COLOR)
            elif letter.lower() in hidden_word:
                # Letter is in the word but not in the correct position
                if grayscale_mode:
                    gw.set_square_color(row, col, 'gray')
                else:
                    gw.set_square_color(row, col, MISSING_COLOR)
            else:
                if grayscale_mode:
                    gw.set_square_color(row, col, 'gray89')
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

    def toggle_grayscale_mode():
        nonlocal grayscale_mode  
        grayscale_mode = not grayscale_mode  

    def toggle_grayscale_mode_button():
        toggle_grayscale_mode()
        if grayscale_mode:
            grayscale_button.config(text="Grayscale Mode ON")
        else:
            grayscale_button.config(text="Grayscale Mode OFF")

    gw = WordleGWindow()
    gw.add_enter_listener(check_word)

    # Milestone_1
    Milestone_1 = random.choice(FIVE_LETTER_WORDS)
    for col, letter in enumerate(Milestone_1):
        row = 0
        gw.set_square_letter(row, col, letter)

    # Create a  window for the button
    root = tk.Tk()
    root.title("Grayscale Mode Toggle")

    # Create a button to toggle grayscale mode
    grayscale_button = tk.Button(root, text="Grayscale Mode OFF", command=toggle_grayscale_mode_button)
    grayscale_button.pack(pady=10)

    threading.Thread(target=root.mainloop).start()

# Start the Wordle game in the main thread
if __name__ == "__main__":
    wordle()
