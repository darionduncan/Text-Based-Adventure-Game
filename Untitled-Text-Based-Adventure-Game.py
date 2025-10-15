#importing
import random
import time
import sys
from time import sleep
import os

#playerstats
player = {
    "Stamina": 20,
    "Max Stamina": 20,
    "XP": 0,
    "Level": 1,
    "Shovel": 1,
    "Items": [],
    "XP Multiplier": 1,
    "Depth (m)": 0,
    "XP Needed": 50,
    "Inventory Limit": 5,
    "Money(£)": 0
}

ITEM_VALUES = {
    "watch": 20,
    "jewellery": 50,
    "soap": 5,
    "radio": 30
}

def sell_items():
    if not player["Items"]:
        print("You have no items to sell.")
        return
    print("Your items:")
    item_counts = {}
    for item in player["Items"]:
        item_counts[item] = item_counts.get(item, 0) + 1
    for item, count in item_counts.items():
        print(f"{item}: {count} (Value: £{ITEM_VALUES.get(item, 0)} each)")
    to_sell = input("Enter the item you want to sell (or 'all' to sell everything): ").strip().lower()
    total_earned = 0
    if to_sell == "all":
        for item in list(player["Items"]):
            value = ITEM_VALUES.get(item, 0)
            total_earned += value
            player["Items"].remove(item)
        player["Money(£)"] += total_earned
        print(f"You sold all items for £{total_earned}. You now have £{player['Money(£)']}.")
    elif to_sell in item_counts:
        count = item_counts[to_sell]
        value = ITEM_VALUES.get(to_sell, 0)
        for _ in range(count):
            player["Items"].remove(to_sell)
            total_earned += value
        player["Money(£)"] += total_earned
        print(f"You sold {count} {to_sell}(s) for £{total_earned}. You now have £{player['Money(£)']}.")
    else:
        print("You don't have that item.")



#defining functions
def clear_terminal(): #clears terminal with a delay
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def clear(): # clears terminal instantly
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_delay(): #clears terminal with a short delay
    sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')
def typewriter(text, delay=0.04):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fast_type(text, delay=0.001):
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
    if player["Level"] < 5:
        while player["XP"] >= player["XP Needed"] and player["Level"] < 5:
            player["Level"] += 1
            player["Max Stamina"] += 10
            player["Stamina"] = player["Max Stamina"]
            player["Shovel"] += 1
            player["XP Multiplier"] += 0.1
            player["XP"] -= player["XP Needed"]
            player["XP Needed"] += 20
            print(f"Congratulations! You've leveled up to Level {player['Level']}!")
            print(f"Max Stamina increased to {player['Max Stamina']}. Stamina fully restored.")
            print(f"Shovel level increased to {player['Shovel']}. XP Multiplier is now {player['XP Multiplier']:.1f}.")
            print(f"XP needed for next level: {player['XP Needed']}")
    elif player["Level"] >= 5 and player["XP"] >= player["XP Needed"]:
        print("You have reached the max level (Level 5)!")
    dig_area = 0.25 * player["Shovel"]
    player["Depth (m)"] += dig_area
    print(f"You dig... (-5 stamina). Stamina: {player['Stamina']}. XP gained: {xpgained}. Depth (m): {player['Depth (m)']}.")

    itemsfound = 0
    for _ in range(player["Shovel"]):  # Number of item rolls = shovel level
        if random.randint(1, 2) == 1:
            for _ in range(player["Shovel"]):  # Multiply items found by shovel level
                if len(player["Items"]) < player["Inventory Limit"]:
                    found_item = random.choice(["watch", "jewellery", "soap", "radio"])
                    player["Items"].append(found_item)
                    itemsfound += 1
                else:
                    print("Your inventory is full! You can't carry more items.")
                    break
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
        answersix = input("What would you like to do next? "
        "\n dig, eat, sleep, 'player' to view player stats, 'sell' to sell items or 'quit' to quit the game? ")
        clear()
        if answersix == "dig":
            dig()
        elif answersix == "eat":
            eat()
        elif answersix == "sleep":
            rest()
        elif answersix == "quit":
            print("Exiting game.")
            sys.exit()
        elif answersix == "player":
            playerstats(player)
        elif answersix == "sell":
            sell_items()
        else:
            print("Invalid option, please try again")

        # Depth check 
        if player["Depth (m)"] >= 20:
            print("You have reached a depth of 20 meters.")
            break
        

# loadingscreen
print("Initializing...")
clear_delay()
load = 0
print("Loading - ", load, "%")
clear_delay()
while load <= 99:
    load = load + 25
    print("Loading - ", load, "%")
    clear_delay()
print("Loading - Complete!")
clear_terminal()

# Introduction to Game Demo
gamename = "Untitled Text Based Adventure Game"
print(f"Hello, and welcome to the {gamename}!")
sleep(0.5)
clear_terminal()
# Entering username and desired story location

while True:
    username = input("Enter your desired username or hit enter if you do not with to use a username: ")
    if len(username) <= 25:
        print("Username accepted")
        break
    else:
        print("Username too long, please enter a username that is 25 character or less.")
clear_terminal()
print(f"Hello, {username} welcome to the {gamename}!")
clear_terminal()

# Location does not alter storyline.

location = input("Enter the location you wish for the game to be set in. Please enter a city name: ")
sleep(1)
print(f"Your chosen location is, {location}")
clear_terminal()

print("This game is based in 2006.")
sleep(0.5)
# Intro to game demo pt2

print("Before we begin, please note that this is only a demo. This is not the full game")
sleep(0.5)
clear_terminal()
# Storyline begins

fast_type(r"""╔──────────────────────────────────────────────────────────────────────────────╗
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
clear_terminal()
typewriter("You arrive home from that dreadful 9 - 5, feeling, exhausted..... drained")

# deciding whether to eat or not - does not affect storyline
typewriter("You make your way to the kitchen, and open the fridge"
           "\n You see some beers on the top shelf....."
           "\n You drink one."
           "\n You drink another....."
           "\n Next thing you know you have drank 6 or 7 beers..... "
           "\n Now your drunk.")

clear_terminal()

typewriter("You decide to go for a drive."
           "\n Personally I think that isn't a good idea but I am just the narrator so..."
           "\n You get in your car and start it."
           "\n You drive to the gas station to get some snacks..."
           "\n You have the 'bright' idea to stuff the snack down your trousers instead of buying them..."
           "\n The cashier spots you."
           "\n You run to the car and lock the door..."
           "\n You drive as fast as you can to get away...")

clear_terminal()

typewriter("CRASH..."
           "\n You hit something..."
           "\n A parked car?!"
           "\n Really? Wow you must be drunk."
           "\n At least the car was a rental and you gave them a one use only debit card."
           "\n *Thinking to yourself* What do I do? Do I leave the car here? You know what screw it."
           "\n You run the rest of the way home.")

clear_terminal()

typewriter("You head back into the kitchen and put the snacks away in the cupboard."
           "\n You go in the fridge"
           "\nIn the fridge you find a slice of pizza")
answerone = get_choice("Would you like to eat the pizza? (yes/no): ", ["yes", "no"])

if answerone == "yes":
    print("You ate the pizza")
elif answerone == "no":
    print("You did not eat the pizza")
clear_terminal()

typewriter("You walk over to the couch and switch on the TV.")
fast_type(r"""


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

clear_terminal()

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
           "\nYou decide to walk upstairs and make your way to bed."
           "\nIt goes quiet"
           "\nSuddenly...")

print("BANG!!!")
typewriter("You hear running up the stairs"
           "\nYou hear a shout - 'ARMED POLICE!!! YOU ARE BEING ARRESTED ON SUSPICION OF MURDER BY FIREARM'"
           "\nYou look up and see 3 Officers holding you at gunpoint.")

jailtime = 0
answerfour = get_choice("Do you want to resist? yes /no: ",["yes", "no"])
if answerfour == "yes":
    print("STOP RESISTING!!!")
    jailtime = 69
elif answerfour == "no":
    jailtime = 30
else:
    print("Invalid option, please try again")

typewriter("A few days later..."
           "\n A bunch of stuff happens and as the narrator I will not go into too much detail because I am not paid enough."
           "\n To summarise: "
           "\n You woke up in a holding cell, went to court for a trial, you were found guilty."
           f"\n They gave you {jailtime} years in prison"
           f"\n So now.... You are in a prison located in East {location}. How fun!"
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

typewriter("Alright so you goal is to reach to 20 metres deep under your cell..."
           "\n After this you must head north to the nearest sewer..."
           "\n You then need to walk through the sewer until you reach the next manhole cover..."
           "\n After that all you need to do is make it back home from there..."
           "\n Well... Not exactly your home"
           "\n That would be a dumb idea..."
           "\n To escape from prison and to go back to the first place where the police would search"
           "\n You will also need to save up enough money to get out of this area and get a new place..."
           "\n Anyways lets continue with the storyline."
           "\n Okay. Lets start by breaking the tiles below this rug (why is there a rug in prison? idk gng js go with it fr)")

print("*You break the tiles*")

typewriter("Okay now grab the shovel under the bed (the prison guards are a bit dumb dw trust they wont see it)")

print("*You grab the shovel*")

typewriter("Okay lets get digging.")
sleep(1)
dig()
gameoptions()
clear_terminal()
typewriter("Alright so you made it to 20 metres"
 "\n Now you need to head north to the nearest sewer..."
 "\n *You head north*" 
 "\n *You reach the sewer*" 
 "\n *You walk to the nearest manhole cover*"
 "\n *You climb out of the sewer*")
clear_terminal()
typewriter(f"So you have around £{player['Money(£)']} in a duffle bag"
           "\n You should call an uber and get out of here...")
clear_terminal()
typewriter("Thanks for playing the demo of the Untitled Text-Based Adventure Game!")
clear_terminal() 
fast_type(r"""╔──────────────────────────────────────────────────────────────────────────────╗
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
