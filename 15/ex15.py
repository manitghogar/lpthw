#import argv from sys
from sys import argv
#unpack argv into script and filename
script, filename = argv
#the function of text is to open the file name specified on the command line
txt = open(filename)
#format variable r is determined by the file name specified on the command line
print "Here's your file %r:" % filename
# applying the read function to the txt command which is opening th efile name
print txt.read()
#Asks a question

#This code is a better way to get the script as it 

print "Type the filename again:"
#prompts user to enter the name of the file and assigns that value to "file_again"
file_again = raw_input("> ")
#opens the file that the user specifies and assigns that command to text_again
txt_again = open(file_again)
#executing the txt.again command by applying the read action to it.
print txt_again.read()