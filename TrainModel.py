#!

__author__ = "E. A. Ramos"
__email__ = "ear@ku.edu"

"""
            Contains HMM Model Trainer. See main.py
"""

import time, sys, os
import pandas as pd
import numpy as np
import string, os 
#Importing Regular Expressions
import re
#Importing RNG
import random
#Importing Non-Built in
import mfunc
import WordNode 
import mfunc
from WordNode import WordNode
from mfunc import myPB 


def ShakesTrain(lenlines, branches):

    mfunc.printtitlescreen()

    # Loading All the Text
    curr_dir = ''
    DF = pd.read_csv(curr_dir + 'Data/Shakespeare_data.csv')

    lines = [h for h in DF.PlayerLine]
    
    print ' '
    print('There are %s Lines in the file given' % len(lines))
    print ' '

    # Define Punctuation, omitting period (we want this to be a "word")
    punct=re.sub(r"[.'-,]",'',string.punctuation)

    # Split database into lines with no punctuation

    def lean_text(txt):
        txt = "".join(v for v in txt if v not in punct).lower()
        txt = txt.encode("utf8").decode("ascii",'ignore')
        txt = str(txt)
        txt = " "+txt #Adding space to front to delimit text
        txt = txt.replace(".", " FULLSTOP ") #Adding flag in place of period
        return txt 

    #Randomizing Line Order
    
    lines = [random.choice(lines) for x in lines]

    alllines = [lean_text(x) for x in lines]    
    
    
    # Split Lines into Words
    

    WordBase = "".join(alllines[:lenlines])

    ###########################################################
    ## Counting Words and Training Model
    ###########################################################

    # Using a key-value pair stored in a dictionary
    # Here a KEY is a word encountered at least once
    # A VALUE is an object representing the word

    WordList = {} #Dictionary to store words

    ## Populating dictionary

    #String Structure to find
    match_pattern = re.findall(r'\b[\S]{1,15}', WordBase) # Finds all words up to len 15
    for word in match_pattern:
        #Counting
        #First Iteration
        CurrWord = WordList.get(word,0)
        if CurrWord == 0:
            #Object instantiation
            WordList[word] = WordNode(word, 1)
        else:
            CurrWord.freq = CurrWord.freq + 1

    #Print number of words found
    TotWords = len(WordList)
    print "Unique Words in Model: %s" %(TotWords)
    print ' '

    ## Creating First Order Markov Model
    # Unfortunately have to iterate again, this is a poor implementation...
    # but, regex is probably faster than any in place file reader I could come up with
    # quickly.

    #Timing
    StartTimer = time.time()
    sys.stdout.flush()
    #Trick Progress Bar
    myPB(0, TotWords, prefix = 'Training Status:', suffix = 'Complete', length = 50)


    # Model Building

    for x, word in enumerate(WordList):
        if word == "FULLSTOP": #Periods have no words after them
            continue
            
        searchstring = r'(?<=\b%s\s)(\b[\S]{1,15})' % word
        match_pattern2 = re.findall(searchstring, WordBase)
        for phrase in match_pattern2:
            DictCopy = WordList[word].next #Copying Internal Dictionary
            PhraseCount = DictCopy.get(phrase,0) #Getting the "next word" Frequency from Dict
            DictCopy[phrase] = PhraseCount + 1 #Incrementing frequency of "next word"
            WordList[word].next = DictCopy #Replacing Dictionary into Object

        myPB(x + 1, TotWords, prefix = 'Training Status:', suffix = 'Complete', length = 50)       
        
    EndTime = time.time()

    # Printing Timer
    print ' '
    print('It took %s seconds to create a model with %s Unique Words and %s Lines of Text')\
    % (int(EndTime-StartTimer),TotWords,lenlines)

    ## Reducing Probability Space

    for word in WordList:
        itera = 0
                
        #Storing only the top 5 words after any word
        for key, value in sorted(WordList[word].next.iteritems(), key=lambda (k,v): (-v,k)):
            WordList[word].nextFive.append(key)
            
            #Iterate
            itera += 1
            if(itera == branches):
                break
  


    ## Printing Affirm

    mfunc.clearscreen()

    print ''
    print '################# Model Trained ##################'
    print 'Returning to Main Menu'
    return WordList

    # End Training Function