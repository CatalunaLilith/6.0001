# Problem Set 4B
# Name: Pat
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'


class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        valid_words = []
        text_list =  list(text.split(" "))
        for word in text_list:
             if is_word(load_words(WORDLIST_FILENAME), word):
                 valid_words += [word]
        self.valid_words = valid_words
        
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return list.copy(self.valid_words)

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''        
        #build base_alphabet_dict
        base_alphabet_dict = {"a":1, "b":2,"c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26, "A":1, "B":2,"C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10, "K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}    
        
        shifted_alphabet_dict = base_alphabet_dict.copy()         
        for key in base_alphabet_dict:
             shifted_letter_value = ((int(base_alphabet_dict[key])) +shift) %26
             if shifted_letter_value == 0:
                 shifted_letter_value = 26
             #get key of  base_alphabet_dict based on shifted_letter_value  
             list_at_shifted_key_at_shifted_value = [key for key, value in base_alphabet_dict.items() if value == shifted_letter_value]

             if key.isupper():
                  value_at_shifted_key_at_shifted_value = list_at_shifted_key_at_shifted_value[1]
             else:     
                  value_at_shifted_key_at_shifted_value = list_at_shifted_key_at_shifted_value[0]
             shifted_alphabet_dict[key]  = value_at_shifted_key_at_shifted_value    

        return shifted_alphabet_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        #replace letters in self.message_text as per build_shift_dict(shift)
        shifted_alphabet_dict = self.build_shift_dict(shift)
        shifted_text = ""
        for char in self.message_text:
            if char in string.punctuation:
                 shifted_text += char
            elif char == " ":
                 shifted_text += char
            #replace char with shifted_alphabet_dict[char]
            else:
                 shifted_text += shifted_alphabet_dict[char]        
        return shifted_text
        

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        #inherits:
            #self.message_text (string, determined by input text)
            #self.valid_words (list, determined using helper function load_words)
        Message.__init__(self, text)          
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)

        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift 

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy() 

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self,shift)
        self.message_text_encrypted = Message.apply_shift(self,shift)
    

class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #inherits:
            #self.message_text (string, determined by input text)
            #self.valid_words (list, determined using helper function load_words)
        Message.__init__(self, text)  
              
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        word_list = load_words(WORDLIST_FILENAME)
        #testing to find best decryption
        shift = 1
        valid_words_of_message_text_decrypted_dict = {}
        while shift <= 26:
             valid_words_of_message_text_decrypted_list = []
             message_text_decrypted_string = self.apply_shift(26-shift)
             message_text_decrypted_list = message_text_decrypted_string.split(" ")
             for word in message_text_decrypted_list:
                 if is_word(word_list, word):
                      valid_words_of_message_text_decrypted_list += [word]     
         
             valid_words_of_message_text_decrypted_dict[shift] = (valid_words_of_message_text_decrypted_list, len(valid_words_of_message_text_decrypted_list)) 
             shift += 1
             
        lenghts_of_valid_words_of_message_text_decrypted_list = []
        for key in valid_words_of_message_text_decrypted_dict:
            lenghts_of_valid_words_of_message_text_decrypted_list += [valid_words_of_message_text_decrypted_dict.get(key)[1]]
                             
        max_lenght_valid_words = max(lenghts_of_valid_words_of_message_text_decrypted_list)
        #if max() is tied, will return the first maximal result
        shift_at_max_lenght_valid_words_temp = [key for key, value in valid_words_of_message_text_decrypted_dict.items() if value[1] == max_lenght_valid_words]
        shift_at_max_lenght_valid_words = shift_at_max_lenght_valid_words_temp[0]
        message_at_max_lenght_valid_words = self.apply_shift(26-shift_at_max_lenght_valid_words)

        return (shift_at_max_lenght_valid_words, message_at_max_lenght_valid_words)
                     
"""
if __name__ == '__main__':

    #test case (PlaintextMessage)
    plaintext1 = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext1.get_message_text_encrypted())
    print("--------------")
    
    plaintext2 = PlaintextMessage('cats are perfect', 2)
    print('Expected Output: ecvu ctg rgthgev')
    print('Actual Output:', plaintext2.get_message_text_encrypted())
    print("--------------")

    #test case (CiphertextMessage)
    ciphertext1 = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext1.decrypt_message())
    print("--------------")
    
    ciphertext2 = CiphertextMessage("cnn mkvvgpu ctg ecvu")
    print('Expected Output:', (2, 'all kittens are cats'))
    print('Actual Output:', ciphertext2.decrypt_message())
    print("--------------")
"""
secret_story_message = CiphertextMessage(get_story_string())
decrypted_tuple_of_secret_story_message = secret_story_message.decrypt_message()


best_shift_for_secret_story = decrypted_tuple_of_secret_story_message[0]
unencrypted_secret_story = decrypted_tuple_of_secret_story_message[1]

print(best_shift_for_secret_story)
print(unencrypted_secret_story)
