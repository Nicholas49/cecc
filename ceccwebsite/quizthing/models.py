from django.db import models
from django.utils import timezone

class answerset(models.Model):

    answer1 = models.CharField(max_length=100, default='NA')
    answer2 = models.CharField(max_length=100, default='NA')
    answer3 = models.CharField(max_length=100, default='NA')
    answer4 = models.CharField(max_length=100, default='NA')
    answer5 = models.CharField(max_length=100, default='NA')
    answer6 = models.CharField(max_length=100, default='NA')
    answer7 = models.CharField(max_length=100, default='NA')
    answer8 = models.CharField(max_length=100, default='NA')
    point1 = models.BooleanField(default=False)
    point2 = models.BooleanField(default=False)
    point3 = models.BooleanField(default=False)
    point4 = models.BooleanField(default=False)
    point5 = models.BooleanField(default=False)
    point6 = models.BooleanField(default=False)
    point7 = models.BooleanField(default=False)
    point8 = models.BooleanField(default=False)
    teamname = models.CharField(max_length=100, default='NA')
    roundno = models.IntegerField(default=1)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return 'Team: {}, Round: {}'.format(self.teamname, self.roundno)

class teamproxy(models.Model):

    teamname = models.CharField(max_length=100, default='NA')
    teamcolor = models.CharField(max_length=100, default='#888888')
    points = models.IntegerField(default=11)
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return 'Team {}'.format(self.teamname)
