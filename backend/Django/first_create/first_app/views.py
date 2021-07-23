from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dictionary = {'insert_me':"Hello I am from views.py!",
                     'new_title':"This is my new title!"}
    return render(request, 'index.html', context=my_dictionary)

def about(request):
    return HttpResponse("About page")