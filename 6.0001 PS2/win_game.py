# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 12:19:37 2020

@author: Barbara
"""
#score=guesses_remaining * unique letters in secret_word (not len(secret_word))


def win_game(secret_word, guesses_remaining):
    """run to generate win game code"""
    score= guesses_remaining * len("".join(set(secret_word)))
    print("Congratulations, you won!")
    print("Your total score for this game is: %s" %score)
    
  