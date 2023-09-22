import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import tkinter as tk
import threading

def wordle():
    grayscale_mode = False  # Variable to track grayscale mode
    max_rows = 5 
    Words_Guessed = 0
    game_count = 0

    # Check if word is from dictionary
    def check_word(s):
        nonlocal Words_Guessed  # Access the Words_Guessed variable
        Words_Guessed += 1  # Increment the button click count
        update_button_counter(button_counter_label)  # Pass the label as a parameter

        row = gw.get_current_row()  # Get current row
        guess = ""
        hidden_word = Milestone_1.lower()  # Convert the hidden word to lowercase for comparison
        Final_word = Milestone_1.upper()
        

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
            if row == max_rows:
                gw.show_message("The word was " + Final_word + ", Click Try Again")
            else:
                gw.show_message("Keep trying!")

        # Increment current row by 1 each time enter is pressed
        row += 1
        gw.set_current_row(row)

    def update_button_counter(label):  # Pass the label as a parameter
        # Update the label text to show the number of button clicks and games played
        label.config(text=f"Words Guessed: {Words_Guessed}, Games Played: {game_count}")

    def toggle_grayscale_mode():
        nonlocal grayscale_mode
        grayscale_mode = not grayscale_mode

    def toggle_grayscale_mode_button():
        toggle_grayscale_mode()
        if grayscale_mode:
            grayscale_button.config(text="Grayscale Mode ON")
        else:
            grayscale_button.config(text="Grayscale Mode OFF")

    def restart_game():
        nonlocal game_count
        game_count += 1 
        gw.show_message("")
        gw.set_current_row(0)

        # Clear the board by resetting colors and letters for all rows and columns
        for row in range(N_ROWS):
            for col in range(N_COLS):
                gw.set_square_color(row, col, UNKNOWN_COLOR)
                gw.set_square_letter(row, col, '')

        # Select a new random word
        global Milestone_1
        Milestone_1 = random.choice(FIVE_LETTER_WORDS)

    gw = WordleGWindow()
    gw.add_enter_listener(check_word)

    # Milestone_1
    global Milestone_1
    Milestone_1 = random.choice(FIVE_LETTER_WORDS)

    # Create a window for the buttons
    root = tk.Tk()
    root.title("Wordle Game")

    # Create a label to display the button clicks and games played
    button_counter_label = tk.Label(root, text=f" Words Guessed: {Words_Guessed}, Games Played: {game_count}")
    button_counter_label.pack(pady=10)

    # Create a button to toggle grayscale mode
    grayscale_button = tk.Button(root, text="Grayscale Mode OFF", command=toggle_grayscale_mode_button)
    grayscale_button.pack(pady=10)

    # Create a button to restart the game
    restart_button = tk.Button(root, text="Try Again", command=restart_game)
    restart_button.pack(pady=10)

    threading.Thread(target=root.mainloop).start()

# Start the Wordle game in the main thread
if __name__ == "__main__":
    wordle()
