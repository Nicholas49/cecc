from django import forms
from oscarsapp.data import noms

def d(opt):
    return (opt, opt)

def get_noms(cat):
    choicelist = []
    for n in noms:
        if n['shortname'] == cat:
            for c in n['nominees']:
                choicelist.append((c['name'], c['name']))
    return choicelist

class Passwordform(forms.Form):
    pswrd = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'inputfield', 'type' : 'password', 'placeholder' : 'password'}))
    username = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'inputfield', 'type' : 'password', 'placeholder' : 'username'}))
    cpswrd = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'inputfield', 'type' : 'password', 'placeholder' : 'user password'}))

class OscarBallot(forms.Form):
    name = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'inputfield form-control', 'placeholder' : 'Name'}))
    kulr = forms.CharField(max_length=20, initial='#880000', widget=forms.TextInput(attrs={'class' : 'kulr form-control', 'type': 'color'}))
    hide_ballot = forms.BooleanField(required=False)