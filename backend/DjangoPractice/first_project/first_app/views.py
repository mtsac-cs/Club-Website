from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello World")
    my_dictionary = {'insert_me':"Hello I am from views.py!"}
    return render(request, 'index.html', context=my_dictionary)