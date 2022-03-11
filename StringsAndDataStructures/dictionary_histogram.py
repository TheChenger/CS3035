# Cameron Cheng

# CS 3035-01
# This file does the same thing as the list file but instead of making a list of
# tuples, we make a dictionary that has the word and its key is the amount of
# times the word appears in the list. Then it prints out the pairs of values
# line by line

def wordDictionary(wordList):

    dict = {}

    duplicate_list = []

    for x in wordList:
        if x in duplicate_list:
            pass
        else:
            duplicate_list.append(x)
            wordCount = wordList.count(x)
            dict[x] = wordCount

    for x, y in dict.items():
        print(x,y)