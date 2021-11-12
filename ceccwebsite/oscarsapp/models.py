from django.db import models
from django.utils import timezone

def d(opt):
    return (opt, opt)

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

tb = (('tbd', 'tbd'),)

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

class oscarballot(models.Model):

    name = models.CharField(max_length=100, default='NA')
    bestpicture = models.CharField(max_length=100, choices=BestPicture, default='NA')
    actor = models.CharField(max_length=100, choices=Actor, default='NA')
    actress = models.CharField(max_length=100, choices=Actress, default='NA')
    supactor = models.CharField(max_length=100, choices=SupActor, default='NA')
    supactress = models.CharField(max_length=100, choices=SupActress, default='NA')
    animatedfeature = models.CharField(max_length=100, choices=AnimatedFeature, default='NA')
    cinematography = models.CharField(max_length=100, choices=Cinematography, default='NA')
    costume = models.CharField(max_length=100, choices=CostumeDesign, default='NA')
    directing = models.CharField(max_length=100, choices=Directing, default='NA')
    documentary = models.CharField(max_length=100, choices=DocumentaryFeature, default='NA')
    docshort = models.CharField(max_length=100, choices=DocumentaryShort, default='NA')
    fediting = models.CharField(max_length=100, choices=FilmEditing, default='NA')
    foreign = models.CharField(max_length=100, choices=ForeignLanguage, default='NA')
    makeupandh = models.CharField(max_length=100, choices=MakeupAndHair, default='NA')
    mscore = models.CharField(max_length=100, choices=MusicScore, default='NA')
    msong = models.CharField(max_length=100, choices=MusicSong, default='NA')
    prodesign = models.CharField(max_length=100, choices=Production, default='NA')
    animatedshort = models.CharField(max_length=100, choices=AnimatedShort, default='NA')
    shortfilm = models.CharField(max_length=100, choices=ShortFilm, default='NA')
    sound = models.CharField(max_length=100, choices=Sound, default='NA')
    visualfx = models.CharField(max_length=100, choices=VisualEffects, default='NA')
    writingad = models.CharField(max_length=100, choices=WritingAdapted, default='NA')
    writingor = models.CharField(max_length=100, choices=WritingOriginal, default='NA')
    skore = models.IntegerField(default=0)
    place = models.IntegerField(default=1)
    vwidth = models.IntegerField(default=0)
    kulr = models.CharField(max_length=20, default='#fc0')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.name, self.id)

class umslballot(models.Model):

    name = models.CharField(max_length=100, default='NA')
    bestpicture = models.CharField(max_length=100, choices=BestPicture, default='NA')
    actor = models.CharField(max_length=100, choices=Actor, default='NA')
    actress = models.CharField(max_length=100, choices=Actress, default='NA')
    supactor = models.CharField(max_length=100, choices=SupActor, default='NA')
    supactress = models.CharField(max_length=100, choices=SupActress, default='NA')
    animatedfeature = models.CharField(max_length=100, choices=AnimatedFeature, default='NA')
    cinematography = models.CharField(max_length=100, choices=Cinematography, default='NA')
    costume = models.CharField(max_length=100, choices=CostumeDesign, default='NA')
    directing = models.CharField(max_length=100, choices=Directing, default='NA')
    documentary = models.CharField(max_length=100, choices=DocumentaryFeature, default='NA')
    docshort = models.CharField(max_length=100, choices=DocumentaryShort, default='NA')
    fediting = models.CharField(max_length=100, choices=FilmEditing, default='NA')
    foreign = models.CharField(max_length=100, choices=ForeignLanguage, default='NA')
    makeupandh = models.CharField(max_length=100, choices=MakeupAndHair, default='NA')
    mscore = models.CharField(max_length=100, choices=MusicScore, default='NA')
    msong = models.CharField(max_length=100, choices=MusicSong, default='NA')
    prodesign = models.CharField(max_length=100, choices=Production, default='NA')
    animatedshort = models.CharField(max_length=100, choices=AnimatedShort, default='NA')
    shortfilm = models.CharField(max_length=100, choices=ShortFilm, default='NA')
    sound = models.CharField(max_length=100, choices=Sound, default='NA')
    visualfx = models.CharField(max_length=100, choices=VisualEffects, default='NA')
    writingad = models.CharField(max_length=100, choices=WritingAdapted, default='NA')
    writingor = models.CharField(max_length=100, choices=WritingOriginal, default='NA')
    skore = models.IntegerField(default=0)
    vwidth = models.IntegerField(default=0)
    wwidth = models.IntegerField(default=0)
    kulr = models.CharField(max_length=20, default='#fc0')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.name, self.id)

class Winners(models.Model):

    BestPicturew = tb + BestPicture
    Actorw = tb + Actor
    Actressw = tb + Actress
    SupActorw = tb + SupActor
    SupActressw = tb + SupActress
    AnimatedFeaturew = tb + AnimatedFeature
    Cinematographyw = tb + Cinematography
    CostumeDesignw = tb + CostumeDesign
    Directingw = tb + Directing
    DocumentaryFeaturew = tb + DocumentaryFeature
    DocumentaryShortw = tb + DocumentaryShort
    FilmEditingw = tb + FilmEditing
    ForeignLanguagew = tb + ForeignLanguage
    MakeupAndHairw = tb + MakeupAndHair
    MusicScorew = tb + MusicScore
    MusicSongw = tb + MusicSong
    Productionw = tb + Production
    AnimatedShortw = tb + AnimatedShort
    ShortFilmw = tb + ShortFilm
    Soundw = tb + Sound
    VisualEffectsw = tb + VisualEffects
    WritingAdaptedw = tb + WritingAdapted
    WritingOriginalw = tb + WritingOriginal

    bestpicture = models.CharField(max_length=100, choices=BestPicturew, default='NA')
    actor = models.CharField(max_length=100, choices=Actorw, default='NA')
    actress = models.CharField(max_length=100, choices=Actressw, default='NA')
    supactor = models.CharField(max_length=100, choices=SupActorw, default='NA')
    supactress = models.CharField(max_length=100, choices=SupActressw, default='NA')
    animatedfeature = models.CharField(max_length=100, choices=AnimatedFeaturew, default='NA')
    cinematography = models.CharField(max_length=100, choices=Cinematographyw, default='NA')
    costume = models.CharField(max_length=100, choices=CostumeDesignw, default='NA')
    directing = models.CharField(max_length=100, choices=Directingw, default='NA')
    documentary = models.CharField(max_length=100, choices=DocumentaryFeaturew, default='NA')
    docshort = models.CharField(max_length=100, choices=DocumentaryShortw, default='NA')
    fediting = models.CharField(max_length=100, choices=FilmEditingw, default='NA')
    foreign = models.CharField(max_length=100, choices=ForeignLanguagew, default='NA')
    makeupandh = models.CharField(max_length=100, choices=MakeupAndHairw, default='NA')
    mscore = models.CharField(max_length=100, choices=MusicScorew, default='NA')
    msong = models.CharField(max_length=100, choices=MusicSongw, default='NA')
    prodesign = models.CharField(max_length=100, choices=Productionw, default='NA')
    animatedshort = models.CharField(max_length=100, choices=AnimatedShortw, default='NA')
    shortfilm = models.CharField(max_length=100, choices=ShortFilmw, default='NA')
    sound = models.CharField(max_length=100, choices=Soundw, default='NA')
    visualfx = models.CharField(max_length=100, choices=VisualEffectsw, default='NA')
    writingad = models.CharField(max_length=100, choices=WritingAdaptedw, default='NA')
    writingor = models.CharField(max_length=100, choices=WritingOriginalw, default='NA')

    active = models.BooleanField(default=True)

    def __str__(self):
        return 'WINNERS'
