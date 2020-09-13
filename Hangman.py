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
right_answer = random.choice(answers)
hidden_symbols = '-' * (len(rigt_answer) - 3)
help_user = rigt_answer[0] + rigt_answer[1] + rigt_answer[2] + hidden_symbols

user_guess = input(f'Guess the word {help_user}:')
if user_guess == rigt_answer:
    print ("You survived!")
else:
    print ("You are hanged!")


#5/8: Keep trying
import random

print("H A N G M A N")
print()
answers = ['python', 'java', 'kotlin', 'javascript']
right_answer = random.choice(answers)

dashes = list('-'*len(right_answer))

attempt = 0
while attempt < 8:
    string = "".join(dashes)
    print(string)
    user_guess_letter = input('Input a letter : ')
    if user_guess_letter in right_answer:
        for i in range(len(right_answer)):
            if user_guess_letter == right_answer[i]:
                dashes[i] = user_guess_letter
    else:
        print("No such letter in the word")
    print("\n")
    attempt += 1

print('''Thanks for playing!
We'll see how well you did in the next stage''')

#Stage 6/8: The value of life
import random

print("H A N G M A N")
answers = ['python', 'java', 'kotlin', 'javascript']
right_answer = random.choice(answers)
dashes = list('-'*len(right_answer))
attempt = 0

while attempt < 8:
    print()
    string = "".join(dashes)
    print(string)
            
    if dashes == right_answer:
        print("You guessed the word!")
        print("You survived!")
        break
    
    user_guess_letter = input('Input a letter:')
    
    if user_guess_letter in string:
        print('No improvements')
        attempt += 1
        
    elif user_guess_letter in right_answer:
        for i in range(len(right_answer)):
            if user_guess_letter == right_answer[i]:
                dashes[i] = user_guess_letter
    else:
        print("No such letter in the word")
        attempt += 1

if dashes != right_answer:
    print("You are hanged!")