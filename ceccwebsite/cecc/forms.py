from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    phone = forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}))
    email = forms.CharField(max_length=40,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    comment = forms.CharField(max_length=1000,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}))

class MenuForm(forms.Form):

    seasons = (
        ('ASPR', 'Spring'),
        ('BSSM', 'Spring/Summer'),
        ('CSUM', 'Summer'),
        ('DAUW', 'Autumn/Winter')
    )

    weekdays = (
        ('AMON', 'Monday'),
        ('BTUE', 'Tuesday'),
        ('CWED', 'Wednesday'),
        ('DTHU', 'Thursday'),
        ('EFRI', 'Friday')
    )

    season = forms.ChoiceField(choices = seasons, label="", initial='',
    widget=forms.Select(attrs={'class': 'form-control signmenu'}), required=True)
    week = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control signmenu'}), initial=1)
    weekday = forms.ChoiceField(choices = weekdays, label="", initial='',
    widget=forms.Select(attrs={'class': 'form-control signmenu'}), required=True)
    breakfast = forms.CharField(max_length=500,
    widget=forms.Textarea(attrs={'class': 'form-control textbox', 'placeholder': 'Breakfast'}))
    lunch = forms.CharField(max_length=500,
    widget=forms.Textarea(attrs={'class': 'form-control textbox', 'placeholder': 'Lunch'}))
    snack = forms.CharField(max_length=500,
    widget=forms.Textarea(attrs={'class': 'form-control textbox', 'placeholder': 'Snack'}))
    pswrd = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class EventForm(forms.Form):

    weekdays = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday')
    )

    months = (
        (1, 'January'),
        (2, 'February'),
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    )

    month = forms.ChoiceField(choices = months, initial='January',
    widget=forms.Select(), required=True)
    dayno = forms.IntegerField()
    weekday = forms.ChoiceField(choices = weekdays, label="", initial='',
    widget=forms.Select(), required=True)
    event = forms.CharField(max_length=500,
    widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Event Description'}))
    pswrd = forms.CharField(max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class PasswordForm(forms.Form):
    passwordf = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Password'}))


