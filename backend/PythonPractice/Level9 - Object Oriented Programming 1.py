############## Objected Oriented Programming
########### Notes taken are following the Python and Django Full Stack Web Developer Bootcamp on Udemy.com
########### URL: https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/

# Note that in the code below, when we add a dot . following mylist, we get a lot of options
# to manipulate the list

mylist = [1, 2, 3]
mylist.append(4)            # In this case, we chose .append()
print(mylist)

# Those are called objects.  In Python, everything is an object.

print(type([1, 2, 3]))      # This will return <class 'list'>, and 'class' is what makes this work
print(type(()))             # Another example: class tuple
print(type(200))            # Class = int
print(type(2.0))            # Class = floating point

# So how do we make our own classes?

###########
# Classes #
###########

# Classes are essentially blueprints that define our objects. Objects are essentially instances
# of that class.

# For example, when we created our list:

mylist = [1, 2, 3]              # We created an instance, or object, of the class 'list'

# So let's create our own class:

class Sample():                    # Note: classes start with upper case, functions lower case
    pass

x = Sample()                        # Create an object of Sample()
print(type(x))                      # <class '__main__.Sample'>, we can ignore __main__ for now.
