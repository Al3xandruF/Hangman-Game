"""Chooses a random object from a list of objects (words)"""
from random import choice


# Main variables for usage in developing the game
words = ['flower', 'piano', 'speaker', 'dinner', 'program']
correct_letters = []
incorrect_letters = []
TRIES = 6
RIGHT_ANSWERS = 0
GAME_OVER = False


# Functions which will make the game work as planned
def choose_word(list_of_words):
    """
    Chooses a random word from the list
    """
    chosen_word = choice(list_of_words)
    different_letters = len(set(chosen_word))

    return chosen_word, different_letters


def ask_letter():
    """
    Asks the user to choose a letter
    from the alphabet throughout the while loop.
    """
    chosen_letter = ''
    is_valid = False
    while not is_valid:
        chosen_letter = input("Please choose a letter:\n")

        if chosen_letter.isalpha() and len(chosen_letter) == 1:
            is_valid = True
        else:
            print("You haven't chosen a correct letter")

    return chosen_letter


def show_new_board(chosen_word):
    """
    Shows up everytime the user chooses a letter
    and refreshes its current state based on user's
    progress throughout the game.
    """
    hidden_list = []

    for right_letter in chosen_word:
        if right_letter in correct_letters:
            hidden_list.append(right_letter)
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


def lose():
    """
    Prints out when the user has no available
     choices and lost the game. Also shows
     the user what the hidden word was.
    """
    print("You don't have any tries left")
    print("The hidden word was " + word + ". GAME OVER!")

    return True


def win(revealed_word):
    """
    Prints out when the user guessed
    the word and won. Also, it reveals
    the word which the user guessed.
    """
    show_new_board(revealed_word)
    print("Congratulations, you guessed the word!!!")

    return True


word, unique_letters = choose_word(words)


"""
Creates the dynamic of the game by calling
all functions based on the player's choices
and repeats itself until the player looses
or wins and game ends.
"""
while not GAME_OVER:
    print('\n' + '*' * 20 + '\n')
    show_new_board(word)
    print('\n')
    print('Incorrect letters: ' + '-'.join(incorrect_letters))
    print(f'Tries: {TRIES}')
    print('\n' + '*' * 20 + '\n')
    letter = ask_letter()
    TRIES, over, RIGHT_ANSWERS = check_letter(letter, word, TRIES, RIGHT_ANSWERS) # noqa
    GAME_OVER = over
