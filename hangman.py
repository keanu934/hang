import random


def prompt(*valid):
    ''' this function handles prompting the user to play a game '''
    choice = input(
        " Do you want to play a game? (yes/y or no/n): ").lower().strip()
    if choice in valid:
        if choice == "yes" or choice == "y":
            print("lets play a game ")
        if choice == "no" or choice == "n":
            print(" LAME !")
    if choice not in valid:
        print("That isnt a valid choice ")

    words = ("eminem", "superman", "cheer", "")
    guess_letters = set(words)
    return guess_letters


def decide_status(guess_count, status):
    if guess_count == 0:
        status = """
      _______
     |/      |
     |
     |
     |
     |
     |
   _|___
 
"""
    if guess_count == 1:
        status = """
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
   _|___
 
    """
    if guess_count == 2:
        status = """
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |
     |
   _|___
 
 
    """
    if guess_count == 3:
        status = """
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |
     |
   _|___
    """
    if guess_count == 4:
        status = """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
   _|___
 
    """
    if guess_count == 5:
        status = """
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
   _|___
 
"""
    if guess_count == 6:
        status = """
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
   _|___
        """


def guess_system(guess_letters):
    """ handels the guess system"""
    guess_count = 0
    while True:
        # print (status)
        guess = input(" Guess a letter : ").lower().strip()
        if guess not in guess_letters:
            print(f"nope {guess} is not in the word ")
            guess_count = guess_count+1
        if guess in guess_letters:
            print(f"{guess}is in the word !")
        if len(guess) >= 2:
            print("THAT TOO MANY LETTERS ")
        decide_status()


def play_game():
    words = {"eminem", "superman", "cheer", "hunting", "mountain",
             "crush", "vaquero", "hangman", "aqueous", "dysproaium"}
    word = random.choice(list(words))
    guess_letters = set(word)
    print(guess_letters)
    prompt("yes", "y", "no", "n")
    guess_system(guess_letters)


if __name__ == '__main__':
    play_game()
