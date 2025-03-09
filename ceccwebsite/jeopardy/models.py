from django.db import models

class jeopardyboard(models.Model):

    game = models.CharField(max_length=100, default='default')

    jround = models.CharField(max_length=6, default='single')
    category = models.CharField(max_length=5, default='cat1')
    catname = models.CharField(max_length=100, default='???')
    dollar = models.CharField(max_length=4, default='200')

    answer = models.CharField(max_length=300, default='none')
    question = models.CharField(max_length=100, default='none')

    isactive = models.BooleanField(default=True)
    isdouble = models.BooleanField(default=False)

    def __str__(self):
        return '{}: {} {} {}'.format(self.game, self.category, self.dollar, self.catname)


class CategoryTitle(models.Model):

    game = models.CharField(max_length=100, default='default')

    jround = models.CharField(max_length=6, default='single')
    category = models.CharField(max_length=5, default='cat1')
    catname = models.CharField(max_length=100, default='???')

    def __str__(self):
        return '{}: {} {}'.format(self.game, self.category, self.catname)


class finaljeopardy(models.Model):

    game = models.CharField(max_length=100, default='default')

    catname = models.CharField(max_length=100, default='???')

    answer = models.CharField(max_length=300, default='none')
    question = models.CharField(max_length=100, default='none')

    def __str__(self):
        return '{}: {}'.format(self.game, self.catname)


class team(models.Model):

    teamno = models.IntegerField()

    teamname = models.CharField(max_length=100, default='none')

    points = models.IntegerField()

    ct = models.BooleanField(default=False)

    def __str__(self):
        return 'Team {} {}: {}'.format(self.teamno, self.teamname, self.points)


class game(models.Model):
    gname = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return 'Name: {}, Creator: {}, Created: {}, Modified: {}'.format(self.gname, self.creator, self.created, self.modified)



class wizard(models.Model):

    turn = models.IntegerField(default=1)


