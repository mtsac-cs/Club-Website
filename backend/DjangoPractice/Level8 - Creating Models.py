##############################
# Level 8                    #
# -------------------------- #
# Creating Django Models     #
##############################

##############################
# Overview: Creating a model #
##############################

# Using object oriented programming, let's create some models.

# Go into the models.py file in your application:

from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    # From our OOP overview, remember that we have special
    # methods, in this case we will use one called __str__
    # so that when someone decides to print an object of our
    # Topic class, it will return the top_name attribute as
    # a string. 
    def __str__(self):
        return self.top_name

class WebPage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date) # cast it as string because it is a date object

##############################
# Migrate models to database #
##############################

# So now we need to migrate our models to the database
python manage.py migrate

# Next we need to register our migrations to our application:
python manage.py makemigrations <app name>

# And run python manage.py migrate one more time.
python manage.py migrate

########################
# Testing the database #
########################

# A way we can test our database is by using shell commands.
python manage.py shell

# This will open an interactive shell.

from first_app.models import Topic
print(Topic.objects.all())

# We will get something like this:
<QuerySet []>

# so then type:
t = Topic(top_name="Social Network")
t.save()

# Now if we run print again:
print(Topic.objects.all())

# We should get back: 
<QuerySet [<Topic: Social Network>]>

# Leave shell
quit()

###################
# Admin interface #
###################

# Using the shell is kind of clunky, so a better way
# to mess with our database is by using the admin interface

# First, we need to register our models to the admin.

# Go into admin.py and type:

from django.contrib import admin
from first_app.models import AccessRecord, Topic, Webpage

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(WebPage)

# And then we'll need to create a superuser that can access
# the admin interface.

python manage.py createsuperuser

# It will require you to create a username, password,
# and add an email address.

# Now run the python server to test the changes.
python manage.py runserver

# Type in the correct URL to access the admin page:
http://127.0.0.1:8000/admin

# And log in.  You should now be able to manipulate your
# database using the admin portal.
