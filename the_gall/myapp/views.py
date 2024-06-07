from django.shortcuts import render
from .models import Song  # Import the Song model

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def setlist(request):
    # Fetch all songs from the database
    setlist = Song.objects.all()

    context = {'setlist': setlist}
    return render(request, 'setlist.html', context)

