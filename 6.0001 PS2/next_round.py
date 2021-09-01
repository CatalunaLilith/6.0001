# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:31:11 2020

@author: Barbara
"""
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

secret_word="cats"
letters_guessed=""

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

"""to  run a round
round_result = next_round (warnings_remaining, guesses_remaining, available_letters,secret_word, letters_guessed)
guessed_letter = round_result[0]
available_letters = round_result[1]
letters_guessed= letters_guessed + guessed_letter
                   """

next_round (3, 6, "abcdefghijklmnopqrstuvwxyz","cats", "a")

#variable to store after next_round: available_letters, letters_guessed
               