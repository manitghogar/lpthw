#imports the exit command from systems as a way to end the game.
from sys import exit

# you finally enter the gold room after the bear room.
def gold_room():
    #The user is prompted to choose how much gold he wants.
    print "This room is full of gold. How much do you take?"
    choice = raw_input("> ")
    # this try function converts the raw input into an integer, and if that does not
    #output an error message as the user really typed in an integer, then it attributes that integer to the how_much variable.
    try:
        int(choice)
        how_much = int(choice)
    #if the user typed in a string then python converts the error message into a friendly message and ends the game.
    except ValueError:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    elif how_much > 10000:
        dead("Unbelievable, we don't have enough gold")
    else:
        dead("You greedy bastard!")
#Users enter the bear room if they picked the left door.
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    #infinite loop as long as it is true.
    while True:
        #prompts users to choose how they aer going to move the bear
        choice = raw_input("> ")
        #if they choose to take the bears honey, then they end up dead. The game ends.
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        #Or else if they choose to taunt the bear, and the bear moves as (not false = true), this means that the and statement outputs true and the function continues to run.
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
        # here the variable bear_moved has been set to true.
            bear_moved = True
        # here, if both statements are true then the function is over and the game ends.
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        # here the if both statements are true, then the person enters the gold room and the game continues.
        elif choice == "open door" and bear_moved:
            gold_room()
        # if something other than the valid inputs were entered, you are prompted to try again.
        else:
            print "I got no idea what that means."
#This is the room users enter if they pick the right door.
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life, eat your head or shoot the monster?"
    #prompted to choose whether to flee or to eat your own head
    choice = raw_input("> ")
    #if they choose to flee, they start again at the start of the game
    if "flee" in choice:
        start()
    #if they eat their own head, the game ends.
    elif "head" in choice:
        dead("Well that was tasty!")
    elif "shoot" in choice:
        dead("The monster eats your bullet and kills you.")
    #If their answer is not valid, they are prompted to choose again.
    else:
        cthulhu_room()
#this function ends the game. The argument that it takes in is the reason that the game should end, and
#is a result of the player not folllowing previous instructions. It appends a 'Good Job' to the end of the string, and then ends (exits) the game.
def dead(why):
    print why, "Good job!"
    exit(0)

#This function starts the game. Prompts user to pick a door.
def start():
    print "You are in a dark room."
    print "There is a door to your right and left"
    print "Which one do you take?"
    #user picks a door
    choice = raw_input("> ")
    #if he picked the left door, he enters the bear room
    if choice == "left":
        bear_room()
    #if he picked the right door he enters the cthulhu room
    elif choice == "right":
        cthulhu_room()
    #if he did not pick left or right, he starves.
    else:
        dead("You stumble around the room until you starve.")

#function that starts the game
start()
