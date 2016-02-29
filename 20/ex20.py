#imports argv from system
from sys import argv
#passes two arguments python: the script name and the input)file that the function needs to run
script, input_file = argv
#this function prints the input file for users to read
def print_all(f):
	print f.read()
#rewinds the pprogram to the start of the input file.
#seek() moves the pointer to some part of the file so you can start reading or writing at that place.
#seek(0) moves the pointer to the beginning of the first line. So we can start reading from the start of the file.
def rewind(f):
	f.seek(0)
#this function takes in the line count and the input file. 
#And then it outputs that specified line number and the corresponding line that we want to read.
def print_a_line(line_count, f):
	print line_count, f.readline()
#opens the input file and assigns that action to the current_file variable.
current_file = open(input_file)
#Here we tell users that we are going to print the whole file.
print "First let's print the whole file:\n"
#utilizes the first function. 'print_all' takes in a file. So we feed it the opened input file.
#The function is executed - it reads the open file and prints it for users to see.
print_all(current_file)
#tells the users that we are going to go back to the start of the file.
print "Now let's rewind, kind of like a tape."
# the rewind fucntion is executed - we apply seek(0) to the opened input file.
rewind(current_file)
#now that we are back at the start of the first line of the file, we will print the three lines again, but this time individually.
print "Let's print three lines:"
#here we set that current_line = 1 and then we feed the current_line variable, and the opened input file to the 
#print_a_line function. The function is run and the current_line count is printed, and that corresponding line is printed.
current_line = 1
print_a_line(current_line, current_file)
#the current_line variable is adjusted by adding 1 to it. The new current_line variable is then passed to the function
#along with the opened input file in the form of the current_file variable. 
"""current_line = current_line + 1"""
current_line += 1
print_a_line(current_line, current_file)

"""current_line = current_line + 1"""
current_line += 1
print_a_line(current_line, current_file)


# += adds the right operand to the left operand and assings the result to the left operand.
# c += a is equivalent to c = c + a


