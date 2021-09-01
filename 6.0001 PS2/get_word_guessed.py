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
    for char in secret_word:
        if char in letters_guessed:
            var_index = 0
            guessed_word_list [var_index] = char
            var_index += 1
    #convert list to string
    guessed_word = ""
    for ele in guessed_word_list:
        guessed_word += ele
    return guessed_word
    

print(get_guessed_word("cats", ["c", "t", "a"]))
