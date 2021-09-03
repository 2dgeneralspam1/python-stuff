# import shit 

import os 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
import random 
import pyttsx3
engine = pyttsx3.init()
import os 

# thsi part is 100% not skidded xd123213

rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 200)     # setting up new voice rate


print('''

▓█████▄  ██░ ██  ▄▄▄       ██▀███      ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▒██▀ ██▌▓██░ ██▒▒████▄    ▓██ ▒ ██▒   ▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
░██   █▌▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒   ▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█▄   ▌░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄     ▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▒████▓ ░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒   ▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒▒▓  ▒  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░   ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ░ ▒  ▒  ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░   ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░ ░  ░  ░  ░░ ░  ░   ▒     ░░   ░    ░      ░     ░   ▒      ░   ░ ░ 
   ░     ░  ░  ░      ░  ░   ░               ░         ░  ░         ░ 
 ░                                                                               
''')

choice = input("Would you like TTS? (Yes or No)\n\n")
if choice.lower() in ["yes", "y"]:
    dothetango = True 
else:
    dothetango = False 

clearConsole()

print(f"Press Enter to generate phrases. TTS is set to {dothetango}\n\n")

while True: 
    wordsOne = [
        "Kid",
        "Adult",
        "Man",
        "Bully",
        "Felon",
        "Teacher",
        "Karen",
        "Woman",
        "Boy",
        "Friend",
        "President",
        "Gold Digger",
        "Best Friend",
        "Fake Friend",
        "Nerd",
        "Tik Toker",
        "Rich person",
        "Poor person",
        "Fake instagrammer",
        "Joe Biden",
        "Donald Trump",
        "Judge",
        "Lawyer"
    ]

    wordsTwo = [
        "Kills",
        "Beats",
        "Makes Fun Of",
        "Punches",
        "Shoots",
        "Tortures",
        "Convicts",
        "Steals",
        "Robs",
        "Destroys",
        "Burns",
        "Rips apart",
        "Burns alive",
        "Kicks",
        "Locks in basement",
        "Tears apart",
        "Farts on",
        "Throws off roof",
        "Eats",
        "Fat shames",
        "Bullies",
        "Judges",
        "Escapes",
        "Dodges"
    ]

    wordsThree = [
        "Kid",
        "Adult",
        "Man",
        "Bully",
        "Felon",
        "Teacher",
        "Karen",
        "Woman",
        "Boy",
        "Friend",
        "President",
        "Car",
        "House",
        "Phone",
        "Purse",
        "Wallet",
        "Tank",
        "Pizza",
        "Chicken",
        "Poor person",
        "Rich person",
        "Dumb kid",
        "Kid with ADHD",
        "Fat kid",
        "Skinny kid",
        "Poor kid",
        "Rich kid",
        "Female",
        "Joe Biden",
        "Donald Trump",
        "Taxes",
        "Shop owner"
    ]

    wordsFour = [ 
        "Instantly regrets it",
        "What happens next is shocking",
        "Lives to regret it",
        "Gets convicted",
        "Gets sent to jail",
        "Gets burned by Donald Trump",
        "Gets sent to jail for 500 years",
        "Instantly dies",
        "Gets killed by karma instantly",
        "Falls off a cliff",
        "Gets run over by a tractor",
        "Gets awarded",
        "Gets a prize",
        "Gets the Noble Peace Prize",
        "Buys a chicken",
        "Dies",
        "Dies, but then comes back alive then dies again",
        "Gets burned alive",
        "Dies from a toaster",
        "Does not live to regret it"
    ]


    randomthing = f"{random.choice(wordsOne)} {random.choice(wordsTwo)} {random.choice(wordsThree)}, {random.choice(wordsFour)}!"
    print(randomthing)
    if dothetango == True: 
        engine.say(randomthing)
        engine.runAndWait()
    
   
   # im dumb 
    input("")

