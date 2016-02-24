from sys import argv

script, first, second, third = argv

print "the script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

"""
error if not enought arguments are given:
ValueError: need more than 3 values to unpack
The error occurs because I give it fewer than 
three arguments, it needs all three to unpack the arv successfully. .
"""

#script 2 with 3 arguments

from sys import argv 

script, first, second = argv

print "the script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second


#script 3 with 6 arguments

from sys import argv

script, first, second, third, fourth, fifth = argv

print "the script is called", script
print "the first variable is called:", first
print "the second variable is called:", second
print "the third variable is called:", third
print "the fourth variable is called:", fourth
print "the fifth variable is called:", fifth

#combine raw_input with argv

from sys import argv

script, first, second, third = argv
fourth = raw_input("What is the fourth input? ")
fifth = raw_input("What is the fifth input? ")

print "the script is called", script
print "the first variable is called:", first
print "the second variable is called:", second
print "the third variable is called:", third
print "the fourth variable is called", fourth
print "the fifth variable is called:", fifth 



