import random

"""
Word Guess Challenge

Implement a word guessing game initialized with a dictionary and a target word. 
The user will enter guesses, and the system will indicate whether the guess is correct, providing hints to guide the user. 
We will begin with a basic version and gradually introduce new requirements to add complexity. 
Aim to design your game for easy extension and refactor as you learn more.
Please note that this problem is challenging. We do not expect you to complete all of it during this sessi


Milestone One: Data Structures and Basic Functionality
Define a dictionary consisting of valid four-letter words. Store the following list:
["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"]
Implement a method to randomly select a word from this list.
Implement a method to accept a guess and check if it matches the selected word.

"""

class Wordle:
    """
    Main Wordle class for checking and storing data for game functionality.
    """

    def __init__(self, word_list):
        self.word_list = word_list
        self.random_word = None
        
    
    def set_random_word(self)->str:
        """Sets a random word for our Wordle object."""

        if self.random_word == None:
            self.random_word = self.word_list[random.randint(0, len(self.word_list))]
            return self.random_word
        else:
            print("Already have a random word")
            return self.random_word
    
    def check_guess(self, word)->bool:
        """Checks if the users input matches our random word."""

        return word == self.random_word
    


def main():
    wordle = Wordle(["able", "belt", "bolt", "cast", "cash", "knot", "note", "near", "over", "salt", "wind"])
    print(wordle.set_random_word())
    print(wordle.check_guess("word"))


if __name__ == "__main__":
    main()