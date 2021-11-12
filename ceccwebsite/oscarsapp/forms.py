from django import forms

def d(opt):
    return (opt, opt)

class Passwordform(forms.Form):
    pswrd = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'inputfield', 'type' : 'password', 'placeholder' : 'password'}))
    username = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'inputfield', 'type' : 'password', 'placeholder' : 'username'}))
    cpswrd = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'inputfield', 'type' : 'password', 'placeholder' : 'user password'}))

class OscarBallot(forms.Form):
    name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'inputfield form-control', 'placeholder' : 'eg: Howard'}))


    f = "The Father"
    j = "Judas and the Black Messiah"
    m = "Mank"
    mn = "Minari"
    n = "Nomadland"
    p = "Promising Young Woman"
    s = "Sound of Metal"
    t = "The Trial of the Chicago 7"
    tt = "Tenet"
    nw = "News of the World"

    BestPicture=(d(f), d(j), d(m), d(mn), d(n), d(p), d(s), d(t))
    Actor=(d("Riz Ahmed"), d("Chadwick Boseman"), d("Anthony Hopkins"), d("Gary Oldman"), d("Steven Yeun"))
    Actress=(d("Viola Davis"), d("Andra Day"), d("Vanessa Kirby"), d("Frances McDormand"), d("Carey Mulligan"))
    SupActor=(d("Sacha Baron Cohen"), d("Daniel Kaluuya"), d("Leslie Odom Jr."), d("Paul Raci"), d("Lakeith Stanfield"))
    SupActress=(d("Maria Bakalova"), d("Glenn Close"), d("Olivia Colman"), d("Amanda Seyfried"), d("Youn Yuh-jung"))
    AnimatedFeature=(d("Onward"), d("Over the Moon"), d("A Shaun the Sheep Movie: Farmageddon"), d("Soul"), d("Wolfwalkers"))
    Cinematography=(d(j), d(m), d(nw), d(n), d(t))
    CostumeDesign=(d("Emma"), d("Ma Rainey's Black Bottom"), d(m), d("Mulan"), d("Pinocchio"))
    Directing=(d("Another Round"), d("Mank"), d("Minari"), d("Nomadland"), d("Promising Young Woman"))
    DocumentaryFeature=(d("Collective"), d("Crip Camp"), d("The Mole Agent"), d("My Octopus Teacher"), d("Time"))
    DocumentaryShort=(d("Colette"), d("A Concerto is a Conversation"), d("Do Not Split"), d("Hunger Ward"), d("A Love Song For Latasha"))
    FilmEditing=(d(f), d(n), d(p), d(s), d(t))
    ForeignLanguage=(d("Another Round"), d("Better Days"), d("Collective"), d("The Man Who Sold His Skin"), d("Quo Vadis, Aida?"))
    MakeupAndHair=(d("Emma"), d("Hillbilly Elegy"), d("Ma Rainey's Black Bottom"), d("Mank"), d("Pinocchio"))
    MusicScore=(d("Da 5 Bloods"), d(m), d("Minari"), d(nw), d("Soul"))
    MusicSong=(d("Fight For You"), d("Hear My Voice"), d("Husavik"), d("Io Si (Seen)"), d("Speak Now"))
    Production=(d(f), d("Ma Rainey's Black Bottom"), d(m), d(nw), d(tt))
    AnimatedShort=(d("Burrow"), d("Genius Loci"), d("If Anything Happens I Love You"), d("Opera"), d("Yes-People"))
    ShortFilm=(d("Feeling Through"), d("The Letter Room"), d("The Present"), d("Two Distant Strangers"), d("White Eye"))
    Sound=(d("Greyhound"), d(m), d(nw), d(s), d("Soul"))
    VisualEffects=(d("Love and Monsters"), d("The Midnight Sky"), d("Mulan"), d("The One and Only Ivan"), d(tt))
    WritingAdapted=(d("Borat Subsequent Moviefilm"), d(f), d(n), d("One Night in Miami..."), d("The White Tiger"))
    WritingOriginal=(d(j), d("Minari"), d(p), d(s), d(t))

    bestpicture = forms.ChoiceField(choices=BestPicture, widget=forms.RadioSelect(attrs={'class' : 'horlist1', 'placeholder' : 'Bestpicpik'}))
    actor = forms.ChoiceField(choices=Actor, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placeholder' : 'Actorpik'}))
    actress = forms.ChoiceField(choices=Actress, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placeholder' : 'Actresspik'}))
    supactor = forms.ChoiceField(choices=SupActor, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'supactorpik'}))
    supactress = forms.ChoiceField(choices=SupActress, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'supactresspik'}))
    animatedfeature = forms.ChoiceField(choices=AnimatedFeature, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'animatedfeaturepik'}))
    cinematography = forms.ChoiceField(choices=Cinematography, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'cinematographypik'}))
    costume = forms.ChoiceField(choices=CostumeDesign, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'costumepik'}))
    directing = forms.ChoiceField(choices=Directing, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'directingpik'}))
    documentary = forms.ChoiceField(choices=DocumentaryFeature, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'docpik'}))
    docshort = forms.ChoiceField(choices=DocumentaryShort, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'docshortpik'}))
    fediting = forms.ChoiceField(choices=FilmEditing, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'feditingpik'}))
    foreign = forms.ChoiceField(choices=ForeignLanguage, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'foreignlangpik'}))
    makeupandh = forms.ChoiceField(choices=MakeupAndHair, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'makeupandhpik'}))
    mscore = forms.ChoiceField(choices=MusicScore, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'musicscorepik'}))
    msong = forms.ChoiceField(choices=MusicSong, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'musicsongpik'}))
    prodesign = forms.ChoiceField(choices=Production, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'productionpik'}))
    animatedshort = forms.ChoiceField(choices=AnimatedShort, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'animatedshortpik'}))
    shortfilm = forms.ChoiceField(choices=ShortFilm, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'shortfilmpik'}))
    sound = forms.ChoiceField(choices=Sound, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'soundpik'}))
    visualfx = forms.ChoiceField(choices=VisualEffects, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'visualeffectspik'}))
    writingad = forms.ChoiceField(choices=WritingAdapted, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'writingadaptedpik'}))
    writingor = forms.ChoiceField(choices=WritingOriginal, widget=forms.RadioSelect(attrs={'class' : 'horlist', 'placedolder' : 'writingoriginalpik'}))
    kulr = forms.CharField(max_length=20, initial='#880000', widget=forms.TextInput(attrs={'class' : 'kulr form-control', 'type': 'color'}))