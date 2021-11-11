# course: Object-oriented programming, year 2, semester 1
# academic year: 202122
# author: B. Schoen-Phelan
# date: 14-10-2021
# purpose: Lab 4

import sys

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")
        if self.user_input.isdigit():
            sys.exit("We would have needed a word not a number")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        word_count = 0 #Number of words in the original sentence.
        scrambled_word = 'Empty' #Stores scrambled version of word during while loop.

        sentence_list = list(self.user_input.split(" ")) #Convert the input into a list, split at each space.
        print(sentence_list) #Debug, display the list version of the sentence.

        word_count = len(sentence_list) #Store the number of words in the sentence.
        word_count2 = 0

        #Go through each word and put into a list.
        #Scramble the word and output it.
        #Original list of words is left unchanged.
        while word_count2 < word_count: #From position 0 up to last.
            print("Word Count: ",word_count2) #Debug, current iteration word count.

            #Store the letters of the word at the index of the current value in scrambled word.
            scrambled_word = list(sentence_list[word_count2])

            #If the word to be scrambled is less than 3 characters long, ignore it.
            if len(scrambled_word) > 3:
                word_length = len(scrambled_word) #Get length of word to be scrambled.

                pos_0 = scrambled_word[0] #Store characters at index 0 and 1.
                pos_1 = scrambled_word[1]

                #Word will have to be a minimum of 4 characters.
                scrambled_word[0], scrambled_word[1] = scrambled_word[3], scrambled_word[2]
                scrambled_word[3], scrambled_word[2] = pos_0, pos_1

                #print(scrambled_word) #Debug, show current scrambled word as its current list form.
                #Set the original list entry to the new joined together scrambled word.
                sentence_list[word_count2] = ''.join(scrambled_word)

            word_count2 = word_count2 + 1  ##Decrement word_count by 1.
            #print(sentence_list)
        #end while

        sentence_list = ' '.join(sentence_list)

        print("--Joined scramble--")
        print(sentence_list)

            #print("Scrambled Word: ","".join(scrambled_word)) #Display the scrambled word.

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation

word_scrambler = WordScramble()
word_scrambler.scramble()

