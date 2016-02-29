#imports argv from system
from sys import argv
#unpacks the list of command line arguments (argv) - passes two arguments 
#python script. Script is always the first and filename is the second in this case.
script, filename = argv
#prints statement applying the name of the file to the format variable int he string
print "We're going to erase %r." % filename
#users are given the option to end the function
print "If you don't want that, hit CTRL-C (^C)."
#users are given the option to proceed
print "If you do want that, hit RETURN."
#this is where users type in the command to halt the function or continue
raw_input("?")
#prints the action: lets users know that the file is being opened
print "Opening the file..."
#open the file in 'write' mode so that things can be added to it.
target = open(filename, 'a')
#tells users that it is currently empyting the file.
print "Truncating the file. Goodbye!"
#performing the action: emptying the file.
#target.truncate()
#tells the user that it is going to ask them for three lines for it to add.
print "Now I'm going to ask you for three lines."
#three lines that users input one after the other.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#lets users know that they are going to write those three lines onto the now empty file
print "I'm going to write these to the file."
#writes line 1 to target (which is the opened file in write mode) 
#target.write(line1)
#creates a new line in the file
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")
add_lines = "%s\n%s\n%s" % (line1, line2, line3)
target.write(add_lines)
#lets users know that they are going to close the file
print "And finally, we close it."
#closes the file that was open for editing
target.close()


#opening with w means that the file now becomes writable (editable)
#it looks like w overwrites the file of its original contents so it is not important to truncate (empty) it
#if we used the append function isntead of the write function, then 
#the new text would not have overwritten the orignial content but would have added to it.


