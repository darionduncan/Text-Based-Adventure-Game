#importing
import time
import sys
from time import sleep
#defining functions
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

#loadingscreen
print("Initializing...")
sleep(1)
load = 0
print("Loading - ", load, "%")
sleep(0.5)
while load <= 99:
    load = load+ 25
    print("Loading - ", load, "%")
    sleep(0.2)
print("Loading - Complete!")
sleep(0.3)

#Introduction to Game Demo
gamename = "Untitled Text Based Adventure Game"
print(f"Hello, and welcome to the {gamename}!")
sleep(0.5)

#Entering username and desired story location

while True:
    username = input("Enter your desired username: ")
    if len(username) <= 25:
        print("Username accepted")
        break
    else:
        print("Username too long, please enter a username that is 25 character or less.")

sleep(1)
print(f"Hello,{username} welcome to the {gamename}!")
sleep(0.5)

#Location does not alter storyline.

location = input("Enter the location you wish for the game to be set in. Please enter a city name: ")
sleep(1)
print(f"Your chosen location is, {location}")
sleep(0.5)

print("This game is based in 2006.")
sleep(0.5)
#Intro to game demo pt2

print("Before we begin, please note that this is only a demo. This is not the full game")
sleep(0.5)

#Storyline begins

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

#deciding whether to eat or not - does not affect storyline
typewriter("You make your way to the kitchen, and open the fridge"
           "\nIn the fridge you find a slice of pizza")
answerone = get_choice("Would you like to eat the pizza? (yes/no): ", ["yes", "no"])

if answerone == "yes":
        print("You ate the pizza")
elif answerone == "no":
        print("You did not eat the pizza")

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
#Choosing a tv channel - Does not affect storyline
answertwo = get_choice("What channel do you want to watch? E4 or ITV?", ["E4", "ITV"])
if answertwo == "E4":
    typewriter("*TV Plays* The Simpsons")
else:
    typewriter("*TV Plays* Family Guy")

typewriter("You sit and watch TV for a few hours.... Falling asleep on the couch"
           "\nYou wake up suddenly..... To the sound of a loud banging."
           "\nIt seems to be coming from the front door?")
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

while True:
    jailtime = 0
    answerfour = input("Do you want to resist? yes/no? ")
    if answerfour == "yes":
        jailtime = 67
        break
    elif answerfour == "no":
        jailtime = 30
        break
    else:
        print("Invalid option, please try again")
