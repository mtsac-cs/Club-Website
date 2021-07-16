# Strings
########### Notes taken are following the Python and Django Full Stack Web Developer Bootcamp on Udemy.com
########### URL: https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/

## Can use single quotes or double quotes

### Basics
print('hello')              # single quotes
print("hello")              # double quotes

### Indexing
mystring = 'abcdefg'
print(mystring)             # this prints out the whole string

print(mystring[3])          # this prints out the character at specific index: output 't'
print(mystring[-1])         # python supports negative indexing, so this will return 'g'

### Slicing
print(mystring[2:])         # to print everything from 'c' all the way to the end, append a colon to indexer: 'cdefg'
print(mystring[:3])         # to print everything up until but not including the index, prefix with a colon: 'abc'
print(mystring[2:5])        # finally, we can select a range from an index up to and not including another index: 'cde'
print(mystring[:])          # we simply use a single colon to print everything in string array
print(mystring[::2])        # use two colons followed by a stepsize. for example, 2 would print every other character: 'aceg'
print(mystring[::-1])       # will return a reversed string by calling a negative stepsize

# Strings are Immutable

# mystring = 'X'            <-- This is impossible because we cannot reassign individual characters.  We would have to reassign the whole string.

### Basic Methods
x = mystring.upper()        # convert to upper case: 'ABCDEFG'
print(x)
y = mystring.capitalize()   # capitalizes the first letter of the string: 'Abcdefg'
print(y)
mystring = 'Hello World'
z = mystring.split()        # splits a string into a list using space as a delimiter: ['Hello', 'World']
print(z)                    # by the way,  python allows you to print out a whole list without iteration
z = mystring.split('e')     # we can also change the delimiter to whatever we want: ['H', 'ello World']

### Print Formatting

# Using string interpolation: inserting a string into another string
x = "Insert another string here: {}".format("INSERT ME!")
print(x)                    # this outputs: Insert another string here: INSERT

# Inserting multiple strings
x = "Item One: {} Item Two: {}".format("dog", "cat")
print(x)

# Inserting variables into string
x = "Item one: {a} Item Two: {b}".format(a = "dog", b = "cat")
print(x)