#sets the value of the variable 'formatter' to four %r format characters
formatter = "%r %r %r %r"
#assigns values 1,2,3,4 to the formatter
print formatter % (1, 2, 3, 4)
#assings 4 strings from one to four to the formatter
print formatter % ("one", "two", "three", "four")
#assigns 4 booleans to the formatter
print formatter % (True, False, False, True)
#assigns the formatter variable four times into the formatter
print formatter % (formatter, formatter, formatter, formatter)
#assigns four strings to the formatter
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight.")

