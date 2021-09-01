# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 12:41:08 2020

@author: Barbara
"""

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def get_word_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are the letter values. 
    Note: only stores letter values once, even if letter is repeated

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    worddict = {}
    for char in sequence:
        worddict[char] = worddict.get(char,SCRABBLE_LETTER_VALUES[char]) 
    return worddict
    
get_word_dict("kittens")    