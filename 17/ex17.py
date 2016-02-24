#imports argv from sys
from sys import argv
#imports exists command form os.path
from os.path import exists
#selecting command line arguments that will be passed onto the script
script, from_file, to_file = argv
# lets the users know that we are copying strings from one file to the other file
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
#in_file = open(from_file)
# indata opens the first file and then reads it. 
indata = open(from_file).read()
# reads how many characters are in the first file
print "The input file is %d bytes long" % len(indata)
# confirms that the second file exists
print "Does the outpout file exist? %r" % exists(to_file)

print "Ready, hit RETURN to continue, CTRL-C to abort"
# if it exits, users hit return to continue
raw_input()

#out_file = open(to_file, 'w')
#out_file.write(indata)

#this open the second file in write mode and the overwrites it with the infromation contained 
# in indata which is the first file that is open and read.

open(to_file, 'w').write(indata)

# confirming that the action is done.

print "Alright, all done."

#out_file.close()
#in_file.close()


