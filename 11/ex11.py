#prints question (argument)
print "How old are you?" ,
#input field for age
age = raw_input ()
#prints argument
print "How tall are you?" ,
#input field for height
height = raw_input()
#prints argument 
print "How much do you weigh?",
#input field for weight
weight = raw_input()
#prints strings with format variables
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)


# raw_input takes input from the user and returns the data input by the user in a string. 

print "What is your Name",
name = raw_input()
print "Where do you go to school?",
school = raw_input()
print "What are you studying?",
major = raw_input()

print "So, your name is %s, you go to %s and you are studying %s." % (name, school, major)

