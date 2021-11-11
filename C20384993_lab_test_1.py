#Author: Ciaran MacDermott, C20384993
#Date: 28/10/2021
#Description: Python program that uses a class and methods to open and read files.
#load_file() takes a file name and mode to open the file in and returns a string of file contents.
#find_words() takes 3 arguments, the first 2 are string values for the contents of 2 separate files,
#and the third is a string value of stop words. The 2 file content strings are compared and similar words
#are stored in one set and words that are in only 1 file are stored in another set. Both sets are printed.
#stop words are removed as well.

#Question 2, (a)
class Words:
    def __init__(self):
        pass
        #load_file("stops.txt","r") #Pass file name and file mode.




#Takes a file name and mode to open the file in and returns a string of file contents.
    def load_file(file_name,file_mode):
        cur_file = open(file_name,file_mode) #Open the file in the passed mode.
        #print(cur_file.readable())
        #print(cur_file.read())
        #except exception as e:
        #   print("Error opening file.") #Display error if file couldn't be opened.

        #Go through the file and enter every line into a variable.
        #ret_string = cur_file.readlines()
        ret_string = []
        for line in cur_file:
            ret_string=ret_string+line.split()

        print(ret_string)

        cur_file.close #Close the file.
        return ret_string



    def find_words(file1_content,file2_content,stop_words):
        #Empty sets.
        set_h1={}
        set_h2={}
        list_commonwords=[]
        list_uniquewords=[]

        #Loop through the words in the first set and compare to set_h2.
        for word in file1_content:
            #If the word is in set2 as well, put it into set_commonwords.
            if word in file2_content:
                list_commonwords+=word
            #Else if the word is not in set2, it is unique.
            elif word not in file2_content:
                list_uniquewords+=word #Add word to set.

        #Display the 2 sets of words.
        print(list_uniquewords)
        print(list_uniquewords)


#Question 2, part (c)
#content lists for 3 files.
content1 = []
content2 = []
content3 = []

instance1 = Words
content1 = instance1.load_file("herbert1.txt",'r')
content2 = instance1.load_file("herbert2.txt",'r')
content3 = instance1.load_file("stops.txt",'r')

instance1.find_words(content1,content2,content3)
#instance1.load_file("herbert1.txt")
#instance1.load_file("herbert2.txt")
#instance1.load_file("stops.txt")
#instance1.find_words(string1,string2,string3)
