from sys import exit

def start():
    print "You are presented with two curtains, curtain 1 and curtain 2, behind which lie two extremely different worlds."
    print "Pick a curtain:"
    choice = raw_input("> ")
    if "1" in choice:
        curtain_1()
    elif "2" in choice:
        curtain_2()
    else:
        print "PICK A CURTAIN"
        start()

def curtain_1():
    print "You push the curtain aside, and enter a room. You notice two tubes, with the sound of water behind them both."
    print "Pick a tube"
    tube = raw_input("> ")
    if "1" in tube or "one" in tube:
        tube_1()
    elif "2" in tube or "two" in tube:
        tube_2()
    else:
        dead("If you can't count, you don't deserve to play this game")

def curtain_2():
    print "You push the curtain aside and you notice two doors. Both doors have trees creeping through its edges."
    print "Pick a door"
    door = raw_input("> ")
    if "1" in door or "one" in door:
        door1()
    elif "2" in door or "two" in door:
        door2()
    else:
        dead("If you can't count, you don't deserve to play this game")

def tube_1():
    print "You slide down the first tube, and fall into the center of an ocean."
    print "There is no sight of land, you are alone and cold."
    print "You hear movement around you, and you quickly turn, there are three creatures staring you in the eyes."
    print "A Shark, a Dolphin, and a Whale."
    print "Pick one to fight, and the others will leave you alone."
    ocean_animal = raw_input("> ")
    if "shark" in ocean_animal:
        dead("The shark eats your head, you're dead.")
    elif "whale" in ocean_animal:
        print "The whale doesn't move, what do you do?"
        print "Do you swim away, or do you try and speak whale?"
        whale = raw_input("> ")
        if "swim" in whale:
            print "The whale is lazy. You have escaped."
            print "You see an underground tunnel, do you swim away or do you enter it?"
            underground_tunnel = raw_input("> ")
            if "swim" in underground_tunnel:
                dead("You run out of breath, and you die.")
            elif "enter" in underground_tunnel or "tunnel" in underground_tunnel:
                lake()
            else:
                dead("You took too long to decide, you are dead.")
        elif "speak" in whale or "whale" in whale:
            dead("The whale destroys you. You are now dead.")
        else:
            print "You need to learn how to decide"
            exit(0)
    elif "dolphin" in ocean_animal:
        dolphin()
    else:
        ocean_animal

def dolphin():
    print "You can either swim towards the dolphin and grab its fin, or flee away in fear."
    print "What do you decide?"
    chose_dolphin = raw_input("> ")
    if swim in chose_dolphin:
        print "You swim with the dolphin to land, and you are safe. You are victorious."
        exit(0)
    elif flee in chose_dolphin:
        dead("The dolphin chases you, and shreds you up.")
    else:
        dolphin()

def dead(why):
    print why, "Good Job!"
    exit(0)

def tube_2():
    print "You jump into the tube and start sliding in what is a very long slide."
    print "You fall and hear big splash."
    lake()

def lake():
    print "You have fallen into a lake in sub-saharan africa."
    print "You are instantly faced by a crocodile and a hippo"
    print "Do you pray to God or do you swim towards the waterfall"
    choice = raw_input("> ")
    if "pray" in choice or "God" in choice or "god" in choice:
        dead("God helps those who help themselves. You are dead.")
    elif "swim" in choice or "waterfall" in choice:
        print "Both the crocodile and the hippo start chasing you."
        print "Just as they near your feat, you jump down the waterfall"
        print "You are in free fall and soon hit the bottom of the river."
        print "You look up and see the crocodile and hippo falling above you"
        print "Do you keep staring, or do you swim to the near by bank?"
        second_choice = raw_input("> ")
        if "stare" in second_choice or "staring" in second_choice:
            dead("You are crushed.")
        elif "swim" in second_choice:
            print "You are safe. You crawl your way deeper into land, and you are happy."
            forest()
        else:
            dead("That is not possible. You are dead.")
    else:
        dead("That's not possible. You are dead.")

def forest():
    print "You are surrounded by trees, more trees, and some more trees."
    print "You hear some movement. You look up and see a bear and a tiger."
    print "Who do you fight?"
    choice = raw_input("> ")
    if "bear" in choice or "Bear" in choice:
        bear()
    elif "tiger" in choice or "Tiger" in choice:
       tiger()
    else:
        forest()

def tiger():
    dead("The tiger charges at you and tears you up into pieces. You're dead.")

def bear():
    print "You can either run towards the bear, or play dead. What do you do?"
    choice = raw_input("> ")
    if "run" in choice:
        print "The bear runs away."
        print "You stand their victorious. You have survived. Do you rest or do you walk?"
        choice1 = raw_input("> ")
        if "rest" in choice1:
            tiger()
        elif "walk" in choice1:
            tiger()
        else:
            bear()
    elif "dead" in choice or "play" in choice:
        print "The bear snifs you, and walks away."
        print "You get up victorious. You have survived. As you being to walk"
        tiger()
    else:
        dead("You have taken too long to decide. You are dead.")

def door1():
    print "You push the door wide open, and you walk through the frame."
    print "The next thing you know."
    forest()

def door2():
    print "You push the door open. You walk through the frame and"
    darkroom()

def darkroom():
    print "You enter a dark room. A very dark room."
    print "You hear sounds. As you put your right foot forward, you slip, but you do not fall."
    print "It is a cliff. The sound gets louder as you feel something coming close."
    print "Do you jump, or do you wait?"
    choice = raw_input("> ")
    if "jump" in choice:
        lake()
    elif "wait" in choice:
        dead("You die in a stampede. Should have jumped.")
    else:
        dead("Man, learn to decide. You are dead.")


start()
