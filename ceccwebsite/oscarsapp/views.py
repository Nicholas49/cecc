from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import Winners, oscarballot, umslballot
from .forms import OscarBallot, Passwordform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

import hashlib
import math

oscurls = ['chart', '', 'loadballot']
umslurls = ['umsl/chart', 'umsl', 'umsl/loadballot']

def base(text,
         alfin="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ',./=-;<>?+_:!@#$%^&*()[]{}`~|",
         alfout="0123456789abcdef"):
    return tostring(toint(text, alfin), alfout)


def toint(stri, alf):
    # takes in a string of characters and then, using the supplied alphabet, interprets the
    # string as a number with a base the size of the alphabet, each character representing a digit.
    # It then converts this number to a base 10 representation and returns it as an integer.

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
    # characters in the provided alphabet

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


def calculatescore(n, w):
    n.skore = 0
    if n.bestpicture == w.bestpicture:
        n.skore += 3
    if n.actor == w.actor:
        n.skore += 3
    if n.actress == w.actress:
        n.skore += 3
    if n.supactor == w.supactor:
        n.skore += 2
    if n.supactress == w.supactress:
        n.skore += 2
    if n.animatedfeature == w.animatedfeature:
        n.skore += 1
    if n.cinematography == w.cinematography:
        n.skore += 1
    if n.costume == w.costume:
        n.skore += 1
    if n.directing == w.directing:
        n.skore += 2
    if n.documentary == w.documentary:
        n.skore += 1
    if n.docshort == w.docshort:
        n.skore += 1
    if n.fediting == w.fediting:
        n.skore += 1
    if n.foreign == w.foreign:
        n.skore += 1
    if n.makeupandh == w.makeupandh:
        n.skore += 1
    if n.mscore == w.mscore:
        n.skore += 1
    if n.msong == w.msong:
        n.skore += 1
    if n.prodesign == w.prodesign:
        n.skore += 1
    if n.animatedshort == w.animatedshort:
        n.skore += 1
    if n.shortfilm == w.shortfilm:
        n.skore += 1
    if n.sound == w.sound:
        n.skore += 1
    if n.visualfx == w.visualfx:
        n.skore += 1
    if n.writingad == w.writingad:
        n.skore += 1
    if n.writingor == w.writingor:
        n.skore += 1
    n.vwidth = n.skore * 3
    n.save()


def create_user(request):
    code = request.POST['code']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['repassword']

    if not password == password2:
        return redirect('passpage', error='Passwords Do Not Match')

    hp = hashlib.sha256(base(code).encode()).hexdigest()

    if not hp == '6eeb012caae507c80b6055868c5af63c61fdacee9cdc24097f23dfcb49d5d392':
        return redirect('passpage', error='Incorrect Access Code')

    users = User.objects.order_by('username')
    for u in users:
        if username == u.username:
            return redirect('passpage', error='user already exists')

    newuser = User.objects.create_user(username, password=password)
    newuser.save()

    user = authenticate(request, username=username, password=password)

    login(request, user)
    return redirect('loadballot')


def ucreate_user(request):
    code = request.POST['code']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['repassword']

    if not password == password2:
        return redirect('upasspage', error='Passwords Do Not Match')

    hp = hashlib.sha256(base(code).encode()).hexdigest()

    if not hp == '6eeb012caae507c80b6055868c5af63c61fdacee9cdc24097f23dfcb49d5d392':
        return redirect('upasspage', error='Incorrect Access Code')

    users = User.objects.order_by('username')
    for u in users:
        if username == u.username:
            return redirect('upasspage', error='user already exists')

    newuser = User.objects.create_user(username, password=password)
    newuser.save()

    user = authenticate(request, username=username, password=password)

    login(request, user)
    return redirect('uloadballot')


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    thisuser = authenticate(request, username=username, password=password)

    if thisuser is not None:
        login(request, thisuser)
        return redirect('loadballot')
    else:
        return redirect('passpage', error='username or password is wrong')


def ulogin_user(request):
    username = request.POST['username']
    password = request.POST['password']

    thisuser = authenticate(request, username=username, password=password)

    if thisuser is not None:
        login(request, thisuser)
        return redirect('uloadballot')
    else:
        return redirect('upasspage', error='username or password is wrong')


def front(request):

    name = 'none'
    logged_in = False

    if request.user.is_authenticated:
        name = request.user.username
        logged_in = True

    commento = oscarballot.objects.order_by('-skore')
    w = Winners.objects.get()

    for n in commento:
        calculatescore(n, w)

    counter = 1
    for n in range(len(commento)):
        if not n == 0:
            if not commento[n].skore == commento[n - 1].skore:
                counter += 1
        commento[n].place = counter

    context = {'commentz' : commento, 'winnerz' : w, 'urlz' : oscurls, 'name': name, 'logged_in': logged_in}

    return render(request, 'oscarsapp/mainchart.html', context)


def ufront(request):

    name = 'none'
    logged_in = False

    if request.user.is_authenticated:
        name = request.user.username
        logged_in = True

    commento = umslballot.objects.order_by('-skore')
    w = Winners.objects.get()

    for n in commento:
        calculatescore(n, w)

    counter = 1
    for n in range(len(commento)):
        if not n == 0:
            if not commento[n].skore == commento[n - 1].skore:
                counter += 1
        commento[n].place = counter

    context = {'commentz' : commento, 'winnerz' : w, 'urlz' : umslurls, 'name': name, 'logged_in': logged_in}

    return render(request, 'oscarsapp/mainchart.html', context)


def passpage(request, error=''):

#    error = hashlib.sha256(base('').encode()).hexdigest()

    form = Passwordform()
    context = {'form' : form, 'error': error, 'urlz' : oscurls}
    return render(request, 'oscarsapp/passpage.html', context)


def upasspage(request, error=''):
    form = Passwordform()
    context = {'form' : form, 'error': error, 'urlz' : umslurls}
    return render(request, 'oscarsapp/passpage.html', context)


def loadballot(request):

    w = Winners.objects.get()

    if w.active == True:

        if request.user.is_authenticated:

            name = request.user.username

            hasballot = False
            ballots = oscarballot.objects.order_by('-skore')
            ballot = 'none'

            for b in ballots:
                if b.name == name:
                    hasballot = True
                    ballot = b

            form = OscarBallot()

            context = {'name': name, 'hasballot': hasballot, 'ballot': ballot, 'form' : form, 'urlz' : oscurls, 'logged_in': True}
            return render(request, 'oscarsapp/fillballot.html', context)

        else:
            return redirect('passpage')

    else:
        return render(request, 'oscarsapp/inactive.html')


def uloadballot(request):

    w = Winners.objects.get()

    if w.active == True:

        if request.user.is_authenticated:

            name = request.user.username

            hasballot = False
            ballots = umslballot.objects.order_by('-skore')
            ballot = 'none'

            for b in ballots:
                if b.name == name:
                    hasballot = True
                    ballot = b

            form = OscarBallot()

            context = {'name': name, 'hasballot': hasballot, 'ballot': ballot, 'form' : form, 'urlz' : umslurls, 'logged_in': True}
            return render(request, 'oscarsapp/fillballot.html', context)

        else:
            return redirect('upasspage')

    else:

        context = {'urlz': umslurls}
        return render(request, 'oscarsapp/inactive.html', context)


def submitballot(request):
    form = OscarBallot(request.POST)

    if form.is_valid():

        foundb = False

        ballots = oscarballot.objects.order_by('-skore')

        for b in ballots:
            if b.name == request.user.username:
                foundb = True

                b.bestpicture=request.POST['bestpicture']
                b.actor=request.POST['actor']
                b.actress=request.POST['actress']
                b.supactor=request.POST['supactor']
                b.supactress=request.POST['supactress']
                b.animatedfeature=request.POST['animatedfeature']
                b.cinematography=request.POST['cinematography']
                b.costume=request.POST['costume']
                b.directing=request.POST['directing']
                b.documentary=request.POST['documentary']
                b.docshort=request.POST['docshort']
                b.fediting=request.POST['fediting']
                b.foreign=request.POST['foreign']
                b.makeupandh=request.POST['makeupandh']
                b.mscore=request.POST['mscore']
                b.msong=request.POST['msong']
                b.prodesign=request.POST['prodesign']
                b.animatedshort=request.POST['animatedshort']
                b.shortfilm=request.POST['shortfilm']
                b.sound=request.POST['sound']
                b.visualfx=request.POST['visualfx']
                b.writingad=request.POST['writingad']
                b.writingor=request.POST['writingor']
                b.kulr=request.POST['kulr']
                b.save()

        if not foundb:

            new_ballot = oscarballot(name=request.POST['name'],
                bestpicture=request.POST['bestpicture'],
                actor=request.POST['actor'],
                actress=request.POST['actress'],
                supactor=request.POST['supactor'],
                supactress=request.POST['supactress'],
                animatedfeature=request.POST['animatedfeature'],
                cinematography=request.POST['cinematography'],
                costume=request.POST['costume'],
                directing=request.POST['directing'],
                documentary=request.POST['documentary'],
                docshort=request.POST['docshort'],
                fediting=request.POST['fediting'],
                foreign=request.POST['foreign'],
                makeupandh=request.POST['makeupandh'],
                mscore=request.POST['mscore'],
                msong=request.POST['msong'],
                prodesign=request.POST['prodesign'],
                animatedshort=request.POST['animatedshort'],
                shortfilm=request.POST['shortfilm'],
                sound=request.POST['sound'],
                visualfx=request.POST['visualfx'],
                writingad=request.POST['writingad'],
                writingor=request.POST['writingor'],
                kulr=request.POST['kulr'])
            new_ballot.save()

        return redirect('front')

    else:

        return redirect('passpage')


def usubmitballot(request):
    form = OscarBallot(request.POST)

    if form.is_valid():
        foundb = False

        ballots = umslballot.objects.order_by('-skore')

        for b in ballots:
            if b.name == request.user.username:
                foundb = True

                b.bestpicture=request.POST['bestpicture']
                b.actor=request.POST['actor']
                b.actress=request.POST['actress']
                b.supactor=request.POST['supactor']
                b.supactress=request.POST['supactress']
                b.animatedfeature=request.POST['animatedfeature']
                b.cinematography=request.POST['cinematography']
                b.costume=request.POST['costume']
                b.directing=request.POST['directing']
                b.documentary=request.POST['documentary']
                b.docshort=request.POST['docshort']
                b.fediting=request.POST['fediting']
                b.foreign=request.POST['foreign']
                b.makeupandh=request.POST['makeupandh']
                b.mscore=request.POST['mscore']
                b.msong=request.POST['msong']
                b.prodesign=request.POST['prodesign']
                b.animatedshort=request.POST['animatedshort']
                b.shortfilm=request.POST['shortfilm']
                b.sound=request.POST['sound']
                b.visualfx=request.POST['visualfx']
                b.writingad=request.POST['writingad']
                b.writingor=request.POST['writingor']
                b.kulr=request.POST['kulr']
                b.save()

        if not foundb:

            new_ballot = umslballot(name=request.POST['name'],
                bestpicture=request.POST['bestpicture'],
                actor=request.POST['actor'],
                actress=request.POST['actress'],
                supactor=request.POST['supactor'],
                supactress=request.POST['supactress'],
                animatedfeature=request.POST['animatedfeature'],
                cinematography=request.POST['cinematography'],
                costume=request.POST['costume'],
                directing=request.POST['directing'],
                documentary=request.POST['documentary'],
                docshort=request.POST['docshort'],
                fediting=request.POST['fediting'],
                foreign=request.POST['foreign'],
                makeupandh=request.POST['makeupandh'],
                mscore=request.POST['mscore'],
                msong=request.POST['msong'],
                prodesign=request.POST['prodesign'],
                animatedshort=request.POST['animatedshort'],
                shortfilm=request.POST['shortfilm'],
                sound=request.POST['sound'],
                visualfx=request.POST['visualfx'],
                writingad=request.POST['writingad'],
                writingor=request.POST['writingor'],
                kulr=request.POST['kulr'])
            new_ballot.save()

        return redirect('ufront')

    else:

        return redirect('upasspage', error='Form Is Invalid')


def chart(request):

    name = 'none'
    logged_in = False

    if request.user.is_authenticated:
        name = request.user.username
        logged_in = True

    commento = oscarballot.objects.order_by('-date_added')
    w = Winners.objects.get()

    for n in commento:
        calculatescore(n, w)

    context = {'commentz' : commento, 'wn': w, 'wincolor': '#B7A261', 'urlz' : oscurls, 'name': name, 'logged_in': logged_in}
    return render(request, 'oscarsapp/bigchart.html', context)


def uchart(request):

    name = 'none'
    logged_in = False

    if request.user.is_authenticated:
        name = request.user.username
        logged_in = True

    commento = umslballot.objects.order_by('-date_added')
    w = Winners.objects.get()

    for n in commento:
        calculatescore(n, w)

    context = {'commentz' : commento, 'wn': w, 'wincolor': '#B7A261', 'urlz' : umslurls, 'name': name, 'logged_in': logged_in}
    return render(request, 'oscarsapp/bigchart.html', context)


def mychart(request):
    comm = request.GET.get('person')
    w = Winners.objects.get()

    context = {'c' : comm, 'wn': w}
    return render(request, '../../oscarsapp/templates/mychart.html', context)


@login_required
def logout_user(request):

    logout(request)
    return redirect('front')


@login_required
def ulogout_user(request):

    logout(request)
    return redirect('ufront')


