from django import forms

class Teamform(forms.Form):
    name = forms.CharField(max_length=30,
    widget=forms.TextInput(attrs={'class' : 'inputfield'}))
    pswrd = forms.CharField(max_length=30,
        widget=forms.TextInput(attrs={'class' : 'inputfield', 'type' : 'password'}))
    kulr = forms.CharField(max_length=20, initial='#003388', widget=forms.TextInput(attrs={'type': 'color'}))

class Answerform(forms.Form):
    roundno = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder' : 1}))
    answer1 = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class' : 'inputfield'}))
    answer2 = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class' : 'inputfield'}))
    answer3 = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class' : 'inputfield'}))
    answer4 = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class' : 'inputfield'}))
    answer5 = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class' : 'inputfield'}))
    answer6 = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class' : 'inputfield'}))
    answer7 = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class' : 'inputfield'}))
    answer8 = forms.CharField(max_length=100,
        widget=forms.TextInput(attrs={'class' : 'inputfield'}))


class Tallypoints(forms.Form):
    cbox1 = forms.BooleanField(required=False)
    cbox2 = forms.BooleanField(required=False)
    cbox3 = forms.BooleanField(required=False)
    cbox4 = forms.BooleanField(required=False)
    cbox5 = forms.BooleanField(required=False)
    cbox6 = forms.BooleanField(required=False)
    cbox7 = forms.BooleanField(required=False)
    cbox8 = forms.BooleanField(required=False)