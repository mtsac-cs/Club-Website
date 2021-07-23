##############################
# Level 7                    #
# -------------------------- #
# Django Models Overview     #
##############################

# Models are used to implement databases into our Django project

# By default, Django comes installed with SQLite, which is fine
# while we learn about databases, but Django can also connect
# to other databases like PostgreSQL, MySQL, MariaDB, etc -
# some of which are designed for larger projects.

# In the settings.py file you can edit the ENGINE parameter used
# for DATABASES if we wanted to switch out the database engine
# to something else.

##############################
# Overview: Creating a model #
##############################

# To create a model, we create a class structure within the
# corresponding models.py file inside of an application file
# directory.

# It is a subclass of Django's built-in class:
 
django.db.models.model

# Each attribute of the class represents a field, which is
# just like a column name with constraints in SQL.

#################
# How SQL works #
#################

# SQL operates like a giant table, with each column representing
# a field, and each row representing an entry.

# | --------------------------------------------------- |
# | WebsiteID      | WebsiteName     | URL              |
# | --------------------------------------------------- |
# | 1              | Google          | www.google.com   |
# | --------------------------------------------------- |
# | 2              | Facebook        | www.facebook.com |
# | ----------------------------------------------------|

# Basically works like an excel sheet. Each field can also be
# of a different type, like a character field, a number field,
# etc.  They can also have restraints, like max number of 
# characters.

#######################
# Model Relationships #
#######################

# In Django, Models = Tables.  Often models will reference each
# other.

# For example, take our table with websites on it:

# | --------------------------------------------------- |
# | WebsiteID      | WebsiteName     | URL              |
# | --------------------------------------------------- |
# | 1              | Google          | www.google.com   |
# | --------------------------------------------------- |
# | 2              | Facebook        | www.facebook.com |
# | ----------------------------------------------------|

# And another table with dates:

# | ----------------------------------- |
# | WebsiteID      | DateAccessed       |
# | ----------------------------------- |
# | 1              | 2018-01-01         |
# | ----------------------------------- |
# | 2              | 2018-02-03         |
# | ------------------------------------|

# The first table is a list of websites accessed, and the second
# one has a list of dates when they were accessed.

# The WebsiteID is what is called a primary key, and the other
# fields are foreign keys.

# Primary keys uniquely identify the table rows, while foreign
# keys connect two or more tables with the same identifiers.

######################
# Example of a model #
######################

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

class WebPage(models.Model):
    category = models.ForeignKey(Topic)
    name = models.CharField(max_length=264)
    url = models.URLField()

#############
# Migration #
#############

# After we've set up the models we can migrate the database.
# Migrating basically lets Django do all of the work of 
# creating our SQL database using the models we created.

# Django can do this with the following command:

python manage.py migrate

# And then we register the changes to our app:

python manage.py makemigrations <app name>

# Then we migrate the database one more time:

python manage.py migrate

# We can also make this easier by registering our models to our
# admin interface, by using the following code:

from django.contrib import admin
from app.models import Model1, Model2

admin.site.register(Model1)
admin.site.register(Model2)

# Finally, we will create a superuser for the admin, use a 
# script called Faker to populate our database, and even create our
# own.

