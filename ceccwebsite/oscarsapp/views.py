from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from .models import Wizard, Ballot, Category, Nomination, Pick
from .forms import OscarBallot, Passwordform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from oscarsapp.data import oscurls, umslurls

import logging
import hashlib

logger = logging.getLogger(__name__)

urlz = {
    "lauer": oscurls,
    "umsystem": umslurls
}


def front(request, version):

    calculate_scores()

    user = 'none'
    logged_in = False

    if request.user.is_authenticated:
        user = request.user.username
        logged_in = True


    ballots = Ballot.objects.filter(game=version).order_by('-skore')

    place = 1
    for count, ballot in enumerate(ballots):
        if count != 0:
            if ballot.skore != ballots[count - 1].skore:
                place += 1
        ballot.place = place
        ballot.save()

    ballots = Ballot.objects.filter(game=version).order_by('-skore')
    categories = Category.objects.order_by('order')

    context = {
        'ballots' : ballots,
        'categories': categories,
        'version' : version,
        'user': user,
        'logged_in': logged_in,
        'wizard': Wizard.objects.get()
    }

    return render(request, 'oscarsapp/mainchart.html', context)


def calculatescore(ballot):
    ballot.skore = 0

    for category in Category.objects.all():
        pick = ballot.pick_set.filter(nomination__category=category)
        if pick and pick[0].nomination == category.winner:
            ballot.skore += category.points

    ballot.vwidth = ballot.skore * 3
    ballot.save()


def calculate_scores():
    for ballot in Ballot.objects.order_by('-skore'):
        calculatescore(ballot)


def create_user(request, version):
    code = request.POST['code']
    username = request.POST['username']
    password = request.POST['password']
    password2 = request.POST['repassword']

    wizard = Wizard.objects.get()

    if not password == password2:
        return redirect("passpage", version=version, error='Passwords Do Not Match')

    hp = hashlib.sha256(code.encode()).hexdigest()
    hash = wizard.lauer_hash if version == "lauer" else wizard.umsl_hash

    if not hp == hash:
        return redirect('passpage', version=version, code=code, error='Incorrect Access Code')

    users = User.objects.order_by('username')
    for u in users:
        if username == u.username:
            return redirect('passpage', version=version, error='user already exists', code=code)

    newuser = User.objects.create_user(username, password=password)
    newuser.save()

    user = authenticate(request, username=username, password=password)

    login(request, user)
    return redirect('loadballot', version=version)


def login_user(request, version):
    username = request.POST['username']
    password = request.POST['password']

    thisuser = authenticate(request, username=username, password=password)

    if thisuser is not None:
        login(request, thisuser)
        return redirect("loadballot", version=version)
    else:
        return redirect("passpage", version=version, error='username or password is wrong')


def passpage(request, version, error='', code=''):

    if error == 'none':
        error = ''

    form = Passwordform()
    context = {
        'form' : form,
        'error': error,
        'code': code,
        'version': version
    }
    return render(request, 'oscarsapp/passpage.html', context)


def loadballot(request, version, code=''):
    if Wizard.objects.get().active == True:

        if request.user.is_authenticated:

            user = request.user.username

            hasballot = False
            ballots = Ballot.objects.filter(game=version)
            ballot = 'none'
            name = user

            for b in ballots:
                if b.user == user:
                    hasballot = True
                    ballot = b
                    name = ballot.name

            form = OscarBallot()

            categories = Category.objects.order_by('order')

            context = {
                'user': user,
                'name': name,
                'hasballot': hasballot,
                'ballot': ballot,
                'form' : form,
                'version': version,
                'logged_in': True,
                'cats': categories
            }

            return render(request, 'oscarsapp/fillballot.html', context)

        else:
            if code:
                return redirect("passpage", version=version, error='none', code=code)
            return redirect("passpage", version=version)

    else:
        context = {'version': version}
        return render(request, 'oscarsapp/inactive.html', context)


def winnerform(request):

    user = request.user
    if user.is_superuser:

        context = {'user': user, 'cats': Category.objects.order_by('order')}
        return render(request, 'oscarsapp/winnerform.html', context)

    else:
        return redirect(
            "passpage",
            version="lauer",
            error="Must be admin to access"
        )


def submit_winners(request):

    user = request.user
    if user.is_superuser:

        for c in Category.objects.order_by('order'):
            if c.shortname in request.POST:
                if request.POST[c.shortname] == "TBD":
                    c.winner = None
                    c.save()
                else:
                    c.winner = Nomination.objects.get(category=c, nominee__name=request.POST[c.shortname])
                    c.save()

        context = {'user': user, 'cats': Category.objects.order_by('order')}
        return render(request, 'oscarsapp/winnerform.html', context)

    else:
        return redirect(
            "passpage",
            version="lauer",
            error="Must be admin to access"
        )


def submitballot(request, version):
    form = OscarBallot(request.POST)

    if form.is_valid():

        ballots = Ballot.objects.filter(game=version)
        hidden = True if 'hide_ballot' in request.POST else False
        username = request.user.username

        name = request.POST['name']
        duplicate = False
        for ballot in ballots:
            if request.user.username != ballot.user and name == ballot.name:
                duplicate = True

        if duplicate:
            for ballot in ballots:
                if ballot.user == username:
                    name = ballot.name

        ballot = None
        for bal in ballots:
            if bal.user == username:
                ballot = bal


        if ballot:
            ballot.name=name
            ballot.game=request.POST['version']
            ballot.kulr=request.POST['kulr']
            ballot.hidden=hidden
            ballot.save()

            for pick in ballot.pick_set.all():
                shortname = pick.nomination.category.shortname
                if shortname in request.POST:
                    pick.nomination = Nomination.objects.get(category__shortname=shortname, nominee__name=request.POST[shortname])
                    pick.save()

        else:
            ballot = Ballot(
                user=username,
                game=request.POST['version'],
                name=name,
                kulr=request.POST['kulr'],
                hidden=hidden
            )

            ballot.save()

            categories = Category.objects.all()
            for c in categories:
                shortname = c.shortname
                if shortname in request.POST:
                    nom = Nomination.objects.get(category__shortname=shortname, nominee__name=request.POST[shortname])
                    pick = Pick(ballot=ballot, nomination=nom)
                    pick.save()

        return redirect('front', version=version)

    else:
        return redirect('passpage', version=version, error=form.errors)


def chart(request, version):
    calculate_scores()
    user = 'none'
    logged_in = False

    if request.user.is_authenticated:
        user = request.user.username
        logged_in = True

    context = {
        'categories': Category.objects.order_by('order'),
        'ballots': Ballot.objects.filter(game=version).order_by('-skore'),
        'wincolor': '#B7A261',
        'version': version,
        'user': user,
        'logged_in': logged_in,
        'wizard': Wizard.objects.get()
    }
    return render(request, 'oscarsapp/bigchart.html', context)


def showhash(request, text):
    return render(
        request,
        'oscarsapp/showhash.html',
        {'hash': hashlib.sha256(text.encode()).hexdigest()}
    )


@login_required
def logout_user(request, version):

    logout(request)
    return redirect("front", version=version)
