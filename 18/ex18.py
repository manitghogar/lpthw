"""
Functions do three things:
	- They name pieces of code the way varibles name strings and numbers.
	- They take arguments the way your scripts take argv.
	- Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."
"""
# this one is like your scripts with argv 
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# okay, that *args is actually pointless, we can just do this 
#The function 'print_two_again' takes in two arguments (arg1 and arg2)
def print_two_again(arg1, arg2):
	#what the function does is it prints the first argument and then prints the second argument
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()


