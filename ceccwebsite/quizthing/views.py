from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import Teamform, Answerform, Tallypoints
from .models import answerset, teamproxy


def frontpage(request):

    form = Teamform()

    context = {'form' : form}
    return render(request, 'quizthing/frontpage.html', context)


@login_required
def answerform(request, roundnum=1):

    form = Answerform()

    context = {'form' : form, 'roundnum' : roundnum}
    return render(request, 'quizthing/answerpage.html', context)


def maketeam(request):

    username = request.POST['name']
    password = request.POST['pswrd']
    color = request.POST['kulr']

    team = User.objects.create_user(username, password=password)
    team.save()

    newteam = teamproxy(teamname=username,
    points=0,
    teamcolor=color)
    newteam.save()

    user = authenticate(request, username=username, password=password)

    login(request, user)
    return redirect('answerform/1')


def loginteam(request):

    username = request.POST['name']
    password = request.POST['pswrd']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        return redirect('showanswers')
    else:
        return redirect('frontpage')


@login_required
def submitanswers(request):

    roundnumber = request.POST['roundno']

    new_answerset = answerset(roundno=roundnumber,
    answer1=request.POST['answer1'],
    answer2=request.POST['answer2'],
    answer3=request.POST['answer3'],
    answer4=request.POST['answer4'],
    answer5=request.POST['answer5'],
    answer6=request.POST['answer6'],
    answer7=request.POST['answer7'],
    answer8=request.POST['answer8'],
    teamname=request.user.username)
    new_answerset.save()

    return redirect(showanswers, roundnum=roundnumber)


def showanswers(request, roundnum=1):

    answersets = answerset.objects.order_by('answer1')
    teams = teamproxy.objects.order_by('teamname')

    form = Tallypoints()

    rounds = range(1, 7)

    openrounds = []

    for r in rounds:
        finished = False
        for a in answersets:
            if a.teamname == request.user.username and a.roundno == r:
                finished = True
        if not finished:
            openrounds.append(r)


    context = {'answersets' : answersets,
        'teams' : teams,
        'form' : form,
        'rounds' : rounds,
        'roundnum' : roundnum,
        'openrounds' : openrounds}
    return render(request, 'quizthing/showanswers.html', context)


@login_required
def tallypoints(request):

    form = Tallypoints(request.POST)

    answersets = answerset.objects.order_by('teamname')

    teams = teamproxy.objects.order_by('teamname')
    for t in teams:
        t.points = 0
        t.save()

    roundnum = request.POST['roundnum']

    if form.is_valid():
        for a in answersets:
            if a.teamname == request.POST['team'] and str(a.roundno) == str(roundnum):
                if 'cbox1' in request.POST:
                    a.point1 = True
                    a.save()
                else:
                    a.point1 = False
                    a.save()
                if 'cbox2' in request.POST:
                    a.point2 = True
                    a.save()
                else:
                    a.point2 = False
                    a.save()
                if 'cbox3' in request.POST:
                    a.point3 = True
                    a.save()
                else:
                    a.point3 = False
                    a.save()
                if 'cbox4' in request.POST:
                    a.point4 = True
                    a.save()
                else:
                    a.point4 = False
                    a.save()
                if 'cbox5' in request.POST:
                    a.point5 = True
                    a.save()
                else:
                    a.point5 = False
                    a.save()
                if 'cbox6' in request.POST:
                    a.point6 = True
                    a.save()
                else:
                    a.point6 = False
                    a.save()
                if 'cbox7' in request.POST:
                    a.point7 = True
                    a.save()
                else:
                    a.point7 = False
                    a.save()
                if 'cbox8' in request.POST:
                    a.point8 = True
                    a.save()
                else:
                    a.point8 = False
                    a.save()

        for a in answersets:
            for t in teams:
                if a.teamname == t.teamname:
                    if a.point1 == True:
                        t.points += 1
                        t.save()
                    if a.point2 == True:
                        t.points += 1
                        t.save()
                    if a.point3 == True:
                        t.points += 1
                        t.save()
                    if a.point4 == True:
                        t.points += 1
                        t.save()
                    if a.point5 == True:
                        t.points += 1
                        t.save()
                    if a.point6 == True:
                        t.points += 1
                        t.save()
                    if a.point7 == True:
                        t.points += 1
                        t.save()
                    if a.point8 == True:
                        t.points += 1
                        t.save()



    return redirect('showanswers', roundnum)


@login_required
def logoutteam(request):

    logout(request)
    return redirect('frontpage')


def resetgame(request):
    answersets = answerset.objects.order_by('teamname')
    teams = teamproxy.objects.order_by('teamname')

    for a in answersets:
        a.delete()

    teams = teamproxy.objects.order_by('teamname')

    for t in teams:
        t.points = 0
        t.save()

    return redirect('showanswers')

def second(request):
    context = {'a': ''}
    return render(request, 'quizthing/second.html', context)
