from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def aboba(request):
    return render(request, 'main/aboba.html', {'title': ['1', '2', '3']})