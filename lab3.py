#course: Object-oriented programming, year 2, semester 1
#academic year: 2021-22
#author: B. Schoen-Phelan
#date: 07-10-2021
#purpose: Lab 3

# Tasks:
#  1. Run the file as is
#  2. Follow the comments in the file and try to solve the
#     exercises. Use the Python documentation to identify
#     functions that could help you.
#  3. Answer the quiz questions.


class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        #message = input("Enter your noun: ")
        #print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #

        statement1 = ("Statement start, end platement here.")
        print(statement1)
        # 1. print only first and last of the sentence:
        list1 = statement1.split()
        print(list1[0],list1[4])

        # 2. use slice notation:
        print("Slice notation")
        print(list1[::4])

        # 3. escaping a character, such as an apostrophe or & sign:
        print("Special character, & , ' ")

        # 4. find all a's in the input word and count how many there are:
        print("-----Count a's in input.-----")
        #a_force = input("Enter word to count a's:")
        #count = a_force.count("a")
        #print("Number of a's: "+str(count))


        # 5. replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        print("-----replace function-----")
       # a_force = a_force.replace('a','-')
       # print(a_force)



    # to run the tasks associated with this file, you must first
    # uncomment line number 86 and comment line 85
    def play_with_lists(self):
        pets = ["Guy", "Fakes"]
        print(pets[len(pets)])
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # 6. hand the input string to a list and print it out:
        list2 = message.split()
        print(list2)

        # 7. append a new element to the list and print:
        list2.append('newelement')
        print(list2)

        # 8. remove from the list in 3 ways:
        list2.remove("Here")
        print(list2)

        # 9. check if the word cake is in your input list:
        print('cake' in list2)

        # 10. reverse the items in the list and print using a function:
        print(list2[::-1])

        # 11. reverse the list with the slicing trick: above


        # 12. print the list 3 times by using multiplication:
        print(list2*3)


tas = Types_and_Strings() # creates an instance of the object
#tas.play_with_strings() # calls the method play_with_strings()
tas.play_with_lists()
