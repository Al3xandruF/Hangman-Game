# Chooses a random object from a list of objects (words)
from random import choice


# main variables for usage in developing the game
words = ['flower', 'piano', 'speaker', 'dinner', 'program']
correct_letters = []
incorrect_letters = []
tries = 6
right_answers = 0
game_over = False


# Functions which will make the game work as planned
def choose_word(list_of_words):
    """
    Chooses a random word from the list
    """
    chosen_word = choice(list_of_words)
    different_letters = len(set(choose_word))

    return chosen_word, different_letters


def ask_letter():
    """
    Asks the user to choose a letter
    throughout the while loop.
    """
    chosen_letter = ''
    is_valid = False

    while not is_valid:
        chosen_letter = input("Please choose a letter")

        if chosen_letter.isalpha() and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You haven't chosen a correct letter")

    return chosen_letter





