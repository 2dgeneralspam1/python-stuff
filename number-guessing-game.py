import os
import random  
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

print('''
  ▄████  █    ██ ▓█████   ██████   ██████     ▒█████   ██▀███     ▓█████▄  ██▓▓█████ 
 ██▒ ▀█▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▒██    ▒    ▒██▒  ██▒▓██ ▒ ██▒   ▒██▀ ██▌▓██▒▓█   ▀ 
▒██░▄▄▄░▓██  ▒██░▒███   ░ ▓██▄   ░ ▓██▄      ▒██░  ██▒▓██ ░▄█ ▒   ░██   █▌▒██▒▒███   
░▓█  ██▓▓▓█  ░██░▒▓█  ▄   ▒   ██▒  ▒   ██▒   ▒██   ██░▒██▀▀█▄     ░▓█▄   ▌░██░▒▓█  ▄ 
░▒▓███▀▒▒▒█████▓ ░▒████▒▒██████▒▒▒██████▒▒   ░ ████▓▒░░██▓ ▒██▒   ░▒████▓ ░██░░▒████▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░    ▒▒▓  ▒ ░▓  ░░ ▒░ ░
  ░   ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░     ░ ▒ ▒░   ░▒ ░ ▒░    ░ ▒  ▒  ▒ ░ ░ ░  ░
░ ░   ░  ░░░ ░ ░    ░   ░  ░  ░  ░  ░  ░     ░ ░ ░ ▒    ░░   ░     ░ ░  ░  ▒ ░   ░   
      ░    ░        ░  ░      ░        ░         ░ ░     ░           ░     ░     ░  ░
                                                                   ░                 
''')

print("Guess the number correctly, or you will be sacrificed to the sun god.")
input("Once you have collected your wits, press enter. The sun god is waiting...")

clearConsole()

levelinput = input("Would you like to play on Easy or Hard?: ")

if levelinput in ("Easy", "easy", "ez"):
    LEVEL = 10
else: 
    LEVEL = 5 

clearConsole()
numberChosen = random.randint(1,50)
CURRENTLIFE = LEVEL 


print("I am thinking of a number inbetween 1 and 50.\n... Guess it or die.")
input(f"\n\nYou have {CURRENTLIFE} lives, or guesses, to guess the number. Press enter to start.")

while True:
    clearConsole()
    if CURRENTLIFE == 0: 
        clearConsole()
        print("You have lost. You have been sacrificed to the gun god.")
        input("Press any key to die.")
        break

    guess = input("Input your guess: ")
    
    if int(guess) == numberChosen:
        clearConsole()
        print("You have succeeded in guessing the number. Congratulations.")
        input("Press any key to escape the temple.")
        break
    else: 
        clearConsole()
        CURRENTLIFE -= 1 
        print(f"Your guess was incorrect. You have lost a life. You have {CURRENTLIFE} live(s) left.")
        input("Press enter to keep guessing...")
