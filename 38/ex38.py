ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# python - split(ten_things) ~ 'call split with argument ten_things
stuff = ten_things.split(' ')  # - apply split on then_things
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
#while the length of stuff is not equal to ten, run the below function. If the
#length of the function is equal to ten, stop running the function.
while len(stuff) != 10:
    # python - pop(more_stuff) - call the function pop with argument more_stuff
    next_one = more_stuff.pop() # apply pop to more_stuff
    print "Adding: ", next_one
    # python - append(stuff, next_one) - call append with arguments stuff and next_one
    stuff.append(next_one) # apply append with argument next_one to stuff
    print "There are %d items now." %len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
# python - pop(stuff) - call pop with argument stuff. This pops (displays and removes) the last item from stuff
print stuff.pop()  # apply pop on stuff
# python - join(' ', stuff) - call join with arguments ' ' and stuff. This joins the elements in stuff as one long string
print ' '.join(stuff) # what? cool! - apply join with argument stuff to ' '
#join('#',stuff[3:5]) call join with arguments '#' and stuff[3:5]
print '#'.join(stuff[3:5]) # super steller! - apply join with argument(stuff[3:5]) on '#'
print '-'.join(stuff[3:5]) # this is another example of calling join with argument [3:6] on '1'
#This function joins the elements from index 3 upto but not including 6 with a '-' between each element

# Real world examples of things in lists:

example1 = "Hello Bye Yes No Okay Maybe"
list1 = example1.split(' ')
list1.insert(4, "Hello")
print list1

list2 = ['Item1', 'Item2', 'Item3', 'Item4']
list2_1 = ' '.join(list2)
print list2_1

list3 = ['Soccer', 'Basketball', 'Baseball', 'Football', 'Golf']
list3.append("Hockey")
print list3

list4 = ['books', 'computers', 'magazines', 'fans', 'speakers']
print len(list4)
#appends adds the list to the end of the list in question
list4.append(list3)
print list4

list5 = ['dentist', 'doctor', 'therapist', 'psychiatrist']
#extend adds elements of the list directly to the end of the list in question
list5.extend(list3)
print list5

list6 = [5, 6, 7, 8, 9, 10, 11]
print list6[2]
list6.remove(9)
print list6
list6.pop(2)
print list6

list7 = [5, 'six', 7, 'eight', '9', 'ten']
print list7.index('six') # returns the index number of the element passed to the function

list8 = ['utilities', 'rent', 'electricity', 'cable', 'rent']
print list8.count('rent') #counts the number of times an element appears in the list

list9 = ['iphone', 'mac', 'ipod', 'ipad']
list9.sort()
print list9

list10 = ['samsung', 'apple', 'nokia', 'LG']
list10.reverse()
print list10

add_this = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
#while the length of list1 is less than 12, add the last remove and add
while len(list1) != 12:
    next_one = list4.pop()
    print "Adding: ", next_one
    list1.append(next_one)
    print "the length is now %d" % len(list1)
    print list1
