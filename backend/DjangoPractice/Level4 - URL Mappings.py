#######################
# Level 4             #
# ------------------- #
# URL Mappings        #
#######################

# We learned earlier how to map a view to the urls.py file from the project folder. Now we want to use the 
# include() function from django.conf.urls to do the same thing.

# The include() function allows us to look for a match with regular rexpression and link back to our application's 
# own urls.py file.
# We will have to manually create this urls.py file.

#############
# include() #
#############

# Go to the project urls.py file and add the following to urlpatterns:

from django.conf.urls import include

urlpatterns = [
    #url(r'^first_app/', include('first_app.urls'))
    path('', include('first_app.urls'))
]

# What it's telling Django to do is to look for any url that looks like www.domainname.com/first_app/...
# This also tells Django to look for the urls.py file in our app folder instead of the one in the
# projects folder.
# This also makes our project clean and modular, this way we can plug and play our apps instead of 
# hard-coding them to a project.

###########################################
# Create a urls.py file under application #
###########################################

from django.urls import path
from first_app import views

urlpatterns = [ 
    path('', views.index, name='index'),
]

# If we wanted, we could pass a string as the first argument in path() in project urls.py so that our app needs to be found at a
# specific extension.
#   path('firstextension/', include('first_app.urls'))
