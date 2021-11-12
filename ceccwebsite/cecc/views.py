from django.shortcuts import render, redirect

from .models import Comment, Ceccmenu, CeccEvent
from .forms import CommentForm, MenuForm, EventForm, PasswordForm

import hashlib
import math


def base(text,
         alfin="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ',./=-;<>?+_:!@#$%^&*()[]{}`~|",
         alfout="0123456789abcdef"):
    return tostring(toint(text, alfin), alfout)


def toint(stri, alf):
    # takes in a string of characters and then, using the supplied alphabet, interprets the
    # string as a number with a base the size of the alphabet, each character representing a digit.
    # It then converts this number to a base 10 representation and returns it as an integer."""

    numblist = tonumblist(stri, alf)

    total = 0

    alflen = len(alf)
    count = len(numblist) - 1
    for numb in numblist:
        total += int(numb) * (alflen ** count)
        count -= 1

    return total


def tostring(numb, alf):
    # The inverse of toint, this function takes in an integer and converts it into a
    # a 'base x' representation in the form of a string where x is the number of
    # characters in the provided alphabet"""

    count = 0
    outstring = ""

    alflen = len(alf)

    while numb >= (alflen ** count):
        count += 1
    count -= 1

    while count >= 0:
        powr = alflen ** count
        digi = math.floor(numb / powr)
        outstring += alf[digi]
        numb %= powr
        count -= 1

    return outstring


def tonumblist(text, alf3):
    # Converts a string of characters into a list of integers based on their position in the supplied alphabet

    numbi = []

    for x in text:
        for y in range(len(alf3)):
            if x == alf3[y]:
                numbi.append(y)
                break

    return numbi

def index(request):
    context = {'rightpane' : False}
    return render(request, 'cecc/index.html', context)

def history(request):
    context = {'rightpane' : True}
    return render(request, 'cecc/history.html', context)

def programs(request):
    context = {'rightpane' : True}
    return render(request, 'cecc/programs.html', context)

def photos(request):
    context = {'rightpane' : True}
    return render(request, 'cecc/photo-gallery.html', context)

def video(request):
    context = {'rightpane' : True}
    return render(request, 'cecc/video.html', context)

def mrdcnewsletter(request):
    context = {'rightpane' : True}
    return render(request, 'cecc/mrdcnewsletter.html', context)

def ceccnewsletter(request):
    context = {'rightpane' : True}
    return render(request, 'cecc/ceccnewsletter.html', context)

def mrdcmenus(request):

    cevents = Ceccmenu.objects.order_by('week', 'weekday')

    seasons = {"ASPR": [], "BSSM": [], "CSUM": [], "DAUW": []}

    for c in cevents:
        weekfound = False
        for w in seasons[c.season]:
            if w["weekno"] == c.week:
                weekfound = True
                w["daylist"].append(c)
        if not weekfound:
            seasons[c.season].append({"weekno": c.week, "daylist": [c]})

    ccontext = {'seasons': seasons, 'rightpane': True}

    return render(request, 'cecc/mrdcmenus.html', ccontext)

def ceccmenus(request):

    cevents = Ceccmenu.objects.order_by('week', 'weekday')

    seasons = {"ASPR": [], "BSSM": [], "CSUM": [], "DAUW": []}

    for c in cevents:
        weekfound = False
        for w in seasons[c.season]:
            if w["weekno"] == c.week:
                weekfound = True
                w["daylist"].append(c)
        if not weekfound:
            seasons[c.season].append({"weekno": c.week, "daylist": [c]})

    ccontext = {'seasons': seasons, 'rightpane': True}

    return render(request, 'cecc/ceccmenus.html', ccontext)

def schedules(request):

    cevents = CeccEvent.objects.order_by('month', 'dayno')

    monthlist = []

    for c in cevents:
        monthfound = False
        for m in monthlist:
            if m["month"] == c.month:
                monthfound = True
                m["daylist"].append(c)
        if not monthfound:
            monthlist.append({"month": c.month, "daylist": [c]})

    ccontext = {'monthlist': monthlist, 'rightpane': True}

    return render(request, 'cecc/news.html', ccontext)

def contact(request):

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = Comment(name=request.POST['name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')
    else:
        form = CommentForm()

    context = {'form': form, 'rightpane': True}

    return render(request, 'cecc/contact-us.html', context)

def addmenu(request):

    if request.method == 'POST':

        password = request.POST['passwordf']

        hp = '2751f85e053ec176a421c9f75621e311ec304579f4ae4e8d5a049f701c039ed7'
        hp2 = hashlib.sha256(base(password).encode()).hexdigest()

        if hp == hp2:
            new_event = Ceccmenu(season=request.POST['season'],
            week=request.POST['week'],
            weekday=request.POST['weekday'],
            breakfast=request.POST['breakfast'],
            lunch=request.POST['lunch'],
            snack=request.POST['snack'])
            new_event.save()

            seasons = getmenus()
            form = MenuForm()
            context = {'seasons': seasons, 'form': form, 'password': password, 'rightpane': True}

            return render(request, 'cecc/sign.html', context)

    return render(request, 'cecc/index.html')

def getmenus():
    cevents = Ceccmenu.objects.order_by('week', 'weekday')

    seasons = {"ASPR": [], "BSSM": [], "CSUM": [], "DAUW": []}

    for c in cevents:
        weekfound = False
        for w in seasons[c.season]:
            if w["weekno"] == c.week:
                weekfound = True
                w["daylist"].append(c)
        if not weekfound:
            seasons[c.season].append({"weekno": c.week, "daylist": [c]})
    return seasons


def sign(request):
    if request.method == 'POST':
        form = MenuForm()
        password = request.POST['passwordf']

        hp = '2751f85e053ec176a421c9f75621e311ec304579f4ae4e8d5a049f701c039ed7'
        hp2 = hashlib.sha256(base(password).encode()).hexdigest()

        if hp == hp2:

            seasons = getmenus()
            context = {'seasons': seasons, 'form': form, 'password': password}
            return render(request, 'cecc/sign.html', context)
        else:
            form = PasswordForm()
            context = {'form': form, 'error': 'Invalid Password', 'rightpane': True}
            return render(request, 'cecc/password.html', context)


    return redirect('index')


def passwordpage(request):

    form = PasswordForm()
    context = {'form': form, 'error': '', 'rightpane': True}
    return render(request, 'cecc/password.html', context)


def delmenu(request):
    if request.method == 'POST':
        password = request.POST['passwordf']

        hp = '2751f85e053ec176a421c9f75621e311ec304579f4ae4e8d5a049f701c039ed7'
        hp2 = hashlib.sha256(base(password).encode()).hexdigest()

        if hp == hp2:
            Ceccmenu.objects.filter(id=request.POST['menu_id']).delete()
            form = MenuForm()
            seasons = getmenus()

            context = {'seasons': seasons, 'form': form, 'password': password, 'rightpane': True}
            return render(request, 'cecc/sign.html', context)


    return render(request, 'cecc/index.html')

def addevent(request):

    if request.method == 'POST':
        form = EventForm(request.POST)

        hp = '2751f85e053ec176a421c9f75621e311ec304579f4ae4e8d5a049f701c039ed7'
        hp2 = hashlib.sha256(base(request.POST['pswrd']).encode()).hexdigest()

        if form.is_valid() and hp == hp2:
            new_event = CeccEvent(month=request.POST['month'],
            dayno=request.POST['dayno'],
            weekday=request.POST['weekday'],
            event=request.POST['event'])
            new_event.save()
            return redirect('')
    else:
        form = EventForm()

    return redirect('ceccmenus')

