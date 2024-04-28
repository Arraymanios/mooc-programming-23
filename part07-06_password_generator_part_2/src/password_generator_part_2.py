# Write your solution here
from random import *

def generate_strong_password(length: int, numbers: bool, characters: bool):
    password = ""
    special = ['!', '?', '=', '+', '-', '(', ')', '#']
    for i in range(length):
        choices = [chr(randint(97, 122))]
        if numbers:
            choices.append(chr(randint(48, 57)))
        if characters:
            choices.append(choice(special))
        password += choice(choices)  
    return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
