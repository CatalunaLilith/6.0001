
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
        else:    
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


def next_round (warnings_remaining, guesses_remaining, available_letters,secret_word, letters_guessed):
    """plays out a standard round. returns tuple with guessed_letter at index 0, availables_letters at index 1"""
    availables_letters = get_available_letters(letters_guessed)
    print("------------")
    print("You have %d warnings left." %warnings_remaining)
    print("You have %d guesses left." %guesses_remaining)
    print("Available letters: %s" %(available_letters))
    print (get_guessed_word(secret_word, letters_guessed))
    print("Please guess a letter:")
    guessed_letter= input()
    return guessed_letter, availables_letters

    
               

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
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
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #initialize variables
    guesses_remaining=6
    available_letters="abcdefghijklmnopqrstuvwxyz"
    letters_guessed=""
    guesses_remaining=6
    warnings_remaining=3

    print("Loading word list from file...")
    print("55900 words loaded.")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is %s letters long." %(len(secret_word)))

    lower_alphabet = ["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper_alphabet = ["A","B","C", "D", "E", "F", "G", "H", "I", "J", "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    
    lower_alphabet_string = "abcdefghijklmnopqrstuvwxyz"
    
    round_result = next_round (warnings_remaining, guesses_remaining, available_letters,secret_word, letters_guessed)
    guessed_letter = round_result[0]
    available_letters = round_result[1]
    letters_guessed= letters_guessed + guessed_letter
    
    if guessed_letter in upper_alphabet : 
        #converts to lowercase
        guessed_letter= str.lower("guessed_letter")
    
    if guessed_letter in lower_alphabet :
        if guessed_letter in available_letters:
            letters_guessed= letters_guessed + guessed_letter
            did_win = is_word_guessed(secret_word, letters_guessed)
            if did_win == True:
                 win_game(secret_word, guesses_remaining)
            if did_win == False:
                #good guess 
                if guessed_letter in secret_word:
                   round_result = next_round (warnings_remaining, guesses_remaining, available_letters,secret_word, letters_guessed)
                   guessed_letter = round_result[0]
                   available_letters = round_result[1]
                   letters_guessed= letters_guessed + guessed_letter
                #bad guess
                else:
                   if guessed_letter in ["a","e","i", "o", "u"] : 
                       guesses_remaining -= 2
                   else :
                       guesses_remaining -= 1
                round_result = next_round (warnings_remaining, guesses_remaining, available_letters,secret_word, letters_guessed)
                guessed_letter = round_result[0]
                available_letters = round_result[1]
                letters_guessed= letters_guessed + guessed_letter
                
        else: #if letter already guessed
            warnings_remaining -= 1
            if warnings_remaining <= 0:
                guesses_remaining -= 1
            print("Oops! You've already guessed that letter.")
            if guesses_remaining == 0:
                lose_game(secret_word)
            else:
                round_result = next_round (warnings_remaining, guesses_remaining, available_letters,secret_word, letters_guessed)
                guessed_letter = round_result[0]
                available_letters = round_result[1]
                letters_guessed= letters_guessed + guessed_letter     
    else:
        warnings_remaining -= 1
        if warnings_remaining <= 0:
            guesses_remaining -= 1
        print("Oops! That is not a valid letter.") 
        if guesses_remaining == 0:
                lose_game(secret_word)
        else:
            round_result = next_round (warnings_remaining, guesses_remaining, available_letters,secret_word, letters_guessed)
            guessed_letter = round_result[0]
            available_letters = round_result[1]
            letters_guessed= letters_guessed + guessed_letter

hangman("cats")        