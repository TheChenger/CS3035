# Cameron Cheng

# CS 3035-01
# This file makes a list of Tuples, which means it is basically a list that
# is full of pairs of values. In this case it is the word and how many times
# that word appeared in the text file. Then it prints out each pair of values.
def listOfTuples(wordList):

    wordCountTupleList = []

    duplicate_list = []
    for x in wordList:
        if x in duplicate_list:
            pass
        else:
            duplicate_list.append(x)
            wordCount = wordList.count(x)
            wordCountTupleList.append((x,wordCount))
    for x in wordCountTupleList:
        print(x)






