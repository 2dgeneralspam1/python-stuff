import random 
import os 
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
import time 
import pyperclip 

numberOf = input("How many titles do you want to generate? ")

clearConsole()

counter = 0 

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
        "Lawyer",
        "Vice President",
        "Idiot",
        "Mentally Challenged Person",
        "Robot",
        "Wall-E",
        "Black person", # I'm not racist, this is just for the generator 
        "White person",
        "SsSniper Wolf",
        "Dhar Mann",
        "Dhar man",
        "Flamingo",
        "DanTDM",
        "YouTuber",
        "Skinny ass nigga",
        "Nigga",
        "White ass nigga",
        "PewDiePie",
        "Famous guy",
        "Stitch",
        "Roblox Player",
        "Slender",
        "The Imposter",
        "The Imposter From Among Us",
        "The Crewmate",
        "The Crewmate from Among Us",
        "Bob"
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
        "Dodges",
        "Drowns",
        "Dunks",
        "Shames",
        "Skinny shames",
        "Looks at",
        "Farts on",
        "Consumes",
        "Shocks"
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
        "Does not live to regret it",
        "Falls into the river and dies",
        "Becomes the president",
        "Turns into a black person"
]

savedWords = ["demo"]

while True: 
    if int(counter) < int(numberOf): 
        randomthing = f"{random.choice(wordsOne)} {random.choice(wordsTwo)} {random.choice(wordsOne)}, {random.choice(wordsFour)}!"
        print(randomthing)
        counter = counter + 1    
        savedWords.append(str(randomthing))
    else:
        input("\ndone\n")
        break
