"""hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1,2,3,4]
"""
#creates the list
the_count = [1,2,3,4,5]
#creates the list
fruits = ['apples', 'oranges', 'pears', 'apricots']
#creates the list
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# this forloop defines 'number' internally as each number in the list and then outputs a string contianing 
# each number in the list. Each iteration of the forloop goes through the list from start to finish.
for number in the_count:
	print "This is count %d" % number

# same as above
for fruit in fruits:
	print "This is fruit %s" % fruit

# also we can go through mixed lists too
# notices we have to use %r since we don't know what's in it
# for each index in the change list, output the below sentence for each index item in the list from start to finish.
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one
elements = [1,2]
#appends the range (0,1,2,3,4,5) to the empty list called elements.
elements.append(range(0,6))

for i in range(0,6):
	print "Element was: %d" % i

"""
# then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)
"""

#The range function geerates a list of numbers. 
#range([start],[stop], [step])
#start: starting number of the sequence.
#stop: Generate numbers up to, but no tincluding this number.
#step: Difference between each number in the sequence.
#The range function is usually used to iterate over with for loops. 

"""
Other operations on lists:
	- List.insert
	- List.append
	- len(list)
	- list.extend
	- list.remove
	- list.pop
	- list.index
	- list.count
	- list.sort
	- list.reverse
"""
