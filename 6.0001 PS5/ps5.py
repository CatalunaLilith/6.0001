# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz
import re


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        """innitializes a new class NewsStory with five parameters
        globally unique identifier (GUID) - a string
        title - a string
        description - a string
        link to more content - a string
        pubdate - a datetime
        """
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
    def get_guid(self):
        """getter for the guid parameter"""
        return self.guid
        
    def get_title(self):
        """getter for the title parameter"""
        return self.title
        
    def get_description(self):
        """getter for the description parameter"""
        return self.description
        
    def get_link(self):
        """getter for the link parameter"""
        return self.link
        
    def get_pubdate(self):
        """getter for the pubdate parameter"""
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2

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
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        if self.is_phrase_in(story):
            should_alert = True
        else:
            should_alert = False 
        return should_alert
 
# Problem 3

class TitleTrigger(PhraseTrigger):
    """inherits is_phrase_in(self, text), is not case sensitive"""
    def __init__(self, phrase):
        """takes in a string phrase. is not case sensite. 
        phrase  may not contain punctuation. 
        phrase may contain spaces"""
        self.phrase = phrase.lower()
        
    def is_phrase_in_title(self, ANewsStory):
        """takes in an object of class NewsStory, 
        fires True when a news item's title contains a given phrase """
        title = ANewsStory.get_title()
        self.text = title 
        phrase_is_in_title = self.is_phrase_in(title)
        return phrase_is_in_title
      
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.is_phrase_in_title(story)


# Problem 4
class DescriptionTrigger(PhraseTrigger):
    """inherits is_phrase_in(self, text), is not case sensitive"""
    def __init__(self, phrase):
        """takes in a string phrase. is not case sensite. 
        phrase  may not contain punctuation. 
        phrase may contain spaces"""
        self.phrase = phrase.lower()
        
    def is_phrase_in_description(self, ANewsStory):
        """takes in an object of class NewsStory, 
        fires True when a news item's title contains a given phrase """
        description = ANewsStory.get_description()
        self.text = description
        phrase_is_in_description = self.is_phrase_in(description)
        return phrase_is_in_description
      
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        return self.is_phrase_in_description(story)

# TIME TRIGGERS

# Problem 5

class TimeTrigger(Trigger):
    """inherits evaluate()"""
    def __init__(self, datetime_string):
        """ Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
        Converts time from string to a datetime and saves it as an attribute."""
        self.trigger_time = datetime.strptime(datetime_string, "%d %b %Y %H:%M:%S")
        self.trigger_time = self.trigger_time.astimezone(pytz.timezone('EST')) 


# Problem 6

class BeforeTrigger(TimeTrigger):
    """inherits __init(self, datetime_string)"""
    def evaluate(self, ANewsStory):
        """fires True if trigger_time is before pubdate of a NewsStory object"""
        pubdate = ANewsStory.get_pubdate()
        pubdate = pubdate.astimezone(pytz.timezone('EST')) 
        if self.trigger_time > pubdate:
            story_is_before = True
        else:
           story_is_before = False
        return story_is_before 
    
class AfterTrigger(TimeTrigger):
    """inherits __init(self, datetime_string)"""
    def evaluate(self, ANewsStory):
        """fires True if trigger_time is after pubdate of a NewsStory object"""
        pubdate = ANewsStory.get_pubdate()
        pubdate = pubdate.astimezone(pytz.timezone('EST')) 
        if self.trigger_time < pubdate:
            story_is_before = True
        else:
            story_is_before = False
        return story_is_before 
    

"""If you've never seen string.punctuation before, do that now
string.split()
string.join()
string.replace
string.lower()
string.upper()
"""
# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, aTrigger):
        """takes another trigger object as a parameter, stores as attribute"""
        self.aTrigger = aTrigger
        
    def evaluate(self, ANewsStory):
        """returns a boolean, the inverse of aTrigger's evaluate function
        given a trigger T and a news item x , the output of the NOT trigger'sevaluate method should be equivalent to not T.evaluate(x)
        """
        inversed_trigger = not self.aTrigger.evaluate(ANewsStory)
        return inversed_trigger
        

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        """takes two trigger objects as parameters,and stores them as attributes"""
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, ANewsStory):
        """fires True if evaluate of trigger1 and evaluate of trigger 2 are both true, else fires False """
        if self.trigger1.evaluate(ANewsStory) == True and self.trigger2.evaluate(ANewsStory) == True:
            and_trigger = True
        else:
            and_trigger = False        
        return and_trigger

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        """takes two trigger objects as parameters,and stores them as attributes"""
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, ANewsStory):
        """fires True if evaluate of trigger1 and/or evaluate of trigger2 is True.
        fires False if evaluate of trigger1 and evaluate of trigger2 are both False """
        or_trigger = False
        if self.trigger1.evaluate(ANewsStory) == True:
            or_trigger = True
        if self.trigger2.evaluate(ANewsStory) == True:
            or_trigger = True
        return or_trigger


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    stories_list = stories
    filtered_stories_list = []
    for aNewsStory in stories_list:
        for atrigger in triggerlist:
            if atrigger.evaluate(aNewsStory) == True:
                filtered_stories_list.append(aNewsStory)
    return filtered_stories_list

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    # line is the list of lines that you need to parse and for which you need to build triggers
    lines_list = lines.copy()
    #build ADD_list, remove ADD elements from lines_list
    ADD_list = []
    i=0
    while i < len(lines_list):
        if "ADD" in lines_list[i]: 
           ADD_holder = lines_list.pop(i)
           ADD_holder = ADD_holder.split(",")
           for elem in ADD_holder:
               if elem != 'ADD':
                   ADD_list += [elem]
        i += 1    
    #build trigger_dict
    trigger_dict = {}
    for elem in lines_list:
        trigger_holder = elem.split(",") + [""]
        trigger_dict[trigger_holder[0]] = (trigger_holder[1], trigger_holder[2], trigger_holder[3])
    trigger_list = []
    for trigger in ADD_list:
        trigger_holder = trigger_dict[trigger]
        if trigger_holder[0] == 'AND':
            trigger_list.append(AndTrigger(trigger_holder[1], trigger_holder[2]))
        elif trigger_holder[0] == 'TITLE':
            trigger_list.append(TitleTrigger(trigger_holder[1]))
        elif trigger_holder[0] == 'DESCRIPTION':
            trigger_list.append(DescriptionTrigger(trigger_holder[1]))
        elif trigger_holder[0] == 'AFTER':
            trigger_list.append(AfterTrigger(trigger_holder[1]))
        elif trigger_holder[0] == 'BEFORE':
            trigger_list.append(BeforeTrigger(trigger_holder[1]))
        elif trigger_holder[0] == 'OR':
            trigger_list.append(OrTrigger(trigger_holder[1], trigger_holder[2]))
        elif trigger_holder[0] == 'NOT':
            trigger_list.append(NotTrigger(trigger_holder[1]))
        else:
            print("Trigger type not recognised, please check your input")
    return trigger_list


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)



if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()
