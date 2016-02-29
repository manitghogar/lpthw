people = 20
cats = 30
dogs = 15

if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"

if people > dogs:
	print "The world is dry!"

dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs:
	print "People are less than or equal to dogs."

if people == dogs:
	print "People are dogs."

if people != cats:
	print "People are dogs, but not cats"

if not(people == cats):
	print "This should output true because it inverts the false statement"

if people == dogs and people == cats:
	print "This statement is false because only one condition is true"

if people == dogs or people == cats:
	print "This statement is true because one of the conditions is true."

if not(people == dogs and people < cats):
	print "This statement is false because it inverts the true statement and therefore this code will not be executed"


""""Study Drills
#1. The code under the if statement is only executes if and only if the IF statement is TRUE.
	(If the condition is true, then do the indented statement. If the condition is not true, then
	skip the indented statement.)
#2. An IF statement, a type of Code Block is defined by its indentation. The code under the IF statement
	is indented four spaces so that it applies directly to the if statement, and once inindented, this ends the code block and the function.
#3. If the code is not indented after the IF statement, you will get an IndentationError: expected an indented block.
	this will now allow the code to run.

"""