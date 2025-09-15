import time
import sys
from time import sleep

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

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
print("Hello, and welcome to the ", gamename,"!")
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
print("Hello, ",username,", welcome to the ", gamename,"!")
sleep(0.5)

#Location does not alter storyline.

location = input("Enter the location you wish for the game to be set in. Please enter a city name: ")
sleep(1)
print("Your chosen location is ", location)
sleep(0.5)

#Intro to game demo pt2

print("Before we begin, please note that this is only a demo. This is not the full game")
sleep(0.5)

#Storyline begins

print("""╔──────────────────────────────────────────────────────────────────────────────╗
│ _____ _            _   _       _   _ _   _          _                        │
│|_   _| |__   ___  | | | |_ __ | |_(_) |_| | ___  __| |                       │
│  | | | '_ \ / _ \ | | | | '_ \| __| | __| |/ _ \/ _` |                       │
│  | | | | | |  __/ | |_| | | | | |_| | |_| |  __/ (_| |                       │
│ _|_|_|_| |_|\___|  \___/|_| |_|\__|_|\__|_|\___|\__,_|                       │
│|_   _|____  _| |_     | __ )  __ _ ___  ___  __| |                           │
│  | |/ _ \ \/ / __|____|  _ \ / _` / __|/ _ \/ _` |                           │
│  | |  __/>  <| ||_____| |_) | (_| \__ \  __/ (_| |                           │
│  |_|\___/_/\_\\__|    |____/ \__,_|___/\___|\__,_| ____                      │
│   / \   __| |_   _____ _ __ | |_ _   _ _ __ ___   / ___| __ _ _ __ ___   ___ │
│  / _ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ | |  _ / _` | '_ ` _ \ / _ \│
│ / ___ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/ | |_| | (_| | | | | | |  __/│
│/_/   \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|  \____|\__,_|_| |_| |_|\___|│
╚──────────────────────────────────────────────────────────────────────────────╝""")
typewriter("You arrive home from that dreadful 9 - 5, feeling, exhausted..... drained")

#deciding whether to eat or not - does not affect storyline
typewriter("You make your way to the kitchen, and open the fridge")
typewriter("In the fridge you find a slice of pizza")
while True:
    answerone = input("Would you like to eat the pizza? (yes/no): ")
    if answerone == "yes":
        print("You ate the pizza")
        break
    elif answerone == "no":
        print("You did not eat the pizza")
        break
    else:
        print("Invalid option. Please enter yes or no.")

typewriter("You walk over to the couch and switch on the TV.")
print("""%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
*                                        +:                 ==                                      
*                                         =:               ==                                       
*                                         .+:             -+                                        
*                                          .+:           :+                                         
*                                           .*.         -=                                          
*                                            .+.       -=                                           
*                                              +:     ==                                            
*       :#####%##############################################################################*      
*       :##%%%#%%#%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@#*      
*       :##%=:=#+++++++++++++++++++*+*******************************#=::%%#%#%#%#%#%#%%%%%%%#*      
*       :##%=-*#%#***+++++=========================++++*********##%#+*::#*=-----=-------==%%#*      
*       :##%=-*#*--*%%@@@%@%%%%%%#***%@%@%%%%%%@%%%%##%%%%@@@@%%+==*=*:.%+-=*%#++--:-=----%%#*      
*       :#*%--*#*-%%*****+*******+**%*#***###**#*=-=--====++***#@%=*=*:.%==*#=-=#==:*-+=:-%%#*      
*       :#*%--**+=@#**+++++*===****##++*****==-=**-------===+**%%@=*=*:.%+=#%=+##---++*=--%%#*      
*       :##%--**==@*++=++**++******#=---==---::::*------====++**%@=+=*:.#+--+*+==--------=%%#*      
*       :##%--**=+%*+++===+********#+-=====--::::*=---=======*##%@===*:.#%%#####%%#%%%%%%#%%#*      
*       :##%--**=*%*++##**#********==-======-=-::+=---==-=====*%%@===*:.#%######%#%#%###%%%%#*      
*       :##%--**-*%%*+**#**********=-=+*=#==**--:-=***-=**==*####@===*-.#%*=:::-*#%*=:::=#%%#*      
*       :##%--**-*%####***++********---=+=-:-=-::=****+****+*####%===*-.#%*:---:=%#+::-::=%%#*      
*       :##%--**-*%#####*=-=:-+*****======-:--:::**************##%===*-.#%#*-::-*%%#*-::=#%%#*      
*       :*#%--**=#%###***=-----=-****=======-:-:+**************##%+==*-:%%#####%#%%%%##%%%%%##      
*       :##%--**=#%##*****==----=****+==+=++=--+*+***************%+==*-:%%%%%%%%%%%%%%%%%%%%##      
*       :##%-=**=#%**#*****=--=#%%%%%%:++===--:###%%%********====#+==*-:%%%%%%%%%%%%%%%%%%%%##      
*       :##%==**=#%*#*#**#%%%%%%%%%%%%=-=***-::%%%%%%%%%%%#**=+++#+==#=:%%%%%%%%%%%%%%%%%%%%##      
*       :##%==**=#%*#***%%%%%%%%%%%%%%*:-#%#:::%%%%%%%%%%%%%*****%+==*=:%%#######%#%%#%%%#%%##      
*       :##%==**+*%###*#%%@%%%%%%%%%%%%=*%%*=+=%%%%%%%%%%%%%#***#%++=#=:%%######%%#%%%%%%%%%##      
*       :##%==**+*%****%%@@@%@%%%%%%%%%=-*%#::*%%%%%%%%%%%%%%#**#@+=+*=:%%%%%%%%%%%%%%%%%%%%##      
*       :##%==#*+*%***#@@@@@@%%%%%%%%%%*-%%%+-#%%%%%%%%%%%@%%%###@+=+*=-%%%%%%%%%%%%%%%%%%%%##      
*       :##%==#**+@###%@@@@@@@%%%%%%%%%#=%%%%-%%%%%%%%%%%%@%%%%#%@=++*=-%%%%%%%%%%%%%%%%%%%%##      
*       :##%==***+@%*==+==:*:==*:+*:==-=:+-+:::**:==*:==:*:*+=+*%@=*+*=-%%%%%%%%%%%%%%%%%%%%##      
*       :##%==#**=%@**=*-+=*:**:::-::*:*:::=-::**:=:*:**=-=-*=+*@#=*+*=:%#################%%##      
*       :##%==**#==+*###%%%%%%%%##################%#%%%%%%#####*===*+*=:%#######%##%%%##%%%%##      
*       :##%==**%*********+++++===================+=++++++**+*****##+*=:%%###%%%%%%%%%%%%%%%##      
*       :##%=:=***********************#***#**************************=--%%%%%%%%%%%%%%%%%%%%#*      
*       :##%%%%%##########%%%%#%%#%%%#######%%%#%%%#%%#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*      
*       :##*****#*##*###********#**********#***#******#*######################%#########*####*      
*           ..:=*#%%%%%@%%@%@%@%@%@%@%@%%%%%%%%%%%%%%%%%%%%%@%@%@%@%@@@@@%@@@@%@@@%%%*+=:.          
*       ..:::--========++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=====-::..       
*                                                                                                   
*                                                                                                   
*                                                                                                   """)
#Choosing a tv channel - Does not affect storyline
while True:
    answertwo = input("What channel do you want to watch? E4 or ITV? ")
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

typewriter("You sit and watch TV for a few hours.... Falling asleep on the couch")
typewriter("You wake up suddenly..... To the sound of a loud banging.")
typewriter("It seems to be coming from the front door?")

while True:
    answerthree = input("Do you walk to the door to check it out? yes / no? ")
    if answerthree == "yes":
        typewriter("You walk to the door. And you peek through the peephole. You see..... ARMED police?!")
        break
    elif answerthree == "no":
        typewriter("You stay put.")
        break
    else:
        print("Invalid option, please try again")

typewriter("*Thinking to yourself* Maybe its best I dont open the door. Whoever is out there seems really aggressive.")

if answerthree == "yes":
    typewriter("You walk back to the couch")

