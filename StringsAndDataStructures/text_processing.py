# Cameron Cheng

# CS 3035-01
# This file takes the text file that the user chooses and returns a list of the
# words in that file that is now sorted in alphabetical order
# This file also counts the raw amount of words in the text file

import string

def textNoPunc(fileName):
    text = open(fileName, 'r', encoding='utf-8')
    textStr = text.read()
    translation_table = textStr.maketrans(dict.fromkeys(string.punctuation + '“”’‘' ))

    noPunctuation = textStr.translate(translation_table)
    finaltext = noPunctuation.lower()

    textList = finaltext.split()
    textList.sort()

    return textList


def wordCount(fileName):
    text = open(fileName, 'r', encoding='utf-8')

    textStr = text.read()
    translation_table = textStr.maketrans(dict.fromkeys(string.punctuation + '“”’‘'))

    noPunctuation = textStr.translate(translation_table)
    finaltext = noPunctuation.lower()

    textList = finaltext.split()

    words = len(textList)

    return words



