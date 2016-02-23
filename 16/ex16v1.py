from sys import argv

script, filename = argv

print "Opening the file.."
target = open(filename, 'r')

#characters = int(raw_input("How many characters do you want? "))

print target.read()



