#!/usr/bin/python3

from os import system
from getpass import getpass

class WordBoard():
    """
    Manages the visual state of the secret word during a Hangman game.

    This class handles the creation of the hidden word representation (underscores) 
    and provides methods to update and display the progress as the player 
    guesses correct letters.

    Attributes:
        secret (str): The word that needs to be guessed.
        word_board (list[str]): A list of characters representing the current 
            state of the board (e.g., ['_', 'a', '_']).
    """
    def __init__(self, secret) -> None:
        """
        Initializes the WordBoard with a secret word.

        Args:
            secret (str): The secret word to be tracked.
        """
        self.secret = secret
        self.init_wordBoard()

    def init_wordBoard(self) -> None:
        """
        Creates the initial hidden board consisting of underscores.
        """
        self.wordBoard = ["_"] * len(self.secret)
        
    def show_wordBoard(self) -> None:
        """
        Prints the current state of the board to the console.
        """
        print(self)

    def update_wordBoard(self, ind: int, char: str) -> None:
        """
        Updates a specific position on the board with a correctly guessed character.

        Args:
            index (int): The position in the word to reveal.
            char (str): The character to place at the given index.
        """
        self.wordBoard[ind] = char

    def __str__(self) -> str:
        """
        Returns a string representation of the board with spaces between characters.

        Returns:
            str: The formatted board (e.g., "_ _ a _ _").
        """
        return " ".join(self.wordBoard)

def show_hangman(attempt: int) -> None:
    """
    Prints the current game state in the CLI.

    Args:
        attempt (int): Wrong attempts counter.
    
    Returns:
        None: No return value. Prints directly in the CLI.
    """
    system(f'cat img/hangman_{attempt}.txt')

def init_game() -> list[str, WordBoard]:
    """ 
    Helper function to initialise the game.

    > Note: User input will be hide in the CLI!
    """
    secret = getpass('Please set a secret word: ') # Hides user input
    secret = secret.lower()
    wordBoard = WordBoard(secret=secret)
    show_hangman(attempt=0) # Init game state img
    return secret, wordBoard

def check_guess(guess: str, secret: str) -> list[int] | None:
    """ 
    Checks a guessed character against the secret.

    Args:
        guess (str): Guessed single character
        secret (str): The secret word to guess

    Returns:
        list[str]: List of indexes, where the character appears in the secret
        None: If the character does not appear in the secret.
    """
    if guess in secret:
        # Finds all ind where the char appears in secret
        ind = [i for i, val in enumerate(secret) if val == guess]
        return ind
    else:
        None

def main() -> None:
    """ 
    Main game logic.

    Runs all the functionalities to play the game. 
    """
    secret, wordBoard = init_game()
    attempts = 0
    print(wordBoard)
    # Set max attempts here
    while attempts <= 2: # Make sure there are enough hangman imgs!
        guess = input('Please set a guess: ')
        guess = guess.lower()
        result = check_guess(guess=guess, secret=secret)
        if result != None:
            show_hangman(attempt=attempts)
            for ind in result:
                wordBoard.update_wordBoard(ind=ind, char=guess)
        else:
            attempts += 1
            show_hangman(attempt=attempts)
        print(wordBoard)
        # Winning logic
        current_word = "".join(wordBoard.wordBoard)
        if current_word == secret:
            print('YOU WON!')
            break

if __name__ == '__main__':
    main()