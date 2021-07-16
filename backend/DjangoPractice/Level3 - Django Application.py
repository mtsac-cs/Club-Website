#######################
# Level 3             #
# ------------------- #
# Django Application  #
#######################

# A Django project: a collection of aplications and configurations that when combined together
# will make up the full web application (your complete website running with Django)

# Things you can create with Django:

#   - A registration application
#   - A polling application
#   - A comments application

# These Django apps can then be plugged into other Django projects, so you can reuse them! (or use other
# people's apps)

# Let's create our first app.

####################
# startapp command #
####################

#   python manage.py startapp first_app

# We have now created a new file structure called first_app, with the following files:
#   __init__.py
#   admin.py
#   apps.py
#   models.py
#   tests.py
#   views.py

# This looks similar to when we created a new Python project, with a few differences.

###############
# __init__.py #
###############

# Just like the project __init__.py, it serves the same purpose: it lets Python know to treat this directory as
# a package.

############
# admin.py #
############

# Here we can register our models that Django will use to create our own admin interface.
# We will discuss this later on.

###########
# apps.py #
###########

# Here we can place application-specific configurations.

#############
# models.py #
#############

# Here we store the application's data models (relationships between the data)

###########
# test.py #
###########

# Here we can place our test functions to test our app code

############
# views.py #
############

# This is where you have functions that handle requests and return responses

########################
# migrations directory #
########################

# Stores database-specific information as it relates to the models


################################

# Before we learn any of this, we need to tell Django that our first_app actually exists.

###############################
# first_project > settings.py #
###############################

# We need to go to our settings.py file that we first made when we created our project.

# Look for a list called INSTALLED_APPS that has several application definitions.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'first_app'                     # add our first_app to this list
]

# To confirm this worked, run the server again with python manage.py runserver
# As long as we do not get any errors, we should be fine

###############
# Hello world #
###############

# Without dealing with templates yet, we are going to create our first Hello World program
# with just the views.py file.

from django.shortcuts import render
from django.http import HttpResponse        # 1: Import the HttpResponse object from the django.http module

# Each view will exist in this views.py file as its individual function:
# Each view will also take in at least one argument:
def index(request):                         # This could be named anything, but by convention, we call this variable 'request'
    return HttpResponse("Hello World!")     # Regardless of response, this returns 'hello world'
                                            # If we wanted, we could pass in html instead of a string
                                            # but we will show that later on

###################################
# Adding our index to our urls.py #
###################################

# We need to tell Django that our view exists, in this case, our index exists.
# To do that, we go to our project > urls.py file and look for the list called urlpatterns:

from first_app import views # import views from our first_app

urlpatterns = [
    # Adding to the list, we pass a first paramater with a regular expression, explained ahead
    path('', views.index, name='index'),  # then we pass in our views.index function, and then set the name variable to the name of our view
    path('admin/', admin.site.urls)
]

# This is essentially mapping our view to this URL
