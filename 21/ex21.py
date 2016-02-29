#this function adds two arguments passed to the function. The output for one prints the action of the function
#the second is htat it returns the sum of the two variables. 
#When this function is assigned to a variable, the outcome of the return actio will be assigned to the variable.n 
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
#subtracts the two arguments passed on to the function
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
#multiply two arguments passed to the fucntion.
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
#divides the two arguments passed ot the function
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"
#we assign the outcoms of the above functions to variables so that they can be used in additional functions.
age = add(40,5)
height = subtract(80,4)
weight = multiply(90,2)
iq = divide(110,2)Computer2241

#This string takes in the value of the above variables. These values are determined by the return portion of the above functions.
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle."
#this function takes the above variables, and does operations on them. It outputs both the
#strings as well as the final numeric value as part of the function.
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print what
#function written out in numbers
hello = (74 - ((50 / 2) * (180))) + 35
print hello
#function written out using the same variables
once_again = (height - ((iq / 2) * weight)) + age
print once_again


#myfunction
watches = add(5,8)
cars = subtract(10,6)
houses = multiply(2,2)
guards = divide(18,3)

print "He has %d watches, %d nice cars, %d houses on the hill and %d guards in total" % (watches, cars, houses, guards)

puzzle_1 = add(houses, multiply(subtract(guards, houses), divide(watches,cars)))

print puzzle_1




