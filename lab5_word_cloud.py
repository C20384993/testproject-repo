# course: Object-oriented programming, year 2, semester 1
# academic year: 2021-22
# author: B. Schoen-Phelan
# date: Oct 2021
# purpose: Lab 5 Exceptions and Files

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        self.create_html(self.my_dict)

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurance of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write('<!DOCTYPE html>\
            <html>\
            <head lang="en">\
            <meta charset="UTF-8">\
            <title>Tag Cloud Generator</title>\
            </head>\
            <body>\
            <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

        # your code goes here!
        fo.write('<span style="font-size: 20px"> HELLO </span>')

        fo.write('</div>\
            </body>\
            </html>')

        fo.close()


    # opens the input file gettisburg.txt
    # remember to open in in the correct mode
    # reads the file line by line
    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):
        my_dict = {} #Create dictionary.
        # your code goes here:
        speech_file = open('gettisburg.txt','r') #Open file for reading.
        for line in speech_file: #Read the file line by line.
            #print(speech_file.readline())
            #current_word = print(line)
            current_word = line.split(" ")
            if word in current_word:
                my_dict[word] = my_dict[word] + 1
            else:
                my_dict[word] = 1  # Put word in dictionary.
            #(word, frequency) = line.split() #Store the word and number of occurences.
        speech_file.close()
        print(my_dict)

        return my_dict

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary
    def add_to_dict(self, word, the_dict):
        # your code goes here
        if word in the_dict:
            the_dict[word] = my_dict[word] + 1
        else:
            the_dict[word] = 1  # Put word in dictionary.

        return the_dict

# creates an instance of the WordCloud object
# remember first step after creation of an instance
# is that Python goes into the __init__ function
wc = WordCloud()
