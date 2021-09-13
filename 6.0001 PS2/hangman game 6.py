
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    assumes wordlist is a list of strings, representing words
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    '''
    assumes secret word is a string, representing the word the user is guessing
    and that all the letters are lowercase
    assumes letters_guessed is a list individual lowercase letters
    returns a boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    shared_characters = ""
    # filled out shared_characters string
    for char in secret_word:
        if char in letters_guessed:
            shared_characters = shared_characters + char
    # compare strings
    if shared_characters == secret_word:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    assumes secret word is a string, representing the word the user is guessing
    and that all the letters are lowercase
    assumes letters_guessed is a list individual lowercase letters
    returns a string, representing the guess so far with the letters that have
    been guessed, and a underscore space (_ ) for the unguessed letters
    '''
    guessed_word_list = ["_ "]*len(secret_word)
    # replaced guessed letters into list
    var_index = 0
    for char in secret_word:
        if char in letters_guessed:
            guessed_word_list[var_index] = char
            var_index += 1
        else:
            var_index += 1
    # convert list to string
    guessed_word = ""
    for ele in guessed_word_list:
        guessed_word += ele
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    assumes letters_guessed is a list individual lowercase letters
    returns a string, representing the letters that have not yet been guessed
    '''
    # make list of alphabet
    available_letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                              "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                              "w", "x", "y", "z"]
    # subtract letters_guessed
    for char in letters_guessed:
        if char in available_letters_list:
            available_letters_list.remove(char)
    # convert available letters list to string
    available_letters = ""
    for ele in available_letters_list:
        available_letters += ele
    return available_letters


def lose_game(secret_word):
    """run to generate losing end game code, when guesses_remaining==0"""
    print("Sorry, you ran out of guesses. The word was %s." % secret_word)


def win_game(secret_word, guesses_remaining):
    """run to generate wining end game code,
    when is_word_guessed(secret_word, letters_guessed) returns True"""
    score = guesses_remaining * len("".join(set(secret_word)))
    print("Congratulations, you won!")
    print("Your total score for this game is: %s" % score)


def next_round(warnings_remaining, guesses_remaining, available_letters,
               secret_word, letters_guessed):
    """
    assumes warnings_remaining is an int
    assumes guesses_remaining is an int
    assumes availalbe_letters is a string
    assumes secret_word is a string
    assumes letters_guessed is a kist of characters
    plays out a standard round.
    returns 2-tuple of (int,string), with guessed_letter at index 0,
    availables_letters at index 1"""
    availables_letters = get_available_letters(letters_guessed)
    print("------------")
    print("You have %d warnings left." % warnings_remaining)
    print("You have %d guesses left." % guesses_remaining)
    print("Available letters: %s" % (available_letters))
    print(get_guessed_word(secret_word, letters_guessed))
    print("Please guess a letter:")
    guessed_letter = input()
    return guessed_letter, availables_letters


def hangman(secret_word):
    '''
    assumes secret_word is a string, representing the word to be guessed
    Starts up an interactive game of Hangman on the command line.
    '''
    # initialize variables
    guesses_remaining = 6
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    letters_guessed = ""
    guesses_remaining = 6
    warnings_remaining = 3
    print("Loading word list from file...")
    print("55900 words loaded.")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %s letters long." % (len(secret_word)))

    lower_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                      "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                      "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    while is_word_guessed(secret_word, letters_guessed) is not True:
        available_letters = get_available_letters(letters_guessed)
        round_result = next_round(warnings_remaining, guesses_remaining,
                                  available_letters, secret_word, letters_guessed)
        guessed_letter = round_result[0]
        available_letters = round_result[1]
        letters_guessed = letters_guessed + guessed_letter

        if guessed_letter in upper_alphabet:
            guessed_letter = str.lower(guessed_letter)
        if guessed_letter in lower_alphabet:
            if guessed_letter in available_letters:
                letters_guessed = letters_guessed + guessed_letter
                did_win = is_word_guessed(secret_word, letters_guessed)
                if did_win:
                    win_game(secret_word, guesses_remaining)
                else:
                    if guessed_letter in ["a", "e", "i", "o", "u"]:
                        guesses_remaining -= 2
                        if guesses_remaining <= 0:
                            lose_game(secret_word)
                            break
                    else:
                        guesses_remaining -= 1
                        if guesses_remaining <= 0:
                            lose_game(secret_word)
                            break

            else:  # if letter already guessed
                warnings_remaining -= 1
                if warnings_remaining <= 0:
                    guesses_remaining -= 1
                print("Oops! You've already guessed that letter.")
                if guesses_remaining <= 0:
                    lose_game(secret_word)
                    break

        else:  # invalid character guess
            warnings_remaining -= 1
            if warnings_remaining <= 0:
                guesses_remaining -= 1
            print("Oops! That is not a valid letter.")
            if guesses_remaining <= 0:
                lose_game(secret_word)
                break


# hangman("kittens")
hangman(choose_word(load_words()))

# TODO writeup gameplay instructions
"""
* At the start of the game, let the user know how many
  letters the secret_word contains and how many guesses s/he starts with.
* The user should start with 6 guesses

* Before each round, you should display to the user how many guesses
  s/he has left and the letters that the user has not yet guessed.

* Ask the user to supply one guess per round. Remember to make
  sure that the user puts in a letter!

* The user should receive feedback immediately after each guess
  about whether their guess appears in the computer's word.

* After each guess, you should display to the user the
  partially guessed word so far.
"""
