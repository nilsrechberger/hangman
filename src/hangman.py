#!/usr/bin/python3

from os import system

class WordBoard():
    def __init__(self, secret) -> None:
        self.secret = secret
        self.init_wordBoard()

    def init_wordBoard(self) -> None:
        self.wordBoard = ["_"] * len(self.secret)
        
    def show_wordBoard(self) -> None:
        print(self)

    def update_wordBoard(self, ind: int, char: str) -> None:
        self.wordBoard[ind] = char

    def __str__(self) -> str:
        return " ".join(self.wordBoard)

def show_hangman(attempt: int):
    system(f'cat img/hangman_{attempt}.txt')

def init_game() -> str:
    secret = input('Please set a secret word: ')
    wordBoard = WordBoard(secret=secret)
    show_hangman(attempt=0)
    return secret, wordBoard

def check_guess(guess: str, secret: str, attempt):
    if guess in secret:
        idx = secret.index(guess)
        return idx
    else:
        None

def main() -> None:
    secret, wordBoard = init_game()
    print(wordBoard)
    for attempt in range(1, 4): # Set max attempts here
        guess = input('Please set a guess: ')
        result = check_guess(guess=guess, secret=secret, attempt=attempt)
        if result != None:
            wordBoard.update_wordBoard(ind=result, char=guess)
        else:
            show_hangman(attempt=attempt)
        print(wordBoard)

if __name__ == '__main__':
    main()