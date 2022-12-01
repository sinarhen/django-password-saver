from random import choice
from string import ascii_letters, digits, punctuation


def generate(dig: bool, spec_symbols: bool, letters: bool, length: int):
    letts = ''
    if dig:
        letts += digits
    if spec_symbols:
        letts += punctuation
    if letters:
        letts += ascii_letters
    password = ''
    for i in range(length):
        password += choice(letts)
    return password
