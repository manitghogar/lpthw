people = 10
cars = 5
trucks = 35
"""
if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide"

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
	"""

#elif is short for else if, and is run if the first statement is not true.
#elif only exists after an if statement.

#else are it executed if the above if and elif statements are not true.
#So for instance, if all the above statements are false, then run this statement.


if cars > people and trucks > cars:
	print "We should take the cars, as there are too many trucks"
elif cars < people and trucks < cars:
	print "We should not take the cars, let's just take the trucks"
elif people >= trucks:
	print "Let's just take the trucks"
else:
	print "Let's stay home"

