################ Regular Expressions

# Regular expressions: allow us to search for patterns in Python strings
# will help us parsing through URLs in Django

#########
# Match #
#########

# import re for regular expressions
import re

# Our terms we want to search for
patterns = ['term1', 'term2']

# The string we want to parse
text = 'This is a string with term1, but no the other!'

# A for loop to look through the string
for pattern in patterns:

    # I'm searching for: term1, term2, etc
    print("I'm searching for: " + pattern)

    # If a match is found, return MATCH!
    if re.search(pattern, text):
        print("MATCH!")
    else:   # else, return NO MATCH!
        print("NO MATCH!")

# However, we can use regular expressions for a more powerful way of parsing the data

match = re.search('term1', text)
print(type(match))

# Instead of a boolean value, we get a Match object (SRE_Match), which contains a lot of helpful data
# like where the match was found, was it found, etc.

print(match.start())                # This will return the index location where the match was found

#########
# Split #
#########

# Regular expressions also support the ability to split using delimiters

split_term = '@'
email = 'user@gmail.com'
print(re.split(split_term, email))      # will print out ['user', 'gmail.com']

# We've seen this before as a built-in Python method:
email = 'user@gmail.com'.split('@')
print(email)

###########
# Findall #
###########

# Occasionally, we might want to find all instances of a pattern instead of just one

# This returns a list of every instance of a term given.
print(re.findall('match', 'test phrase match in middle'))

# we can also check the length of findall to count:
print(len(re.findall('match', 'test phrase match in middle')))

#############################
# The meta character syntax #
#############################

#####
# * #
#####

def multi_re_find(patterns, phrase):

    # What this code will do is take in a list of terms: patterns
    for pat in patterns:
        # For every term (pat) in patterns, print what term we are looking for
        print("Searching for pattern {}".format(pat))
        # Also, run findall() and print a list of every match found
        print(re.findall(pat, phrase))
        # print \n to make a newline
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'        # our string we will parse
# First meta character syntax: * will find the following character 'd' 0 or more times
# so to translate: find each term that starts with s, and also follows with 0 or more 'd's
test_patterns = ['sd*']         # our list of patterns

# run our function to run our findall test
multi_re_find(test_patterns, test_phrase)


#####
# + #
#####

# If instead we want to look for one or more 'd's, we use a plus sign:
test_patterns = ['sd+']

multi_re_find(test_patterns, test_phrase)

#####
# ? #
#####

# Or if we want to find 'd' 0 or 1 time, we use the question mark

test_patterns = ['sd?']
multi_re_find(test_patterns, test_phrase)

############################
# Define your own stepsize #
############################

# To define our own stepsize, we use curly braces

test_patterns = ['sd{3}']
multi_re_find(test_patterns, test_phrase)

# We can also add another stepsize to the existing one, so if we want to search for 
# 2 or 3 'd's, we do:
test_patterns = ['sd{1,3}']         # no spaces inside braces
multi_re_find(test_patterns, test_phrase)

#############
# Either or #
#############

# We can also use syntax to find either one character or another character

test_patterns = ['s[sd]+']

multi_re_find(test_patterns, test_phrase)
# so this time we get back a list of every term that starts with an 's', and is followed by
# either one or more 's' or 'd' characters

##############
# Exceptions #
##############

# We can also look for terms that -do not- include a defined pattern

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

# To try this out, we want to remove the above string of any punctuation.
# To do this, we use the carrot symbol before our pattern to exclude terms:
test_patterns = ['[^!.?]+']

multi_re_find(test_patterns, test_phrase)

######################################
# Other weird operations we can make #
######################################

# This will return a range of characters that are all lower case
test_patterns = ['[a-z]+']
multi_re_find(test_patterns, test_phrase)

# And the inverse with all capital letters:
test_patterns = ['[A-Z]+']
multi_re_find(test_patterns, test_phrase)

# We can parse for specific character types, like digits. To do this, we type 'r' outside of the string,
# and for this, we use \d that stands for digits
test_phrase = 'This is a string with numbers 12312 and a symbol #hashtag'
test_patterns = [r'\d+']       # return all instances of 1 or more digits
multi_re_find(test_patterns, test_phrase)

# For non-digits:
test_patterns = [r'\D+'] 
multi_re_find(test_patterns, test_phrase)

# For whitespace: \s
test_patterns = [r'\s+'] 
multi_re_find(test_patterns, test_phrase)

# For non-whitespace: \S
test_patterns = [r'\S+'] 
multi_re_find(test_patterns, test_phrase)

# For alpha-numeric characters: \w
test_patterns = [r'\w+'] 
multi_re_find(test_patterns, test_phrase)

# For non-alpha-numeric characters: \W
test_patterns = [r'\W+'] 
multi_re_find(test_patterns, test_phrase)