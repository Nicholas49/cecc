from django.shortcuts import render, redirect, HttpResponse

def mainview(request):
    context = {'foo': 'bar'}
    return render(request, 'ceccwebsite/mainview.html', context)
