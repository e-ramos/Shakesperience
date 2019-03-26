#!

__author__ = "E. A. Ramos"
__email__ = "ear@ku.edu"

"""
            Contains functions. See main.py
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

'''
#########################

#Functions included:

    topfive()

    savemodel()

    shakebranches()

    printMenu()

    clearscreen()

    printtitlescreen()

    myPB()
    



'''

def topfive(WordList):
    # Printing Top Words
    itera = 0
    numprint = 5
    print ' '
    print "Top %s Most Frequent Words:" %(numprint)
    print('')
    for key, value in sorted(WordList.iteritems(), key=lambda (k,v): (-v.freq,k)):
        
        if key == "FULLSTOP":
            continue
            
        print "%s: %s" % (key, value.freq)
        
        ## Print First Numprint
        itera += 1
        if(itera == numprint):
            break

def savemodel(WordList):
    if os.path.isfile('Data/WordList.pkl'):
        os.remove("Data/WordList.pkl")
        print('File Overwritten!')
    f = open("Data/WordList.pkl","wb")
    pickle.dump(WordList,f,protocol=pickle.HIGHEST_PROTOCOL)
    f.close()

   ## Reducing Probability Space
def shakebranches(branches, WordList):
    for word in WordList:
        itera = 0
                
        #Storing only the top 5 words after any word
        for key, value in sorted(WordList[word].next.iteritems(), key=lambda (k,v): (-v,k)):
            WordList[word].nextFive.append(key)
            
            #Iterate
            itera += 1
            if(itera == branches):
                break

## Main Menu
def printMenu():
    clearscreen()

    print 'Main Menu:'
    print '---------------------'
    print '| 1. Vocabulate     |'
    print '| 2. Tweak Model    |'
    print '| 3. Train Model    |'
    print '---------------------'


###########################################################
## Creating Timer
###########################################################

def myPB (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '#'):

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)

    sys.stdout.flush()
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    

    # Print New Line on Complete
    if iteration == total: 
        print()            
###########################################################

#### Clear Screen

def clearscreen():
    os.system('cls')


##### Print title

def printtitlescreen():

    clearscreen()
    sys.stdout.write(\
    "     _,--._.-,    S             \n"+\
    "    /\_--,\_ )     H            \n"+\
    ".-.) _; ^'_/ (.;    A           \n"+\
    " \ \'       \/  )     K          \n"+\
    "  |.'-.  _.'|-'       E         \n"+\
    " <_`-'\_'_.' /         S        \n"+\
    "  `'-._( \ \            P       \n"+\
    "    ___   \ \,      ___  E      \n"+\
    "    \ .'-. \ \   .-'_. /  R     \n"+\
    "     '._' '.\ \/.-'_.'     I    \n"+\
    "        '--``\ ('--'        E   \n"+\
    "              \ \            N  \n"+\
    " By:          `\ \,           C \n"+\
    " E.A. Ramos     \ |            E\n")


##### 