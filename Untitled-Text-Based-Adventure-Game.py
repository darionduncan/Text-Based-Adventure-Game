
#importing
import random
import time
import sys
from time import sleep
import os

#playerstats
player = {
    "Stamina": 50,
    "Max Stamina": 50,
    "XP": 0,
    "Level": 1,
    "Shovel": 1,
    "Items": [],
    "Toilet Paper": 0,
    "XP Multiplier": 1,
    "Depth (m)": 0
}

#defining functions
def clear_terminal():
<<<<<<< Updated upstream
=======
    sleep(2)
>>>>>>> Stashed changes
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_choices:
            return choice
        print(f"Invalid option, please enter one of: {', '.join(valid_choices)}")

def dig():
    if player["Stamina"] < 5:
        print("You are too tired to dig. Try eating or sleeping to refill stamina.")
        return
    player["Stamina"] -= 5
    xpgained = 10 * player["XP Multiplier"]
    player["XP"] += xpgained
    player["Depth (m)"] += 0.5
    print(f"You dig... (-5 stamina). Stamina: {player['Stamina']}. XP gained: {xpgained}. Depth (m): {player['Depth (m)']}.")

    itemsfound = 0
    for _ in range(player["Shovel"]):  # Number of item rolls = shovel level
        if random.randint(1, 2) == 1:
            found_item = random.choice(["watch", "jewellery", "soap", "radio"])
            player["Items"].append(found_item)
            itemsfound += 1
    if itemsfound:
        print(f"You found {itemsfound} item(s): {player['Items'][-itemsfound:]}")
    else:
        print("You didn't find any items.")

def rest():
    player["Stamina"] = player["Max Stamina"]
    print("You slept. Stamina fully restored.")

def eat():
    player["Stamina"] = min(player["Stamina"] + 20, player["Max Stamina"])
    print(f"You ate. Stamina now: {player['Stamina']}/{player['Max Stamina']}")

def playerstats(player):
    print("Player Stats:")
    for key, value in player.items():
        print(f"  {key.capitalize()}: {value}")


def gameoptions():
    while True:
        answersix = input("What would you like to do next? dig, eat, sleep, view player stats or quit the game? ")
        if answersix == "dig":
            dig()
        elif answersix == "eat":
            eat()
        elif answersix == "sleep":
            rest()
        elif answersix == "quit":
            print("Exiting game.")
            sys.exit()
        elif answersix == "view player stats":
            playerstats(player)
        else:
            print("Invalid option, please try again")

        # Depth check after action
        if player["Depth (m)"] >= 10:
            print("You have reached a depth of 10 meters.")
            break
        clear_terminal()

# loadingscreen
print("Initializing...")
sleep(1)
load = 0
print("Loading - ", load, "%")
sleep(0.5)
while load <= 99:
    load = load + 25
    print("Loading - ", load, "%")
    sleep(0.2)
print("Loading - Complete!")
sleep(0.3)
clear_terminal()
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

# Introduction to Game Demo
gamename = "Untitled Text Based Adventure Game"
print(f"Hello, and welcome to the {gamename}!")
sleep(0.5)

# Entering username and desired story location

while True:
    username = input("Enter your desired username or hit enter if you do not with to use a username: ")
    if len(username) <= 25:
        print("Username accepted")
        break
    else:
        print("Username too long, please enter a username that is 25 character or less.")

sleep(1)
print(f"Hello, {username} welcome to the {gamename}!")
sleep(0.5)

# Location does not alter storyline.

location = input("Enter the location you wish for the game to be set in. Please enter a city name: ")
sleep(1)
print(f"Your chosen location is, {location}")
sleep(0.5)

print("This game is based in 2006.")
sleep(0.5)
# Intro to game demo pt2

print("Before we begin, please note that this is only a demo. This is not the full game")
sleep(0.5)
clear_terminal()
# Storyline begins

print(r"""╔──────────────────────────────────────────────────────────────────────────────╗
│ _____ _            _   _       _   _ _   _          _                        │
│|_   _| |__   ___  | | | |_ __ | |_(_) |_| | ___  __| |                       │
│  | | | '_ \ / _ \ | | | | '_ \| __| | __| |/ _ \/ _` |                       │
│  | | | | | |  __/ | |_| | | | | |_| | |_| |  __/ (_| |                       │
│ _|_|_|_| |_|\___|  \___/|_| |_|\__|_|\__|_|\___|\__,_|                       │
│|_   _|____  _| |_     | __ )  __ _ ___  ___  __| |                           │
│  | |/ _ \ \/ / __|____|  _ \ / _` / __|/ _ \/ _` |                           │
│  | |  __/>  <| ||_____| |_) | (_| \__ \  __/ (_| |                           │
│  |_|\___/_/\_\__|    |____/ \__,_|___/\___|\__,_|  ____                      │
│   / \   __| |_   _____ _ __ | |_ _   _ _ __ ___   / ___| __ _ _ __ ___   ___ │
│  / _ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ | |  _ / _` | '_ ` _ \ / _ \│
│ / ___ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/ | |_| | (_| | | | | | |  __/│
│/_/   \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|  \____|\__,_|_| |_| |_|\___|│
╚──────────────────────────────────────────────────────────────────────────────╝""")
typewriter("You arrive home from that dreadful 9 - 5, feeling, exhausted..... drained")

# deciding whether to eat or not - does not affect storyline
typewriter("You make your way to the kitchen, and open the fridge"
           "\n You see some beers on the top shelf....."
           "\n You drink one."
           "\n You drink another....."
           "\n Next thing you know you have drank 6 or 7 beers..... "
           "\n Now your drunk."
           "\n You decide to go for a drive."
           "\n Personally I think that isn't a good idea but I am just the narrator so..."
           "\n You get in your car and start it."
           "\n You drive to the gas station to get some snacks..."
           "\n You have the 'bright' idea to stuff the snack down your trousers instead of buying them..."
           "\n The cashier spots you."
           "\n You run to the car and lock the door..."
           "\n You drive as fast as you can to get away..."
           "\n CRASH..."
           "\n You hit something..."
           "\n A parked car?!"
           "\n Really? Wow you must be drunk."
           "\n At least the car was a rental and you gave them a one use only debit card."
           "\n *Thinking to yourself* What do I do? Do I leave the car here? You know what screw it."
           "\n You run the rest of the way home."
           "\n You head back into the kitchen and put the snacks away in the cupboard."
           "\n You go in the fridge"
           "\nIn the fridge you find a slice of pizza")
answerone = get_choice("Would you like to eat the pizza? (yes/no): ", ["yes", "no"])

if answerone == "yes":
    print("You ate the pizza")
elif answerone == "no":
    print("You did not eat the pizza")
clear_terminal()

typewriter("You walk over to the couch and switch on the TV.")
print(r"""


                                   ▓                        ▓
                                   ▒▒                      ▒▓
                                     ▒▓                  ▒▒
                                      ▒▒                ▒▒
                                       ▒▒              ▒▒
                                        ▒▒            ▒▓
                                         ▒▒▓         ▒▒
                                          ▒▒▒ ▒▒▒▒ ▒▒▓
                                         ▒▒▒▒▒▒▓▓██▓▓▓▒
          ░░░░░░░░░░░░░░░░░░░░░░░░▒░▒▒▒▒▒▒▒░░░░▒▒▒▓▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓
          ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
          ░▒▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓██▓███████████████████████████████████████████▓▒▓▓
          ▒▒███▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████▓█▒▒▓▓
          ▒▒▓█▓▒▒▒▓▓▓▓▓▓▓▓▓██████████████████████████████████▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓████▓▓▓▓▓▒▒▓▓
          ▒▒▓█▓▒▓██▓█████                                  ████████▓▒▒▓▓▓▓░▒▓▓███▓▓▓▓▓▒▒▓▓
          ▒▒██▓▒█████                                           ████▒▒▓▓▓▒▒███▓▓▓▓█▓▓▓▒▒▓▓
          ▒▒▓█▓▒████                                             ███▒▒▓▓▓▓▓▓▓██▓▓███▓▓▒▒▓▓
          ▒▒▓█▓▒███                                               ██▒▓▓▓▓▓▓▓▓▓██████▓▓▒▒▓▓
          ▒▒▓█▓▓███                                               ██▒▓▓▓▓▓▓▓▓▓█████▓▓▓▒▒▒▓
          ▒▒▓█▓▓███                                               ██▒▒▓▓▓▓▓▒▒████▓▓▓▓▓▒▒▓▓
          ▒▒▓██▓██                                                ██▒▓▓▓▓▓░░▒████▓▓▓▓▓▒▒▒▓
          ▒▒▓██▓██                                                ██▒▓▓▓▓▓▓██▓▒██▓█▓▓▓▒▒▒▓
          ▒▒▓██▓██                                                ██▒▓▓▓▓▓▓▓▓██▓▓▓██▓▓▒▒▓▓
          ▒▒▓██▓██                                                 █▒▓▓▓▓▓▓▓▓▓▓▓████▓▓▒▒▓▓
          ▒▒▓██▓██                                                 █▒▓▓▓▓▓▓▓▓▓██████▓▓▒▒▓▓
          ▒▒▓██▓██                                                ██▒▓▓▓▓▓▓▒▓▓▓▓▓█▓▓▓▓▒▒▓▓
          ▒▒▓██▓██                                                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
          ▒▒▓██▓██                                                ██▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
          ▒▒▓██▓███                                               ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
          ▒▒▓█▓▓███                                               ██▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
          ▒▒▓██▓███                                               ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
          ▒▒▓█▓▓███                                              ███▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
          ▒▒▓█▓▓████                                             ███▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
          ▒▒▓█▓▓████                                            ████▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓
          ▒▒▓█▓▒▓████                                          █▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓
          ▒▒▓█▓▓▒█████▓▓▓██                               █████▒░▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒
          ▒▒▓██▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓███████████████████████▓▓▓▒▒▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒
          ▒▒▓██▓▒▒▒▒▒▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▒
          ▒▒▓██▓▓▓▓▒▒▒▒▒▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▒
          ▒▒▓███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▒
          ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
          ▒▒▒▒▒▒▒▒▒▒▓▒▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
                 ▒▒▓▓▓▓▓                                                    ▓▓▓▓██
                 ▒▒▒▓▓                                                        ▓▓▓▓
                 ▒▒▓                                                           ▓▒▓▓
                 ▒▓                                                              ▒▓





                                                                                                    """)

while True:
    answertwo = input("What channel would you like to watch? E4 or ITV?")
    if answertwo == "E4":
        print("You put on E4")
        break
    elif answertwo == "ITV":
        print("You put on ITV")
        break
    else:
        print("Invalid option, please try again")

if answertwo == "E4":
    typewriter("*TV Plays* The Simpsons")
else:
    typewriter("*TV Plays* Family Guy")

typewriter("You sit and watch TV for a few hours.... Falling asleep on the couch"
           "\nYou wake up suddenly..... To the sound of a loud banging."
           "\nIt seems to be coming from the front door?")
clear_terminal()
answerthree = get_choice("Do you walk to the door to check it out? (yes/no): ", ["yes", "no"])
if answerthree == "yes":
    typewriter("You walk to the door. And you peek through the peephole. You see..... ARMED police?!")
elif answerthree == "no":
    typewriter("You stay put.")

typewriter("*Thinking to yourself* Maybe its best I dont open the door. Whoever is out there seems really aggressive. "
           "\nYou decide to walk upstairs and amke your way to bed."
           "\nIt goes quiet"
           "\nSuddenly...")

print("BANG!!!")
typewriter("You hear running up the stairs"
           "\nYou hear a shout - 'ARMED POLICE!!! YOU ARE BEING ARRESTED ON SUSPICION OF MURDER BY FIREARM'"
           "\nYou look up and see 3 Officers holding you at gunpoint.")

jailtime = 0
answerfour = get_choice("Do you want to resist? yes /no: ",["yes", "no"])
if answerfour == "yes":
    jailtime = 67
elif answerfour == "no":
    jailtime = 30
else:
    print("Invalid option, please try again")

typewriter("A few days later..."
           "\n A bunch of stuff happens and as the narrator I will not go into too much detail because I am not paid enough."
           "\n To summarise: "
           "\n You woke up in a holding cell, went to court for a trial, you were found guilty."
           f"\n They gave you {jailtime} years in prison"
           "\n So now.... You are in prison. How fun!"
           "\n Oh... and by the way. You were framed. You didnt actually kill anybody."
           "\n So now it comes down to only one thing. ESCAPING!!")

answerfive = get_choice("Do you want to? yes or no?", ["yes", "no"])
if answerfive == "yes":
    typewriter("You made the right - yet morally and legally questionable - decision."
               "\n Lets get you ready to escape")
elif answerfive == "no":
    typewriter("Well that's the end of the game then")
    sys.exit("Game Over")
clear_terminal()

typewriter("Alright so you goal is to reach to 10 meters deep under your cell..."
           "\n After this you must head north to the nearest sewer..."
           "\n You then need to walk through the sewer until you reach the next manhole cover..."
           "\n After that all you need to do is make it back home from there..."
           "\n Well... Not exactly your home"
           "\n That would be a dumb idea..."
           "\n To escape from prison and to go back to the first place where the police would search"
           "\n Anyways lets continue with the storyline."
           "\n Okay. Lets start by breaking the tiles below this rug (why is there a rug in prison? idk gng js go with it fr)")

print("*You break the tiles*")

typewriter("Okay now grab the shovel under the bed (the prison guards are a bit dumb dw trust they wont see it")

print("*You grab the shovel*")

typewriter("Okay lets get digging.")
dig()
<<<<<<< Updated upstream
gameoptions()
=======
gameoptions()
>>>>>>> Stashed changes
