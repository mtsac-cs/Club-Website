###################
# Level 2         #
# --------------- #
# Django Project  #
###################

# When you installed Django, it also installed a command line tool called:
#       django-admin

# To create our first project, type:
#       django-admin startproject first_project

# This will create a folder with the name we gave it, and it will have a few files in it.

#############################################
# Using a different folder to start project #
#############################################

# If you don't like the current folder you are in to create your project, we can use a different folder.
# First, navigate to your folder with:
#       cd <directory name>
# If you want to create a new folder here, then:
#       mkdir <directory name>
#       cd <new directory name>
# And then do the previous steps for creating your first project


###############
# __init__.py #
###############

# A blank Python script that tells Python that this directory can be treated as a 'package'
# Package: 

###############
# settings.py #
###############

# Where we will be storing all of our project's settings

###########
# urls.py #
###########

# A Python script that will store all of the URL patterns for our project, and how they relate to our
# website's different web pages. Basically: the different web pages of our web app.

# Will use regular expressions!

###########
# wsgi.py #
###########

# This is a Python script that acts as the Web Server Gateway Interface. It will alter on help us
# deploy our web app to production.

#############
# manage.py #
#############

# This is a python script that we will use a lot. It will be associated with many commands as we build our
# web app.

# Using manage.py, type in the folowing command:
#       python manage.py runserver
# This will deploy a local web server that we can access at:
#       http://127.0.0.1:8000/

# We now should see a web page saying that Django is installed correctly.
# Note: we should see an error message that we have some unapplied migrations.  We won't worry
# about this yet.

# Quit server with 
# - CTRL + Z 
# - or CTRL + C 
# - or CTRL + BREAK 
# - or CTRL + SHIFT + C

##############
# Migrations #
##############

# That was a lie.  MIGRATIONS COME NOW.

# A migration allows you to move databases from one design to another, this is also reversible.
#   i.e. add a new field, add a new column, or reverse any changes.

