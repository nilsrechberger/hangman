#!/usr/bin/python3

def init_game() -> str:
    secret = input('Please set a secret word: ')
    return secret

def check_guess(guess: str, secret: str) -> True | False:
    if guess in list(secret):
        print(True)
    else:
        print(False)

def main() -> None:
    secret = init_game()
    for _ in range(3): # Set max attempts here
        guess = input('Please set a guess: ')
        check_guess(guess=guess, secret=secret)

if __name__ == '__main__':
    main()