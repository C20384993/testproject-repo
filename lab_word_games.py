# course: Object-oriented programming, year 2, semester 1
# academic year: 2021-20
# author: B. Schoen-Phelan
# date: 11-11-2021
# purpose: Lab wk8 - Word Games

# base class
class WordGames:
    """
    Class to represent the word game's base class.
    Methods and attributes that every type of word
    game should have are defined here.
    ...
    Attributes:
    -----------
        _my_words : str
        Read from user input and identifies the word
        or sentence that a user has inputted.

    Methods:
    --------
        the_words:
            Property getter method that returns
            the value of the user inputted word
            or sentence

        word_play:
            Contains logic for playing the game.
            Child classes should override this
            method in order to implement their own
            game logic.
    """
    def __init__(self):
        """
        Constructs the necessary attributes for the
        WordGame object.

        Parameters: None.
        -----------

        Instance variables:
        -------------------
            _my_words : str
                Variable that holds the user inputted word or
                sentence. Set to enforced encapsulation via
                name mangling.
        """
        self._my_words = input("Please enter a word or sentence: ")

    @property
    def the_words(self):
        """
        Property method to return the value of the user
        inputted word or sentence.

        Parameters: None.
        -----------

        Returns:
        ________
            _my_words : str
                The value of the word or sentence that has
                been inputted by a user.
        """
        return self._my_words

    def word_play(self):
        """
        Plays the game. The base class version of playing
        the game simply prints the value that has been
        inputted.

        Parameters: None.
        -----------

        Returns: None.
        --------
        """
        print("User input was: "+self.the_words)


#Child class, overriding, same name as WordGames
class WordDuplication(WordGames): # you implement this and provide docstrings
    """
    Child class of CardGames. Takes user input
    and duplicates it.
    ...
    Attributes:
    -----------
        user_input : str
        Used to store user's input
        so it can be duped.
    """
    def word_play(self):
        user_input = input("Enter input for dupe: ")
        print("Duplication: "+user_input)

class WordScramble(WordGames): # you implement this and provide docstrings
    """
        Child class of WordGames. Takes user input and
        stores it in a variable. Contains simple logic
        for swapping letters around to simulate a
        scramble of the words.
        ...
        Attributes:
        -----------
            user_input : str
            Read from user input and identifies the word
            or sentence that a user has inputted.

            sentence_list : list
            Stores the user_input as a list

            word_count : int
            Store a count of the number of words in the
            sentence.

            word_count2 : int
            Used in the for loop against word_count.

            scrambled_word : str
            Store the letters of the word at the
            index of the current value.

            word_length : int
            Used to check if the current word is
            less than 3 characters long.

            pos_0 : int
            Used to temporarily store the character at
            the current index.

            pos_1 : int
            Used to temporarily store the character at
            the next index.

        Methods:
        --------
            None.
        """
    def word_play(self): #override init from WordGames
        self.user_input = input("Enter sentence: ")
        # print what was input
        print("The user input was: ", self.user_input)

        word_count = 0  # Number of words in the original sentence.
        scrambled_word = 'Empty'  # Stores scrambled version of word during while loop.

        sentence_list = list(self.user_input.split(" "))  # Convert the input into a list, split at each space.
        print(sentence_list)  # Debug, display the list version of the sentence.

        word_count = len(sentence_list)  # Store the number of words in the sentence.
        word_count2 = 0

        # Go through each word and put into a list.
        # Scramble the word and output it.
        # Original list of words is left unchanged.
        while word_count2 < word_count:  # From position 0 up to last.
            print("Word Count: ", word_count2)  # Debug, current iteration word count.

            # Store the letters of the word at the index of the current value in scrambled word.
            scrambled_word = list(sentence_list[word_count2])

            # If the word to be scrambled is less than 3 characters long, ignore it.
            if len(scrambled_word) > 3:
                word_length = len(scrambled_word)  # Get length of word to be scrambled.

                pos_0 = scrambled_word[0]  # Store characters at index 0 and 1.
                pos_1 = scrambled_word[1]

                # Word will have to be a minimum of 4 characters.
                scrambled_word[0], scrambled_word[1] = scrambled_word[3], scrambled_word[2]
                scrambled_word[3], scrambled_word[2] = pos_0, pos_1

                # print(scrambled_word) #Debug, show current scrambled word as its current list form.
                # Set the original list entry to the new joined together scrambled word.
                sentence_list[word_count2] = ''.join(scrambled_word)

            word_count2 = word_count2 + 1  ##Decrement word_count by 1.
            # print(sentence_list)
        # end while

        sentence_list = ' '.join(sentence_list)

        print("--Joined scramble--")
        print(sentence_list)


# prints the docstrings info
# if this class was a python module
print(WordGames.__doc__)

# Create an instances of the classes here:
wg = WordGames()
wg.word_play()

