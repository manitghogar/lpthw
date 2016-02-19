#variable determining how many types of people there are
x = "There are %d types of people." % 10
#binary is equal to binary
binary = "binary"
#contraction formating
do_not = "don't"
# STRING INSIDE STRING (1)- variables determing those who know binary and those who don't
y = "Those who know %s and those who % s." % (binary, do_not)
#printing the value of x as set above
print x
#printing the value of y as set above
print y
# STRING INSIDE STRING (2) - Variable x will be embedded into the format variable %r
print "I said: %r." % x
# STRING INSIDE STRING (3) Variable Y will replace  the %s format variable in ths string
print "I also said: '%s'." % y
#defining what hilarios is (it is false)
hilarious = False
#defining the evaluation of the joke - there is a format character in this line allowing any variable to be applied here
joke_evaluation = "Isn't that joke so funny?! %r"
# STRING INSIDE STRING  (4) in this line, the hilarious equation takes the place of teh %r format variable 
print joke_evaluation % hilarious
#assigning the value of w
w = "This is the left side of..."
#assigning the value of e
e = "a string with a right side."
#joining the w and e variables forms one long string because of the + function
print w + e


