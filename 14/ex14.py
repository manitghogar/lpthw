
#importing argv from sys
from sys import argv 
#unpacking argv into three variables v0, v1 and v2
script, user_name, birth_country = argv
#setting a consistent prompt that shows up everytime a question is asked
prompt = '>>'
#strings that use the argv arguments 
print "Hi %s of %s, I'm the %s script." % (user_name, birth_country, script)
#string
print "I'd like to ask you a few questions."
#string questions using argv argument
print "Do you like me %s?" % user_name
#prompt to answer the question
likes = raw_input(prompt)
#string questions using argv variable
print "Where do you live %s?" % user_name
lives = raw_input(prompt)
#string question
print "What kind of computer do you have?"
computer = raw_input(prompt)
#string question
print "What is your favourite food"
food = raw_input(prompt)

print """
Alright, so you said %r about liking me. 
You live in %r. Not sure where that is. 
But what I do know is that you like %r just like me.
And you have a %r computer. Nice.
""" % (likes, lives, food, computer)

