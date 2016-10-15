'''

Made by Christopher Geiger on 10/14/2016

Notes:
Doesn't allow any special characters (including punctuation)
Crashes if spaces are added to the end of an entered morse code

'''

import string
import sys


alphaString = string.ascii_lowercase + ' '

alfList = list(alphaString)

MORSELIST = ['.-', '-...' , '-.-.' , '-..' , '.' , '..-.' , '--.' , '....' , '..' , '.---' , '-.-' , '.-..' , '--' , '-.' , '---' , '.--.' , '--.-' , '.-.' , '...' , '-' , '..-' , '...-' , '.--' , '-..-' , '-.--' , '--..', '/']

morseDic = dict(zip(alfList, MORSELIST))
engDic = dict(zip(MORSELIST, alfList))

print(str(morseDic))
print(str(engDic))


def acceptInput():
    clear()
    usr = input('Press 1 for English to Morse or 2 for Morse to English: ')
    if usr == '1': toMorse()
    elif usr == '2': toEnglish()
    else:
        print('Input error, try again.')
        acceptInput()

def toMorse():
    clear()
    word = input('Give me some text to translate to morse: ')
    for c in word:  
        print(str(morseDic[str(c)])+' ', end = '')

    print()
    usrinput = input('Done. Go again? Y/N ')
    if usrinput.lower() == 'y':
        acceptInput()
    else: sys.exit()


def toEnglish():
    clear()
    #TODO: Fix crash when ' ' is at the end of a string
    morse = input('Give me some text to translate to english: ')
    usrMorseList = morse.split(' ')
    for morseCode in usrMorseList:
        print(str(engDic[morseCode]).upper(), end='')
    
    print()
    usrinput = input('Done. Go again? Y/N ')
    if usrinput.lower() == 'y':
        acceptInput()
    else: sys.exit()

def clear():
    print('\n'*100)

acceptInput()
#TODO: Add special inputs
#TODO: Make functions flow more intuitively
