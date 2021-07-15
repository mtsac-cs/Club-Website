################
# Dictionaries #
################

########### Notes taken are following the Python and Django Full Stack Web Developer Bootcamp on Udemy.com
########### URL: https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/

## Basically lists but with key-value pairings

my_stuff = {"key1":"value", 'key2':'value2', 'key3':{'123':[1, 2, 3, 'grabme']}}          # Dictionaries do not retain any sort of order

print(my_stuff['key3'])                                                         # Return a value by calling the key
print(my_stuff['key3']['123'][3])                                               # How to call nested lists and dictionaries

## Dictionaries are mutable, so we can change the values by reassigning keys

my_stuff = {'lunch':'pizza', 'bfast':'eggs'}
my_stuff['lunch'] = 'burger'
# you can add new items by calling a new key and giving it a value
my_stuff['dinner'] = 'pasta'
print(my_stuff['lunch'])
print(my_stuff)

