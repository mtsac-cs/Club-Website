####################
# Level 1          #
# ---------------- #
# Django Practice  #
####################

###################
# What is Django? #
###################

# - Django is a free and open source web framework
# - Websites that use it: Pinterest, PBS, Instagram, Bitbucket, Washington Times, Mozilla, etc

########################
# What does Django do? #
########################

# Django solves two major problems:
# - It allows us to map a requested URL sent by the user to the code meant to handle it
# - Allows us to create that html file dynamically using templates

#####################
# History of Django #
#####################

# - Created in 2003 when the web developers at the at the Lawrence Journal-World newspaper started using Python
#   for their development
# - It originating as a newspaper is important
# - Because the original developers were surrounded by writers, good documentation is a key part of Django!

# - Django has its own excellent basic tutorial where you are wealked through creating a basic polling web app.

###########################
# The virtual environment #
###########################

# - When encountering Django tutorials, you are often asked to instal a venv, or virtual environment.
# - venv: a virtual environment allows you to have a virtual installation of Python and packages on your 
#   computer
#   - venvs are important because it lets us work in the same version of Python, especially considering that
#   - packages change and get updated often, and they can break backwards compatibility
#   - if we wanted to test the new features of a new package, we can just create a new venv so to not mess
#   - up our current project.  Anaconda makes this easy.

##################################
# Creating a virtual environment #
##################################

# First, switch your terminal from powershell to cmd.
# - In Visual Studio Code:
#   - CTRL + Shift + P
#   - Select Terminal: Select Default Profile
#   - Pick CMD

# To use a virtual environment with conda, we use these commands:
#   conda create --name myEnv django
# This creates an environemtn called "myEnv" with the latest version of Django
# - later on, we can create a specific version of Django if we wanted, so in the command above, replace
#   Django with django=1.9 or something.

##############################
# Activating the environment #
############################## 

# To activate a virtual environment use the following command:
#   activate myEnv
# Now anything installed with pip or conda when the environment is activated, will only be installed
# to this environment.

# conda documentation to set up environments: https://conda.io/docs/using/envs.html

##################################
# Installing a different version #
##################################

# At some point during the venv setup, it will show you the new packages it will install.
# If you rather have a different version of a package, like Python for example, you will
# include the name of the package at the end of the venv setup command like so:

#   conda create --name myEnv python=3.9

######################################
# Find all discoverable environments #
######################################

# If you forgot the name of your environment, the command:
#   conda info --envs
# should help you find it

############################
# Verify environment works #
############################

# Type 'python' to get python version with venv
# Type 'quit()' to exit Django
# Type 'deactivate' to deactivate virtual environment
# Type 'python' again, and the version should be the one installed on the pc