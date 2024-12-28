#!/usr/bin/env python
import random
import pickle
import os

# Replace 'ENV_VAR_NAME' with the name of the environment variable you want to print
env_var_name = 'FLAG'
env_value = os.getenv(env_var_name)

def restore_split_pickles(first_pickle_file, second_pickle_file):
    # Load the first part
    with open(first_pickle_file, 'rb') as f:
        first_part = pickle.load(f)
    
    # Load the second part
    with open(second_pickle_file, 'rb') as f:
        second_part = pickle.load(f)
    
    # Combine the two parts into one dictionary
    combined_dict = {**first_part, **second_part}
    
    return combined_dict

# Usage
traces = restore_split_pickles('first_part.pkl', 'second_part.pkl')
# traces = pickle.load(open("./traces.pkl", 'rb'))

flag = "sha3bola"
# flag = "0xL4ugh{Sha3b0la}"

def cap_pass_trace(password_guess):
    # Remove the trailing newline character
    password_guess = password_guess.strip("\n")

    # Known password (global variable `flag` assumed to be defined elsewhere)
    known_password = flag

    # Allowed characters in the password guess
    allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789\x01"

    # Check if the password guess exceeds the length of the known password
    if len(password_guess) > len(known_password):
        print(f"Only guesses up to {len(known_password)} characters are allowed.")
        quit()

    # Ensure all characters in the password guess are in the allowed list
    for char in password_guess:
        if char not in allowed_characters:
            print(f"Invalid character '{char}' in guess. Allowed characters: {allowed_characters}")
            quit()

    # Build the recorded password based on correct matches with the known password
    recorded_password = ""
    for i, char in enumerate(password_guess):
        if known_password[i] != char:
            recorded_password += "*" * (len(password_guess) - i)
            break
        recorded_password += char

    # Return a random trace from the preloaded traces for the recorded password
    return traces[recorded_password][random.randint(0,99)]


inp = input("DEBUG> ")

if "sha3bola" in inp:
    print(f"Correct! here's your flag: ", env_value)
else:
    res = cap_pass_trace(inp)[:1000]
    print(res)
