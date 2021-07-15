########### Name and Main
########### Notes taken are following the Python and Django Full Stack Web Developer Bootcamp on Udemy.com
########### URL: https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/

# Unlike other languages, Python doesn't have a main driver function that runs code when the program is
# executed.  Instead, all code at level 0 indentation is implicitly assumed to be run and executed, so
# you can consider that code to be part of 'main'.

# There is a way to test if a module is being run directly using a variable called __name__.

def func():
    print("fun() in one.py")

print("TOP LEVEL ONE.PY")

if __name__ == '__main__':
    print("one.py is being run directly")
else:
    print("one.py has been imported")

# By default, __main__ is equal to the name of the module, so __name__ tests the name of the module __name__
# currently resides in. That way if this module is imported elsewhere, -their- __main__ will be different, but
# __name__ will still have the name of the module it  was created in.