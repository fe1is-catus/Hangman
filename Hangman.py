#Stage 1/8: Hello, Hangman
print (f"""H A N G M A N
The game will be available soon.""")

#2/8: I want to play a game
print ("H A N G M A N")
user_guess = input('Guess the word:')
if user_guess == "python":
    print ("You survived!")
else:
    print ("You are hanged!")

#3/8: Make your choice
import random

print ("H A N G M A N")
answers = ['python', 'java', 'kotlin', 'javascript']
user_guess = input('Guess the word:')

rigt_answer = random.choice(answers)
if user_guess == rigt_answer:
    print ("You survived!")
else:
    print ("You are hanged!")

#4/8: Help is on the way
import random

print ("H A N G M A N")
answers = ['python', 'java', 'kotlin', 'javascript']
rigt_answer = random.choice(answers)
hidden_symbols = '-' * (len(rigt_answer) - 3)
help_user = rigt_answer[0] + rigt_answer[1] + rigt_answer[2] + hidden_symbols

user_guess = input(f'Guess the word {help_user}:')
if user_guess == rigt_answer:
    print ("You survived!")
else:
    print ("You are hanged!")