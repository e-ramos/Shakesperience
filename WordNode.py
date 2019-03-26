#!

__author__ = "E. A. Ramos"
__email__ = "ear@ku.edu"

"""
            Class Necessary for Prefix Data Structure
"""
###########################################################
## Creating Data Struct: Word Node
###########################################################

class WordNode:
    def __init__(self, name, freq):
        self.name = name #String containing name
        self.freq = freq #Frequency of Word (Relative to Last Root)
        self.next = {} #Dictionary of the next available words and their frequencies
        self.nextFive = [] #Ordered tuple of the top 5 next words
        
        #Flagging the Period
        if self.name == "FULLSTOP":
            self.theend = 1
        else:
            self.theend = 0 