# word guessing game

# importing modules
import random

# welcome message and greeting the user
name = input("Hello dear user! Can I have your name please? ")
print(f"great to meet you, {name}. Welcome to our little program.\n"
      f"we are truly thankful that you are here.\n"
      f"now to explain our program, this is a word guessing game.\n"
      f"a random word is chosen and you are prompted to guess the word\n"
      f"correctly. you have a specific amount of chances based on the word's\n"
      f"length. furthermore, you are advised to only type in alphabet and not\n"
      f"any unacceptable characters such as numbers or sings like $, #, !, etc.\n"
      f"any input is going to decrement your number of chances, so be careful to not\n"
      f"waste them!")

# importing a file, splitting its content and then using the rn.choice() to choose a random word
with open("1000-most-common-words.txt", "r") as word_file:
    words = word_file.read().split()

# variables
random_word = random.choice(words)
chances = len(random_word) + (int(len(random_word)/2))

# word guessing function
def word_guessing():

      print("\nnow its your time to type in the characters you think are in the word")
      print(f"\nshall we start the game, {name}.")
      print("\nthe following is the word you must guess:\n", "__ " * len(random_word), end="")
      print(f"\nyou have {chances} chances.")

      guessed_characters = []
      failed_attempts = 0

      # while loop
      while True:
            user_character = input("\nplease type in a character: ")

            if user_character.isalpha():
                  if user_character in random_word:
                        guessed_characters.append(user_character)
            else:
                  failed_attempts += 1
                  guessed_characters.append(user_character)
                  if failed_attempts == chances:
                        if user_character in guessed_characters:
                              print("\nYOU LOSE !!!\n"
                                    "you're happy now. You just wasted your chances\n"
                                    "by typing the same none sense :_(")
                        else:
                              print("\nYOU LOSE !!!\n"
                                    "you're happy now. You just wasted your chances\n"
                                    "by typing some none sense :_(")
                  elif failed_attempts == chances - 1:
                        if user_character in guessed_characters:
                              print("\nthis is the same wrong input that you have provided before.\n"
                              "please be careful to not waste your chances.\n"
                              "you have one more chance at this.\n"
                              "DON'T BLOW IT !!!")
                        else:
                              print("\nYour input does not follow the rules.\n"
                                    "please be careful to not waste your chances.\n"
                                    "you have one more chance at this.\n"
                                    "DON'T BLOW IT !!!")
                  else:
                        if user_character in guessed_characters:
                              print("\nthis is the same wrong input that you provided before.\n"
                              "please be careful to not waste your chances.\n"
                              f"you now have {chances - failed_attempts} chances")
