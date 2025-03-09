from django.shortcuts import render, redirect, HttpResponse
from .models import jeopardyboard, CategoryTitle, finaljeopardy, team, wizard, game


def board(request, game_name='default'):

    answers = jeopardyboard.objects.filter(game=game_name)
    cats = CategoryTitle.objects.filter(game=game_name, jround='single')
    teams = team.objects.order_by('teamno')
    wiz = wizard.objects.get()


    context = {'answers': answers,
        'categories': cats,
        'game_name': game_name,
        'teams': teams,
        'wiz': wiz}

    return render(request, 'jeopardy/board.html', context)


def board2(request, game_name='default'):

    answers = jeopardyboard.objects.filter(game=game_name)
    cats = CategoryTitle.objects.filter(game=game_name, jround='double')
    teams = team.objects.order_by('teamno')
    wiz = wizard.objects.get()

    context = {'answers': answers,
        'categories': cats,
        'game_name': game_name,
        'teams': teams,
        'wiz': wiz}

    return render(request, 'jeopardy/board2.html', context)


def showanswer1(request, game_name='default', jcat='cat1', dollar='800'):

    teams = team.objects.order_by('teamno')
    wiz = wizard.objects.get()

    turn = wiz.turn

    wiz.turn += 1
    if wiz.turn > len(teams):
        wiz.turn = 1
    wiz.save()

    return redirect('showanswer2', game_name=game_name, jcat=jcat, dollar=dollar, turn=turn)


def showanswer2(request, game_name='default', jcat='cat1', dollar='800', turn=1):

    jround = ''
    janswer = ''
    jquestion = ''
    jcatname = ''
    jdollar = ''
    isdouble = False

    answers = jeopardyboard.objects.filter(game=game_name)
    cat = CategoryTitle.objects.filter(game=game_name, category=jcat)
    teams = team.objects.order_by('teamno')

    catname = 'none'
    if len(cat) != 0:
        catname = cat[0].catname

    for a in answers:
        if a.category == jcat and a.dollar == dollar:
            jround = a.jround
            janswer = a.answer
            jquestion = a.question
            jcatname = catname
            jdollar = a.dollar
            isdouble = a.isdouble

            a.isactive = False
            a.save()

    context = {'game_name': game_name,
        'jround': jround,
        'catname': jcatname,
        'dollar': jdollar,
        'answer': janswer,
        'question': jquestion,
        'isdouble': isdouble,
        'teams': teams,
        'turn': turn}

    return render(request, 'jeopardy/showanswer.html', context)


def showexample(request, game_name='default', jcat='cat1'):

    jround = ''
    janswer = ''
    jquestion = ''
    jcatname = ''

    answers = jeopardyboard.objects.filter(game=game_name)
    cat = CategoryTitle.objects.get(game=game_name, category=jcat)

    for a in answers:
        if a.category == jcat and a.dollar == 'ex':
            jround = a.jround
            janswer = a.answer
            jquestion = a.question
            jcatname = cat.catname

            a.isactive = False
            a.save()

    if jround == 'single':
        jround = 'play'

    context = {'game_name': game_name,
        'jround': jround,
        'catname': jcatname,
        'answer': janswer,
        'question': jquestion}

    return render(request, 'jeopardy/showexample.html', context)


def move_turn(request):
    teams = team.objects.order_by('teamno')
    wiz = wizard.objects.get()

    direc = request.GET['direc']

    if direc == 'f':
        wiz.turn += 1
        if wiz.turn > len(teams):
            wiz.turn = 1

    if direc == 'b':
        wiz.turn -= 1
        if wiz.turn < 1:
            wiz.turn = len(teams)

    wiz.save()

    jround = request.GET['round']
    gname = request.GET['gname']

    if jround == 'single':
        return redirect('board', game_name=gname)
    if jround == 'double':
        return redirect('board2', game_name=gname)




def reset(request, gname='default'):

    answers = jeopardyboard.objects.filter(game=gname)
    teams = team.objects.order_by('teamno')
    wiz = wizard.objects.get()

    wiz.turn = 1
    wiz.save()

    for a in answers:
        a.isactive = True
        a.save()

    for t in teams:
        t.points = 0;
        t.save()

    return redirect('board', game_name=gname)


def final(request, game_name='default'):

    final = finaljeopardy.objects.filter(game=game_name)
    teams = team.objects.order_by('teamno')

    context = {'final': final, 'game_name': game_name, 'teams': teams}

    return render(request, 'jeopardy/final.html', context)


def make_game(request):

    gname = request.POST['game_name']
    jrou = request.POST['jround']
    answ = request.POST['answer']
    ques = request.POST['question']
    dd = False

    if 'dailydouble' in request.POST:
        dd = True

    answers = jeopardyboard.objects.filter(game=gname, jround=jrou)

    isnew = True

    for a in answers:
        if a.category == request.POST['category'] and a.dollar == request.POST['dollar']:
            isnew = False
            if answ == '' and ques == '' and dd == False:
                a.delete()
            else:
                a.answer = answ
                a.question = request.POST['question']
                a.isdouble = dd
                a.save()

    if isnew:
        newboard = jeopardyboard(game=gname,
            jround = jrou,
            category = request.POST['category'],
            dollar = request.POST['dollar'],
            answer = answ,
            isdouble = dd,
            question = ques)
        newboard.save()

    if jrou == 'single':
        return redirect('edit_game', game_name=gname)
    if jrou == 'double':
        return redirect('edit_game2', game_name=gname)

    return redirect('edit_game', game_name=gname)


def make_category(request):

    gname = request.POST['game_name']
    answ = request.POST['answer']
    jrou = request.POST['jround']

    cats = CategoryTitle.objects.filter(game=gname, jround=jrou)

    isnew = True

    for c in cats:
        if c.category == request.POST['category']:
            isnew = False
            c.catname = answ
            c.save()

    if isnew:
        newcat = CategoryTitle(game=gname,
            jround = jrou,
            category = request.POST['category'],
            catname = answ)
        newcat.save()

    if jrou == 'single':
        return redirect('edit_game', game_name=gname)
    if jrou == 'double':
        return redirect('edit_game2', game_name=gname)

    return redirect('edit_game', game_name=gname)


def make_final(request):
    gname = request.POST['game_name']
    cat = request.POST['category']
    answ = request.POST['answer']
    ques = request.POST['question']

    finals = finaljeopardy.objects.all()

    isnew = True

    for f in finals:
        if f.game == gname:
            isnew = False
            f.catname = cat
            f.answer = answ
            f.question = ques
            f.save()

    if isnew:
        newfinal = finaljeopardy(game = gname,
            catname = cat,
            answer = answ,
            question = ques)
        newfinal.save()

    return redirect('edit_gamef', game_name=gname)


def new_game(request, game_name='default', creator='John Doe'):

    games = game.objects.all()
    for g in games:
        if g.gname == game_name:
            return redirect('menu2')

    new_game = game(gname=game_name, creator=creator)
    new_game.save()
    return redirect('edit_game', game_name=game_name)


def edit_game(request, game_name='default'):

    answers = jeopardyboard.objects.filter(game=game_name)
    cats = CategoryTitle.objects.filter(game=game_name)

    catlist = ['cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6']
    numlist = ['ex', '200', '400', '600', '800', '1000']

    context = {'answers': answers, 'categories': cats, 'game_name': game_name, 'catlist': catlist, 'numlist': numlist}

    return render(request, 'jeopardy/create_game.html', context)


def edit_game2(request, game_name='default'):

    answers = jeopardyboard.objects.filter(game=game_name)
    cats = CategoryTitle.objects.filter(game=game_name)

    catlist = ['cat7', 'cat8', 'cat9', 'cat10', 'cat11', 'cat12']
    numlist = ['ex', '400', '800', '1200', '1600', '2000']

    context = {'answers': answers, 'categories': cats, 'game_name': game_name, 'catlist': catlist, 'numlist': numlist}

    return render(request, 'jeopardy/create_game2.html', context)


def edit_gamef(request, game_name='default'):

    final = finaljeopardy.objects.filter(game=game_name)

    context = {'final': final, 'game_name': game_name}

    return render(request, 'jeopardy/create_gamef.html', context)


def tallypoints(request):

    teams = team.objects.order_by('teamno')
    jrou = request.POST['jround']
    gname = request.POST['gname']

    for t in teams:
        if t.teamname in request.POST:
            t.points += int(request.POST['dollaramount'])
            t.save()

    if jrou == 'single':
        return redirect('board', game_name=gname)
    if jrou == 'double':
        return redirect('board2', game_name=gname)

    return redirect('board', game_name=gname)


def tallydouble(request):

    teams = team.objects.order_by('teamno')
    jrou = request.POST['jround']
    gname = request.POST['gname']

    for t in teams:
        if t.teamname in request.POST:
            t.points += int(request.POST['wager'])
            t.save()

    if jrou == 'single':
        return redirect('board', game_name=gname)
    if jrou == 'double':
        return redirect('board2', game_name=gname)

    return redirect('board', game_name=gname)


def endgame(request):

    teams = team.objects.order_by('teamno')

    gname = request.POST['game_name']

    for t in teams:
        if t.teamname in request.POST:
            t.points += int(request.POST[t.teamname])
            t.save()

    topscore = 0
    winner = 'none'

    for t in teams:
        if t.points > topscore:
            topscore = t.points
            winner = t.teamname

    return redirect(results, topscore, winner, gname)


def results(request, topscore=0, winner='???', game_name='default'):

    teams = team.objects.order_by('teamno')

    context = {'teams': teams, 'topscore': topscore, 'winner': winner, 'game_name': game_name}

    return render(request, 'jeopardy/endgame.html', context)


def editteam(request):

    teams = team.objects.filter(teamno=request.GET['tno'])

    for t in teams:
        t.teamname = request.GET['tname']
        t.points = request.GET['score']
        t.save()

    if request.GET['round'] == 'single':
        return redirect('board', game_name=request.GET['gname'])
    if request.GET['round'] == 'double':
        return redirect('board2', game_name=request.GET['gname'])


def old_menu(request):

    answers = jeopardyboard.objects.all()
    ranswers = reversed(answers)
    cats = CategoryTitle.objects.all()
    rcats = reversed(cats)

    games = []

    for a in ranswers:
        if not a.game in games:
            games.append(a.game)

    for c in rcats:
        if not c.game in games:
            games.append(c.game)

#    for a in ranswers:
#        if not a.game in games:
#            games.append(a.game)

    context = {'games': games}

    return render(request, 'jeopardy/menu.html', context)


def menu(request):

    games = game.objects.all()

    context = {'games': games}

    return render(request, 'jeopardy/menu2.html', context)


def delete_game(request, game_name='foo'):

#    answers = jeopardyboard.objects.filter(game=game_name)
#    cats = CategoryTitle.objects.filter(game=game_name)

#    for a in answers:
#        a.delete()

#    for c in cats:
#        c.delete()

    return redirect('menu')


def change_name(request):

    oldname = request.POST['oldname']
    newname = request.POST['newname']
    jround = request.POST['jround']

    jgame = game.objects.get(gname=oldname)
    answers = jeopardyboard.objects.filter(game=oldname)
    cats = CategoryTitle.objects.filter(game=oldname)
    final = finaljeopardy.objects.filter(game=oldname)

    for a in answers:
        a.game = newname
        a.save()

    for c in cats:
        c.game = newname
        c.save()

    for f in final:
        f.game = newname
        f.save()

    jgame.gname = newname
    jgame.save()

    if jround == 'single':
        return redirect('edit_game', game_name=newname)
    elif jround == 'double':
        return redirect('edit_game2', game_name=newname)
    else:
        return redirect('edit_gamef', game_name=newname)


def shiftup(request):

    gname = request.GET['game_name']
    jround = request.GET['jround']
    category = request.GET['category']

    answers = jeopardyboard.objects.filter(game=gname, jround=jround, category=category)

    if jround == 'single':
        for a in answers:
            if a.dollar == '200':
                a.dollar = 'xx'
            if a.dollar == '400':
                a.dollar = '200'
            if a.dollar == '600':
                a.dollar = '400'
            if a.dollar == '800':
                a.dollar = '600'
            if a.dollar == '1000':
                a.dollar = '800'
            if a.dollar == 'xx':
                a.dollar = '1000'
            a.save()
    if jround == 'double':
        for a in answers:
            if a.dollar == '400':
                a.dollar = 'xx'
            if a.dollar == '800':
                a.dollar = '400'
            if a.dollar == '1200':
                a.dollar = '800'
            if a.dollar == '1600':
                a.dollar = '1200'
            if a.dollar == '2000':
                a.dollar = '1600'
            if a.dollar == 'xx':
                a.dollar = '2000'
            a.save()

    if jround == 'single':
        return redirect('edit_game', game_name=gname)
    elif jround == 'double':
        return redirect('edit_game2', game_name=gname)
    else:
        return redirect('edit_gamef', game_name=gname)


def shiftdown(request):

    gname = request.GET['game_name']
    jround = request.GET['jround']
    category = request.GET['category']

    answers = jeopardyboard.objects.filter(game=gname, jround=jround, category=category)

    if jround == 'single':
        for a in answers:
            if a.dollar == '1000':
                a.dollar = 'xx'
            if a.dollar == '800':
                a.dollar = '1000'
            if a.dollar == '600':
                a.dollar = '800'
            if a.dollar == '400':
                a.dollar = '600'
            if a.dollar == '200':
                a.dollar = '400'
            if a.dollar == 'xx':
                a.dollar = '200'
            a.save()
    if jround == 'double':
        for a in answers:
            if a.dollar == '2000':
                a.dollar = 'xx'
            if a.dollar == '1600':
                a.dollar = '2000'
            if a.dollar == '1200':
                a.dollar = '1600'
            if a.dollar == '800':
                a.dollar = '1200'
            if a.dollar == '400':
                a.dollar = '800'
            if a.dollar == 'xx':
                a.dollar = '400'
            a.save()

    if jround == 'single':
        return redirect('edit_game', game_name=gname)
    elif jround == 'double':
        return redirect('edit_game2', game_name=gname)
    else:
        return redirect('edit_gamef', game_name=gname)


def shiftright(request):

    gname = request.GET['game_name']
    jround = request.GET['jround']
    category1 = request.GET['category']
    category2 = 'foo'
    if category1 == 'cat12':
        category2 = 'cat1'
    else:
        category2 = 'cat' + str(int(category1[3:]) + 1)

    answers1 = jeopardyboard.objects.filter(game=gname, category=category1)
    answers2 = jeopardyboard.objects.filter(game=gname, category=category2)

    cat1 = CategoryTitle.objects.filter(game=gname, category=category1)
    cat2 = CategoryTitle.objects.filter(game=gname, category=category2)

    if category1 == 'cat6':
        for c in cat1:
            c.jround = 'double'
            c.save()
        for c in cat2:
            c.jround = 'single'
            c.save()
        for a in answers1:
            a.jround = 'double'
            if not a.dollar == 'ex':
                a.dollar = str(int(a.dollar) * 2)
            a.save()
        for a in answers2:
            a.jround = 'single'
            if not a.dollar == 'ex':
                a.dollar = str(int(a.dollar) // 2)
            a.save()

    if category1 == 'cat12':
        for c in cat1:
            c.jround = 'single'
            c.save()
        for c in cat2:
            c.jround = 'double'
            c.save()
        for a in answers1:
            a.jround = 'single'
            if not a.dollar == 'ex':
                a.dollar = str(int(a.dollar) // 2)
            a.save()
        for a in answers2:
            a.jround = 'double'
            if not a.dollar == 'ex':
                a.dollar = str(int(a.dollar) * 2)
            a.save()

    for a in answers1:
        a.category = 'bar'
        a.save()
    for c in cat1:
        c.category = 'bar'
        c.save()
    for a in answers2:
        a.category = category1
        a.save()
    for c in cat2:
        c.category = category1
        c.save()

    answersbar = jeopardyboard.objects.filter(game=gname, category='bar')
    catbar = CategoryTitle.objects.filter(game=gname, category='bar')

    for a in answersbar:
        a.category = category2
        a.save()
    for c in catbar:
        c.category = category2
        c.save()

    if jround == 'single':
        return redirect('edit_game', game_name=gname)
    elif jround == 'double':
        return redirect('edit_game2', game_name=gname)
    else:
        return redirect('edit_gamef', game_name=gname)


def gen_games(request):

    answers = jeopardyboard.objects.all()

    already_made = []

    for a in answers:
        if a.game in already_made:
            continue
        else:
            already_made.append(a.game)

    hr = ''
    for al in already_made:
        newgame = game(gname = al,
            creator = '')
        newgame.save()

    return HttpResponse(hr)



def hello(request):

    a = 1
    b = 1

    d = ''

    for n in range(100):
        d += str(b / a) + '<br>'
        a, b = (b, a + b)

    return HttpResponse(d)


