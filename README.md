# word guessing game project

This is a project in GeeksforGeeks website. I am creating this program for practice and modifying its code based on my own needs and to try more skills in python. the program in this project uses a wordlist text file as its source. using randome.choice() method, it chooses one of the words in the file and then it is the user's job to guess the word correctly in a number of chances. the chances' quantity is dependent on the lenght of the word. the longer the word is the more chances using simple equation depicted below:
chances = len(random_word) + int(len(random_word)/2)

it is random equation that I came up with !!
