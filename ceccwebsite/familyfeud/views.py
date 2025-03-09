from django.shortcuts import render, redirect, HttpResponse
#from .models import board

def board(request):
    return render(request, 'familyfeud/board.html')
