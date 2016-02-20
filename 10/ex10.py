# escape sequence that creates a tab
tabby_cat = "\tI'm tabbed in."
# escape sequence that creates a new line
persian_cat = "I'm split\non a line."
# escape sequence that creates a backslash
backslash_cat = "I'm \\ a \\ cat."

#by typing ''' in the beginnning and end, all are converted into strings
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# prints the above variabels
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#escape sequence for ' to indicate 6'2 inches
print 'I am 6\'2 tall.'
#testing the difference between %r and %s format characters
print "Hello this is me testing %r with escapes" % tabby_cat
print "Hello this is me testing %s with escapes" % tabby_cat
#testing the difference between %r and %s format characters
print "Let's see how this works with %r" %persian_cat
print "Let's see how this works with %s" %persian_cat