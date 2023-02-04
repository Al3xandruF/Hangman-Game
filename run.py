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


def show_new_board(chosen_word):
    """
     Shows up everytime the user chooses a letter
     and refreshes its current state based on user's
     progress throughout the game
    """
    hidden_list = []

    for l in chosen_word:
        if l in correct_letters:
            hidden_list.append(l)
        else:
            hidden_list.append('-')

    print(' '.join(hidden_list))


def check_letter(chosen_letter, hidden_word, tries, matches):
    """
    Checks if the letter the user entered
    matches with the hidden word.
    Also, everytime the function checks
    it will complete the lists of
    correct/incorrect words.
    Will also check if the user has one
    try or less/ if the letter matches
    the hidden word or if the user won or lost.
    """
    end = False

    if chosen_letter in hidden_word and chosen_letter not in correct_letters:
        correct_letters.append(chosen_letter)
        matches += 1
    elif chosen_letter in hidden_word and chosen_letter in correct_letters:
        print("You have already found that letter, try with another one")
    else:
        incorrect_letters.append(chosen_letter)
        tries -= 1

    if tries == 0:
        end = lose()
    elif matches == unique_letters:
        end = win(hidden_word)

    return tries, end, matches


