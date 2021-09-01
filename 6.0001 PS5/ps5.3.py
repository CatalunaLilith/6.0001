import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re

class PhraseTrigger():
    def __init__(self, phrase):
        """takes in a string phrase. is not case sensite. 
        phrase  may not contain punctuation. 
        phrase may contain spaces"""
        self.phrase = phrase.lower ()
        
    def is_phrase_in(self, text):
        """takes a string string text. 
        evaluates True if phrase is in text. else evaluates False
        not case sensitive"""
        phrase_is_in_text = False
        self.text = text.lower()
        text = self.text.lower()
        text_list = re.split("!|'|\.|#|\$|%|&|\+|\"|'|,| |\(|\)|\*|-|/|:|;|<|=|>|\?|@|\[|]|^|_|`|{|}|~|\|", text)
        for elem in text_list.copy():
            if elem == "":
                text_list.remove("")
        phrase_list = re.split("!|'|\.|#|\$|%|&|\+|\"|'|,| |\(|\)|\*|-|/|:|;|<|=|>|\?|@|\[|]|^|_|`|{|}|~|\|", self.phrase)        
        for elem in  phrase_list.copy():
            if elem == "":
                 phrase_list.remove("")
        i=0
        j=0
        while i < len(text_list)-1 :
            if phrase_list[j] == text_list[i]:
                while j < len(phrase_list)-1:
                    if phrase_list[j+1] == text_list[i+1]:
                        phrase_is_in_text =True
                    j += 1    
            i += 1
        return phrase_is_in_text
    
    
    #take in text string, make it lowercase
        #split text string into text_list with split() (whitespace and punction as split points)
        #take phrase from PhraseTrigger object, split() into phrase_list
        #what happens if i try to split() into one item>
        #iterate over text_list, seeing if phrase_list[0] in is text_list
            #if phrase_list[0] in is text_list test if phrase_list[0+1] is next in text_list
                #if entirety phrase_list is found consecutively
                    #phrase_is_in_text == True
                #else nothing (returns to check next elem of text_list
            #if phrase_list not found 
                #phrase_is_in_text == False   