#!/bin/python3
# MasterMind
# by ICTROCN
# v1.02
# 06-02-2025
# Last mod by Bryan : added word list and words instead of numbers
print("MasterMind")

import random

word_list = [
    "lief", "boom", "wolf", "held", "maan", "goud", "rood", 
    "hart", "spin", "mooi", "wind", "zand", "klok", "vuur",
    "noot", "geel", "leef", "meer", "duik", "snee", "kruk",
    "hoop", "tent", "voet", "koud", "warm", "wand", "deur", 
    "doek", "veer", "blad", "gras", "klop", "blik", "keer",
    "hand", "wang", "neus", "tand", "teen", "been", "klem", 
    "leeg", "volk", "reis", "zang", "lijn", "muur", "vlag",
    "ring", "hond", "kooi", "bank", "kast", "kist", "lamp",
    "zeep", "kous", "balg", "hark", "zaag", "gids", "druk",
    "film", "boek", "spel", "dans", "lied", "vlas", "leus",
    "buis", "trap", "gang", "lift", "rots", "grot", "dijk",
    "beek", "rond", "vlak", "vlek", "klas", "veer", "rook",
    "raam", "boog", "zeil", "toet", "bout", "deur", "nest",
    "haak", "peer", "baas", "touw", "been", "pijl", "zout",
]

def generate_Code():
    return list (random.choice(word_list))

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    # Count whites by subtracting black and calculating min digit frequency match
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

def show_Secret(mystery):
    print(mystery)

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-letter word. You have 10 attempts.")
    secret_Code = generate_Code()
    attempts = 10
    admin_code = "Admin123"
    is_admin = False

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Attempt {attempt}: ").strip().lower()
            if guess == "Admin" or guess == "admin":
                if is_admin:
                    print("You are already in admin mode.")
                    continue
                code_guess = input("What is the admin password? ")
                if code_guess == admin_code:
                    is_admin = True
                    print("Admin mode activated.")
                    continue
                else:
                    print("Incorrect admin code. Try again.")
                    continue

            if guess == "cheat" and is_admin or guess == "Cheat" and is_admin:
                print("The secret code is:")
                show_Secret(secret_Code)
                continue
                    
            valid_Guess = len(guess) == 4 and guess.isalpha()
            if not valid_Guess:
                print("Invalid input. Enter a valid 4 letter word.")

        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        play_Mastermind()
        again  = input (f"Play again (Y/N) ?").upper()

