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

Milestone Two: User Interface
Develop a terminal user interface for the game. Start by welcoming the user, explaining the game rules, and then proceeding with the game. 
Sample prompts might include:
Welcome to Word Guess! You have 5 turns to guess the word. Please enter your first guess:

Wrong guess! Try again:

You got it! Amazing!

You're out of turns, game over!

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
    wordle.set_random_word()
    number_of_guesses = 5
    curr = number_of_guesses
    print(wordle.random_word)
    while curr > 0:
        if curr == number_of_guesses:
            guess = input("Welcome to Word Guess! You have 5 turns to guess the word. Please enter your first guess:")
        else:
            guess = input("Enter another guess:")
        
        if wordle.check_guess(guess):
            print("You got it! Amazing!")
            break
        else:
            if curr-1 == 0:
                print("You're out of turns, game over!")
            else:
                print("Wrong Guess. Try Again!")
            curr-=1


if __name__ == "__main__":
    main()