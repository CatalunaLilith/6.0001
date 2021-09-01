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
        self.text = text.lower()
        alpha_text = ""
        for char in self.text:
            if char not in string.punctuation:
                alpha_text += char
        if self.phrase in alpha_text:
                phrase_is_in_text  = True
        else:
            if " " in self.phrase:
                spaceless_phrase = (self.phrase).replace(" ","")
            print (spaceless_phrase)
            if spaceless_phrase in alpha_text:
                phrase_is_in_text  = True
            else:    
                phrase_is_in_text = False
        return phrase_is_in_text
    
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        if self.is_phrase_in(story):
            should_alert= True
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
        self.phrase = phrase.lower ()
        
    def is_phase_in_title(self, ANewsStory):
        """takes in an object of class NewsStory, 
        or
        takes in an object, the string title from an object of class NewsStory
        that fires when a news item's title contains a given phrase """
        title = aNewsStory.get_title 
        #TODO figure out to recognise that NewsStory is a class NewsStory
        phrase = self.phrase
        phrase_is_in_title = phrase.is_phrase_in(title)
        return phrase_is_in_title
            
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        if self.is_phrase_in_title(NewsStory):
            should_alert= True
        else:
            should_alert = False 
        return should_alert

#TODO test until TITLETRigger works
test_newstory = NewsStory("", "there have been no purple cows found in this apartment", "", "", "")

#test_titletrigger = TitleTrigger("purple cow")

#print(test_titletrigger.is_phase_in_title(test_newstory))
#print(test_titletrigger.evaluate(test_newstory))


"""If you've never seen string.punctuation before, do that now
string.split()
string.join()
string.replace
string.lower()
string.upper()
"""

# Problem 4
# TODO: DescriptionTrigger




# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

# Problem 6
# TODO: BeforeTrigger and AfterTrigger


# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger

# Problem 8
# TODO: AndTrigger

# Problem 9
# TODO: OrTrigger


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    return stories



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
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers

    print(lines) # for now, print it so you see what it contains!



"""
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
        # triggerlist = read_trigger_config('triggers.txt')
        
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

"""