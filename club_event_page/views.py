from django.shortcuts import render

def index(request):
    return render(request, 'club_event_page/index.html')
    