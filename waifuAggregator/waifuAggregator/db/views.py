from django.shortcuts import render
from .models import pegs

# Create your views here.

def db(request):
    peges = pegs.objects.all()
    return render(request, 'db/db.html', {'peges': peges})