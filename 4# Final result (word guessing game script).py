# word guessing game

# importing modules
import random

# welcome message and greeting the user
name = input("Hello dear user! Can I have your name please? ")
print(f"\ngreat to meet you, {name}. Welcome to our little program.\n"
      f"we are truly thankful that you are here.\n"
      f"now to explain our program, this is a word guessing game.\n"
      f"a random word is chosen and you are prompted to guess the word\n"
      f"correctly. you have a specific amount of chances based on the word's\n"
      f"length. furthermore, you are advised to only type in alphabet and not\n"
      f"any unacceptable characters such as numbers or signs like $, #, !, etc.\n"
      f"any input is going to decrement your number of chances, so be careful to not\n"
      f"waste them!")

# importing a file, splitting its content and then using the rn.choice() to choose a random word
with open("1000-most-common-words.txt", "r") as word_file:
    words = word_file.read().split()

# variables
random_word = random.choice(words)
chances = len(random_word) * 4

# word guessing function
def word_guessing():

      print("\nnow its your time to type in the characters you think are in the word")
      print(f"\nshall we start the game, {name}.")
      print("\nthe following is the word you must guess:\n", "__ " * len(random_word), end="")
      print(f"\nyou have {chances} chances.")

      # function variables
      input_characters = []
      failed_attempts = 0

      # while loop
      while True:

            if all(char in input_characters for char in random_word):
                  return ("congratulation !!!! You actually guessed the word correctly.\n"
                          "job well done :).\n"
                          "hope to see next time.\n"
                          f"the word is: {random_word}")
            else:
                  user_character = input("\nplease type in a character: ")
                  lower_user_char = user_character.lower()

                  if lower_user_char.isalpha():
                        if lower_user_char in random_word:
                              # append the character to the list
                              input_characters.append(lower_user_char)

                              for i in random_word:
                                    if i in input_characters:
                                          print(i, end= " ")
                                    else:
                                          print("__", end= " ")
                              print("\n")
                              print(f"you have now {chances - failed_attempts} attempt/attempts left")

                        # if the user character is an alphabet but not in the word
                        else:
                              failed_attempts += 1
                              if failed_attempts == chances:
                                    if lower_user_char in input_characters:
                                          # append the character to the list
                                          input_characters.append(lower_user_char)

                                          return("\nYOU LOSE !!!\n"
                                                "you're happy now. You just wasted your chances\n"
                                                "by typing the same wrong answer again :_(\n"
                                                f"\n"
                                                f"the word is: {random_word}")
                                    else:
                                          # append the character to the list
                                          input_characters.append(lower_user_char)

                                          return("\nYOU LOSE !!!\n"
                                                 "it's ok. better luck next time :)\n"
                                                 f"the word is: {random_word}")
                              elif failed_attempts == chances - 1:
                                    if lower_user_char in input_characters:
                                          # append the character to the list
                                          input_characters.append(lower_user_char)

                                          print("\nthis is the same wrong input that you have provided before.\n"
                                                "please be careful to not waste your chances.\n"
                                                "you have one more attempt left.\n"
                                                "DON'T BLOW IT !!!")
                                    else:
                                          # append the character to the list
                                          input_characters.append(lower_user_char)

                                          print("\nthis character is not in the word.\n"
                                                "please be careful to not waste your chances.\n"
                                                "you have one more attempt left.\n"
                                                "DON'T BLOW IT !!!")
                              else:
                                    if lower_user_char in input_characters:
                                          # append the character to the list
                                          input_characters.append(lower_user_char)

                                          print("\nthis is the same wrong input that you provided before.\n"
                                                "please be careful to not waste your chances.\n"
                                                f"you now have {chances - failed_attempts} attempt/attempts left")
                                    else:
                                          # append the character to the list
                                          input_characters.append(lower_user_char)

                                          print("\nthis character is not in the word.\n"
                                                f"you now have {chances - failed_attempts} attempt/attempts left")

                  # if the user input is not alphabet
                  else:
                        failed_attempts += 1
                        if failed_attempts == chances:
                              if lower_user_char in input_characters:
                                    # append the character to the list
                                    input_characters.append(lower_user_char)

                                    return("\nYOU LOSE !!!\n"
                                          "you're happy now. You just wasted your chances\n"
                                          "by typing the same none sense :_(\n"
                                          f"the word is: {random_word}")
                              else:
                                    # append the character to the list
                                    input_characters.append(lower_user_char)

                                    return("\nYOU LOSE !!!\n"
                                          "you're happy now. You just wasted your chances\n"
                                          "by typing some none sense :_(\n"
                                          f"the word is: {random_word}")
                        elif failed_attempts == chances - 1:
                              if lower_user_char in input_characters:
                                    # append the character to the list
                                    input_characters.append(lower_user_char)

                                    print("\nthis is the same wrong input that you have provided before.\n"
                                          "please be careful to not waste your chances.\n"
                                          "you have one more attempt left.\n"
                                          "DON'T BLOW IT !!!")
                              else:
                                    # append the character to the list
                                    input_characters.append(lower_user_char)

                                    print("\nYour input does not follow the rules.\n"
                                          "please be careful to not waste your chances.\n"
                                          "you have one more attempt left.\n"
                                          "DON'T BLOW IT !!!")
                        else:
                              if lower_user_char in input_characters:
                                    # append the character to the list
                                    input_characters.append(lower_user_char)

                                    print("\nthis is the same wrong input that you provided before.\n"
                                          "please be careful to not waste your chances.\n"
                                          f"you now have {chances - failed_attempts} attempt/attempts left")
                              else:
                                    # append the character to the list
                                    input_characters.append(lower_user_char)

                                    print("\nYour input does not follow the rules.\n"
                                          "please be careful to not waste your chances.\n"
                                          f"you now have {chances - failed_attempts} attempt/attempts left")

# call the function to action
final_result = word_guessing()
print(final_result)
