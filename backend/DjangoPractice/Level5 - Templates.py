#######################
# Level 5             #
# ------------------- #
# Templates           #
#######################


#######################
# What is a template? #
#######################

# Templates and Template Tags

# The template will contain the static parts of an html page (parts that are always the same)
# You can see these as the scaffolding or blueprints of a page.

# Template tags: allows you to inject dynamic content that your Django App's views will produce, effecting
# the final HTML. Template tags have their own special syntax.

###############################
# Create a template directory #
###############################

# First, we need to create a templates directory, and a subdirectory for every specific app's templates.
# It will go inside of our top level directory:
#   first_project/templates/first_app

############################################
# Let Django know about template directory #
############################################

# First we need to let Django know about our templates by editing the DIR key inside of the
# TEMPLATES dictionary in the settings.py file.

# However, there is an issue we have to deal with first.

# We want our project to be transferrable from one computer to another. Like our urls.py issue, we don't want
# our path to be 'hard-coded' into the DIR key - this is a problem if a user imports to their own 
# os system with different file structure or simply a different-named directory.

# We can use Python's os module to dynamically generate the correct file path strings, regardless of computer.
# Import os and try out the following:
import os

print(__file__)             # Returns 'G:/Program Files/anaconda3/python.exe'
print(os.path.dirname(__file__))    # returns 'f:/Mt Sac CS Club/Projects/WP/Club-Website/backend/DjangoPractice/Level5 - Templates.py'

# We will use this os module to feed the path to the DIR key inside of the TEMPLATES dictionary
# Then, we will create an html file called index.html inside of the templates/first_app directory 

# Inside this HTML file we will insert template tags (aka Django Template Variable)
# These template variables will allow us to inject content into the HTML directly from Django!

########################################
# Proving the power of a web framework #
########################################

# Django will be able to inject content into the HTML
# Which means later on we can use Python code to inject content from a database! (which we will learn with models)

############
# render() #
############

# To do all of this, we will use the render() function and place it in our original index() fucntion 
# inside of our views.py file.

###############
# Settings.py #
###############

# Add this under settings.py base_dir variable:
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

# Then find TEMPLATES and assign DIRS the TEMPLATE_DIR variable

################################
# Create a template index.html #
################################

# Next we will create our first index.html file:

<! DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>First App</title>
    </head>
    <body>
        <h1>Hello this is index.html!</h1>
        {{ insert_me }}         # this is our template tag that django will insert code
    </body>

</html>

# Then we will go into views and edit our function:
def index(request):
    # return HttpResponse("Hello World")
    my_dictionary = {'insert_me':"Hello I am from views.py!"}
    return render(request, 'index.html', context=my_dictionary)