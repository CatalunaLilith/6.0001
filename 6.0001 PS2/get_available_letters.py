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

