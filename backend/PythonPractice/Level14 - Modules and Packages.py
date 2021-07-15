########### Modules and Packages
########### Notes taken are following the Python and Django Full Stack Web Developer Bootcamp on Udemy.com
########### URL: https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/

# How to create your own module and import to your own file

# let's pretend this is in mymodule.py
def func_in_module():
    print("I am inside the mymodule.py file!")

# then in another file, we can import it, as long as they're in the same folder:
import mymodule
mymodule.func_in_module()

# Another way is to import our module as another name to make it shorter
import mymodule as mm
mm.func_in_module()

# Or if we just want to import a few functions from the module:
from mymodule import func_in_module
func_in_module()

# a non-recommended way of doing it is to use an asterisk to import everything in the module
from mymodule import *