
# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
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
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    shared_characters = ""
    #filled out shared_characters string 
    for char in secret_word: 
        if char in letters_guessed:
            shared_characters = shared_characters + char
    #compare strings                
    if shared_characters == secret_word :
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word_list = ["_ "]*len(secret_word)
    #replaced guessed letters into list
    var_index = 0
    for char in secret_word:
        if char in letters_guessed:
            guessed_word_list [var_index] = char
            var_index += 1
    #convert list to string
    guessed_word = ""
    for ele in guessed_word_list:
        guessed_word += ele
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
     #make list of alphabet
    available_letters_list = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #subtract letters_guessed
    for char in letters_guessed:
        if char in available_letters_list:
            available_letters_list.remove(char)
    #convert available letters list to string
    available_letters = ""
    for ele in available_letters_list:
        available_letters += ele
    return available_letters 

#run when guesses_remaining==0
def lose_game(secret_word):
    """run to generate losing end game code"""
    print("Sorry, you ran out of guesses. The word was %s." %secret_word) 
    
#run when is_word_guessed(secret_word, letters_guessed) returns True
def win_game(secret_word, guesses_remaining):
    """run to generate wining end game code"""
    score= guesses_remaining * len("".join(set(secret_word)))
    print("Congratulations, you won!")
    print("Your total score for this game is: %s" %score)   

def next_round (warnings_remaining, guesses_remaining, available_letters):
    """plays out a standard round. returns guessed_letter"""
    print("You have %d warnings left." %warnings_remaining)
    print("You have %d guesses left." %guesses_remaining)
    print("Available letters: %s" %(available_letters))
    print (get_guessed_word(secret_word, letters_guessed))
    print("Please guess a letter:")
    guessed_letter= input()
    return guessed_letter