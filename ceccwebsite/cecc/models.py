from django.db import models
from django.utils import timezone


class Comment(models.Model):
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.name, self.id)

class Ceccmenu(models.Model):

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

    season = models.CharField(
        max_length=4,
        choices=seasons,
        default='ASPR',
    )
    week = models.IntegerField(default=1)
    weekday = models.CharField(
        max_length=4,
        choices=weekdays,
        default='NOD',
    )
    breakfast = models.TextField(max_length=500)
    lunch = models.TextField(max_length=500)
    snack = models.TextField(max_length=500)

    def __str__(self):
        return '{}, Week: {}, Weekday: {}'.format(self.season, self.week, self.weekday)

class CeccEvent(models.Model):

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

    month = models.IntegerField(default=1)
    dayno = models.IntegerField(default=1)
    weekday = models.CharField(
        max_length=3,
        choices=weekdays,
        default='NOD',
    )
    event = models.TextField(max_length=500)

    def __str__(self):
        return 'Month: {}, Day: {}, Weekday: {}'.format(self.month, self.dayno, self.weekday)
