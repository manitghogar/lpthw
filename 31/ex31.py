"""
print "You enter a dark room with three doors. Do you go through door #1, door #2 or door#3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
	print "You drop into a black empty elevator shaft. How do you react?"
	print "1. You reach out to grab an elevator chain."
	print "2. You dive head first and accept your faith."
	print "3. You pray and hope for the best"

	elevator = raw_input("> ")

	if elevator == "1" or elevator == "3":
		print "You are safe"
	elif elevator == "2":
		print "you fall into a bed of foam"
	else:
		print "you are definitely dead"

else: 
	print "You stumble around and fall on a knife and die. Good job!"

"""

#My game

print "this is a game that I am going ot create. In this game we face two options. Option 1 and Opton 2. What do you choose?"
option = raw_input("> ")

if option == "1":
	print "You will be presented with three vacation options:"
	print "1. Go to egypt"
	print "2. Go to africa"
	print "3. Go to Thailand"

	vacation = raw_input()

	if vacation == "1" or vacation == "2":
		print "Have fun, great country"
	else:
		print "Good luck in Bangkok"

elif option == "2":
	print "You will be presented with two activity options:"
	print "1. Go bungee jumping"
	print "2. Go sky diving"

	activity = raw_input("> ")

	if activity == "1":
		print "Nice choice"
	elif activity == "2":
		print "daredevil we got over here"
	else:
		print "boring"

else:
	print "%r is not a valid option" % option

	





