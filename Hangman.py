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

#Stage 7/8: Error!
import random

print("H A N G M A N")
answers = ['python', 'java', 'kotlin', 'javascript']
right_answer = random.choice(answers)
dashes = list('-'*len(right_answer))
eng_lowc_letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

user_guess_letters = []

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
    
    if len(user_guess_letter) != 1:
        print("You should input a single letter")
    
    elif user_guess_letter not in eng_lowc_letter:
        print("It is not an ASCII lowercase letter")

    elif user_guess_letter in user_guess_letters:
        print('You already typed this letter')
            
    elif user_guess_letter in right_answer:
        user_guess_letters.append(user_guess_letter)
        for i in range(len(right_answer)):
            if user_guess_letter == right_answer[i]:
                dashes[i] = user_guess_letter
           
    else:
        user_guess_letters.append(user_guess_letter)
        print("No such letter in the word")
        attempt += 1

if dashes != right_answer:
    print("You are hanged!")

#Stage 8/8: Menu, please
import random

print("H A N G M A N")

def game_start():
    answers = ['python', 'java', 'kotlin', 'javascript']
    right_answer = random.choice(answers)
    dashes = list('-'*len(right_answer))
    user_guess_letters = []
    eng_lowc_letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    attempt = 0
    
    while attempt < 8:
        print()
        string = "".join(dashes)
        print(string)
                
        if string == right_answer:
            print("You guessed the word!")
            print("You survived!")
            break
        
        user_guess_letter = input('Input a letter:')
        
        if len(user_guess_letter) != 1:
            print("You should input a single letter")
        
        elif user_guess_letter not in eng_lowc_letter:
            print("It is not an ASCII lowercase letter")
        
        elif user_guess_letter in user_guess_letters:
            print('You already typed this letter')
                
        elif user_guess_letter in right_answer:
            user_guess_letters.append(user_guess_letter)
            for i in range(len(right_answer)):
                if user_guess_letter == right_answer[i]:
                    dashes[i] = user_guess_letter
            
        else:
            user_guess_letters.append(user_guess_letter)
            print("No such letter in the word")
            attempt += 1

    if string != right_answer:
        print("You lost!")

def menu():
    user_choise = input('Type "play" to play the game, "exit" to quit:')
    if user_choise == "play":
        game_start()
    else:
        menu()
menu()
