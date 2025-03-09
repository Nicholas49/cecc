from django.db import models
from django.utils import timezone
from oscarsapp.data import noms

class Wizard(models.Model):
    active = models.BooleanField(default=False)
    lauer_hash = models.CharField(max_length=100, default='')
    umsl_hash = models.CharField(max_length=100, default='')

class Nominee(models.Model):

    name = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='poster')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):

    name = models.CharField(max_length=100, default='')
    shortname = models.CharField(max_length=100, default='')
    points = models.IntegerField(default=1)
    order = models.IntegerField(default=0)
    winner = models.ForeignKey(
        'Nomination',
        related_name='winner',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Nomination(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE, null=True)
    subtitle = models.CharField(
        max_length=100,
        default='',
        null=True,
        blank=True
    )
    url = models.CharField(max_length=100, default='', null=True, blank=True)

    def __str__(self):
        return f'{self.category.name} - {self.nominee.name}'


class Ballot(models.Model):

    user = models.CharField(max_length=100, default='NA')
    name = models.CharField(max_length=100, default='NA')
    game = models.CharField(max_length=100, default="Lauer")
    skore = models.IntegerField(default=0)
    place = models.IntegerField(default=1)
    vwidth = models.IntegerField(default=0)
    kulr = models.CharField(max_length=20, default='#fc0')
    hidden = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Name: {}, ID: {}'.format(self.name, self.id)


class Pick(models.Model):

    ballot = models.ForeignKey(Ballot, on_delete=models.CASCADE, null=True)
    nomination = models.ForeignKey(Nomination, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.ballot} - {self.nomination}'

