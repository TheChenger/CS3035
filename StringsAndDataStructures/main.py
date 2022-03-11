# Cameron Cheng

# CS 3035-01
# https://calstatela.instructuremedia.com/embed/a7cb626a-3457-4fc7-bc2d-afcdb3842210
# This main file gives the user the option of which text file they would
# like to get processed. In addition to that we also time the list and dictionary
# files to see which one is faster.
import text_processing
import list_histogram
import dictionary_histogram
import timeit


if __name__ == "__main__":
    print("we all good")
    print("These are the different file options for you to process")
    print("1: Utopia by Thomas More")
    print("2: Autobiography of Ben Franklin by Ben Franklin")
    print("3: The Odyssey by Homer")


    n = int(input('Enter the file number you would like to process: '))
    if n == 1:
        text1 = "UtopiaText.txt"
        words = text_processing.textNoPunc(text1)
        start1 = timeit.default_timer()
        print(list_histogram.listOfTuples(words))
        end1 = timeit.default_timer()
        start2 = timeit.default_timer()
        print(dictionary_histogram.wordDictionary(words))
        end2 = timeit.default_timer()

        print('Total Word Count' , text_processing.wordCount(text1))
        print('List total time: ' , end1-start1)
        print('Dictionary total time: ' ,end2-start2)

    elif n == 2:
        text1 = "BenFranklin.txt"
        words = text_processing.textNoPunc(text1)
        start1 = timeit.default_timer()
        print(list_histogram.listOfTuples(words))
        end1 = timeit.default_timer()
        start2 = timeit.default_timer()
        print(dictionary_histogram.wordDictionary(words))
        end2 = timeit.default_timer()

        print('Total Word Count', text_processing.wordCount(text1))
        print('List total time: ', end1 - start1)
        print('Dictionary total time: ', end2 - start2)
    elif n == 3:
        text1 = "TheOdyssey.txt"
        words = text_processing.textNoPunc(text1)
        start1 = timeit.default_timer()
        print(list_histogram.listOfTuples(words))
        end1 = timeit.default_timer()
        start2 = timeit.default_timer()
        print(dictionary_histogram.wordDictionary(words))
        end2 = timeit.default_timer()

        print('Total Word Count', text_processing.wordCount(text1))
        print('List total time: ', end1 - start1)
        print('Dictionary total time: ', end2 - start2)
