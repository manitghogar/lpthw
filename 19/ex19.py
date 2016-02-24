#defines the function cheese_and_crackers which takes in two arguments. 
"""
def cheese_and_crackers (cheese_count, boxes_of_crackers):
	#The function outputs the number of cheeses in a senetence depending on argument passed to it.
	print "You have %d cheeses!" % cheese_count
	#The second outpout line is the number of cracker boxes depending on the argument of cracker boxes passed to it.
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#The third and fourth line are strings
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

#feeding the function pure numbers, one that represents the cheese count and the other that represents the boxes of crackers.
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)
#feeds the function variables that we set for the cheese count and boxes of crackers.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#we feed the function pure math, one for the amount of cheese and the other for the box of crackers.
print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)
#we feed the function a combination of a variable and math, once again representing 1. amount of cheese and 2. the box of crackers.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
"""
def soccer_and_basketball (number_of_soccer_balls, number_of_basketballs):
	print "We currently have %d soccer balls" % number_of_soccer_balls
	print "We also happen to have %d basketballs" % number_of_basketballs
	print "in total we have %d balls" % (number_of_soccer_balls+number_of_basketballs)
	print "Damn, thats alot of balls!"

#1
soccer_and_basketball(10,12)
#2

soccer_balls = 50
basketballs = 100
soccer_and_basketball(soccer_balls, basketballs)
#3
soccer_and_basketball(5+8, 6+2)
#4
soccer_and_basketball(soccer_balls, 8-2)
#5
soccer_and_basketball(6+2, basketballs)
#6
soccer_and_basketball(soccer_balls+9, basketballs+2)
#7
user_input_soccer_balls = int(raw_input("How many soccer balls are there? "))
user_input_basketballs = int(raw_input("How many basketballs are there? "))
soccer_and_basketball(user_input_soccer_balls, user_input_basketballs)




