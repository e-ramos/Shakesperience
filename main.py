#!

__author__ = "E. A. Ramos"
__email__ = "ear@ku.edu"

"""
            Shakesperience: Hidden Markov Poetry

            Creates a Trie of Order One Markovity as a model for the english language. 
            Then allows the user to generate complete phrases using this model.

            Github:
            
            Note: Expects data to be extracated in  '~/Data' relative to the path of this file. 
"""



import time, sys, os
import pandas as pd
import numpy as np
import string
import pickle
#Importing Regular Expressions
import re
#Importing RNG
import random
#Importing Non-Built in
import mfunc
import TrainModel
from WordNode import WordNode


## Init

mfunc.printtitlescreen()

## Check for Stored Model

if os.path.isfile('Data/WordList.pkl'):

    print ''
    print 'We Have Detected a Stored Model and Will Load it By Default'
    print 'Pick Menu Option 3 To Overwrite this Model (THIS CANNOT BE UNDONE)'
    print ''
    time.sleep(3)
else:
    print ''
    print 'No Model Found in Files!'
    print 'Training a default weak model'
    print 'Use Menu option 3 to improve (can be slow)'
    print ''
    time.sleep(3)
    WordList = TrainModel.ShakesTrain(1000, 5)
    mfunc.savemodel(WordList)


## MAIN LOOP
while True:
    ## Loading Present Model:

    with open('Data/WordList.pkl', 'rb') as f:
        WordList = pickle.load(f)

    print('Model Loaded')
    mfunc.topfive(WordList)
    time.sleep(3)


    ## Main Menu

    mfunc.printMenu()
    selection = raw_input('Select a Number [1-3]:')

    ## 

    if selection == '3':
        mfunc.clearscreen()
        print('Training New Model:')
        print('How many lines would you like to use?')
        linelen = raw_input('The Maximum is 111396 :')
        print('')
        print('How many Trie Branches would you like?')
        branches = raw_input('(More = higher variability; 5 is default):')

        WordList=TrainModel.ShakesTrain(int(linelen),int(branches))
        mfunc.savemodel(WordList)

    elif selection == '2':
        print('Tweaking the model for more variability')
        print('')
        print('How many Trie Branches would you like?')
        branches = raw_input('(More = higher variability; 5 is default):')
        mfunc.shakebranches(int(branches), WordList)

    elif selection == '1':
        ## Printing Sentence
        while True:
            mfunc.clearscreen()
            print('You Can Always Input "1" to return to menu:')
            seedstr =raw_input('Input a partial sentence to "Shakespearify" \n:')
            if seedstr == '1':
                break
            else:
                seedword = seedstr.split()[-1]

                #Checking input
                if seedword in WordList:

                    outstr = seedstr
                    CurrWord = seedword
                    while True:

                        #Randomizing amongst the most likely
                        nextind = random.randint(0, len(WordList[CurrWord].nextFive)-1)

                        nextword = WordList[CurrWord].nextFive[nextind]

                        if nextword == 'FULLSTOP':
                            outstr = outstr + "."
                            break

                        CurrWord = nextword
                        outstr = outstr +' '+nextword

                    #Printing
                    print ''
                    print(outstr)
                    print('')
                    raw_input('Press Any Key To Continue:')

                else:
                    print ''
                    print "Sorry, that phrase is not Elizabethan enough to continue,"
                    print "TRY AGAIN with a different phrase"
                    print "Here's a random one:"
                    print ''

                    seedword = random.choice(list(WordList.keys()))

                    outstr = seedword
                    CurrWord = seedword
                    while True:

                        #Randomizing amongst the most likely
                        nextind = random.randint(0, len(WordList[CurrWord].nextFive)-1)

                        nextword = WordList[CurrWord].nextFive[nextind]

                        if nextword == 'FULLSTOP':
                            outstr = outstr + "."
                            break

                        CurrWord = nextword
                        outstr = outstr +' '+nextword

                    #Printing
                    print(outstr)
                    print('')
                    raw_input('Press Any Key To Continue:')







