####################
# Level 6          #
# ---------------- #
# Static Files     #
####################

# Template files are great to learn because we can create
# dynamic content by injecting text into an HTML file
# using variables parsed by Django.

# Interestingly, we can also inject files into html files,
# or more accurately, static files.  This includes things
# like images, videos, and even logic (for loops, etc), but
# we'll talk about logic later.

###############################
# Create a Static File folder #
###############################

# We want to make sure that we are staying consistent with
# the idea of modularity, so let's create a folder within
# our project folder called 'static' which will contain
# things like images and other documents we can insert.

# Also create another folder inside of it called 'images'
# Also too, download a picture, any picture, and store inside

#############################
# Create a path to 'static' #
#############################

# Like we did with our templates folder, we need to tell
# Django about our new 'static' directory. To do this,
# go into settings.py and add:
 
STATIC_DIR = os.path.join(BASE_DIR, "static")

# under the BASE_DIR variable.

##############
# STATIC_URL #
##############

# Conveniently, there is another reference to our static files 
# in another variable called STATIC_URL. In the spirit of modularity
# let's use the STATIC_DIR we created earlier and store inside a 
# new list caled STATICFILES_DIRS and place it below the STATIC_URL
# variable. Make sure it hasn't already been created as sometimes
# it is created for you.

STATICFILES_DIRS = [
    STATIC_DIR,
]

##################################
# Accessing our picture directly #
##################################

# What this does essentially is it allows us to access our our jpeg
# file directly from the address bar, which means that it's now live
# on the internet.  To test this, run the server and visit:

http://127.0.0.1:8000/static/images/this_is_a_duck.jpg

# And we should get our picture inside of our images folder.

################################
# Injecting the file into HTML #
################################

# Let's modify our HTML file and add some new code:

<!DOCTYPE html>
{% load static %}
<html>
    <head>
        <meta charset="utf-8">
        <title>CS Club Duck Page</title>
    </head>
    <body>
        <h1>Hello this is index.html!</h1>
        <img src="{% static "images/this_is_a_duck.jpg" %}" alt="Oh shit that's not a duck.">
    </body>

</html>

# We add a new tag: {% load static %} because we want
# to tell Django that we will be adding some static files.
# It will also save us time if we don't need to load
# static files so that we're not just always loading them.

# If we visit our index page, we should now see our updated
# web page.

#########################
# Injecting other files #
#########################

# Static files aren't just images, it can also involve any
# files that aren't going to change, like CSS and Javascript.

# CSS

# Create a css folder inside of our static folder and
# also create a fresh css file called style.css.

# Inside of our HTML file, add link to the <head> tags:

<link rel="stylesheet" href="/css/style.css">

# Deliberately, the href link was left to show what changes are
# made to make this work.  We will replace it with our 
# template tag:

<link rel="stylesheet" href="{% static "css/style.css" %}">

# Refresh the index page and we should see our CSS updated.