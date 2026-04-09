#!/usr/bin/python3

secret = "cat"

guesses = [
    "c",
    "x",
    "a",
    "t"
]

def test() -> None:
    print(list(secret))

def main() -> None:
    for letter in guesses:
        if letter in list(secret):
            print(True)
        else:
            print(False)

if __name__ == '__main__':
    main()