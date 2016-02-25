print "Let's practice everything."
print 'You\'d need to know \'bout escpaes with \\ that do \n new lines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovelynor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

#prints the value of the poem
print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five
#function that takes in a starting value and outputs a value for jelly beans, jars and crates
#based on the formulas specified in the function.
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
#setting the starting point to 10000
start_point = 10000
#setting each of the three outputs of the function to a variable.
beans, jars, crates = secret_formula(start_point)
#printing the output of the function at a starting point of 10000.
print secret_formula(start_point)
print beans, jars, crates
print jars
#assings the variable values to the format characters in the string 
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)
#divides the initial starting point by 10 to use as the argument for this function.
start_point = start_point / 10
#as the function outputs three values, it is sufficient to assign the return outputs to the format characters.
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)


