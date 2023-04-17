from random import *
import string

def generate_password(length):
    password_length = length
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    special_characters = string.punctuation
    source = lower_case + upper_case + special_characters
    password = sample(source, password_length) 
    password = "".join(password)
    return password

