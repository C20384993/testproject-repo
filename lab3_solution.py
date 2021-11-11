#course: Object-oriented programming, year 2, semester 1
#academic year: 2021-22
#author: B. Schoen-Phelan
#date: 07-10-2021
#purpose: Solution to Lab 3

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
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #

        # 1. print only first and last of the sentence:
        print("First character: " + message[0])
        print("Last character : " + message[-1])

        # 2. use slice notation:
        print("Print from position 3 to end: " + message[3:])
        print("Print up to prosition 3: " + message[:3])
        print("Prints everthing via slice: " + message[:])

        # 3. escaping a character, such as an apostrophe or & sign:
        print("He said \"that\'s fantastic\"!")

        # 4. find all a's in the input word and count how many there are:
        lower_message = message.lower()
        print("all lower characters: " +lower_message)
        print("The first occurence of a is at position: " + str(lower_message.find('a')))
        print("There are "+ str(lower_message.count('a'))+ " a's in the word.")
        print("Total character count is: " +str(len(lower_message)))

        # 5. replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        print(lower_message.replace('a', '-'))


    # to run the tasks associated with this file, you must first
    # uncomment line number 75 and comment line 74
    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # 6. hand the input string to a list and print it out:
        li = list(message.split(" "))
        print(li)

        # 7. append a new element to the list and print:
        li.append("new")
        print(li)

        # 8. remove from the list in 3 ways:
        print(li.pop())
        print(li.remove("cake"))
        del li[-1:-2]
        print(li)

        # 9. check if the word cake is in your input list:
        print('cake' in li)

        # 10. reverse the items in the list and print using a function:
        li.reverse()
        print(li)

        # 11. reverse the list with the slicing trick:
        li[::-1]
        print(li)

        # 12. print the list 3 times by using multiplication:
        print(li*3)


tas = Types_and_Strings() # creates an instance of the object
tas.play_with_strings() # calls the method play_with_strings()
#tas.play_with_lists()
