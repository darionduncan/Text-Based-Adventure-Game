from time import sleep
#loadingscreen
print("Initializing...")
sleep(1)
load = 0
print("Loading - ", load, "%")
sleep(0.5)
while load <= 99:
    load = load+ 25
    print("Loading - ", load, "%")
    sleep(0.3)
print("Loading - Complete!")
sleep(0.3)

#Introduction to Game Demo

gamename = "Untitled Text Based Adventure Game"
print("Hello, and welcome to the ", gamename,"!")
sleep(0.5)
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
print("Before we begin, please note that this is only a demo. This is not the full game")
sleep(0.5)

