from random import *
from string import ascii_lowercase, ascii_uppercase, punctuation

def generate_password(password_length):
    lower_case = ascii_lowercase
    upper_case = ascii_uppercase
    special_characters = punctuation
    source = lower_case + upper_case + special_characters
    password = sample(source, password_length) 
    password = "".join(password)
    return password

print(generate_password(8))