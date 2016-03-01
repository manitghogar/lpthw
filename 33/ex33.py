

print "What is your upper limit"
upperlimit = int(raw_input("> "))
print "And what is your increment?"
increment = int(raw_input("> "))

def number_function(upperlimit, increment):
    i = 0
    numbers = []
    while i < upperlimit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

#print number_function(upperlimit, increment)


def number_function2(upperlimit):
    numbers = []
    for i in range(0,upperlimit):
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

print number_function2(upperlimit)


