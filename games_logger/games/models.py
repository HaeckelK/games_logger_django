from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description_short = models.CharField(max_length=50, blank=False)
    description_long = models.CharField(max_length=250, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)


class TimeCategory(Category):
    pass


class GenreCategory(Category):
    pass


class PlatformCategory(Category):
    pass


class Game(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    genre = models.ForeignKey(GenreCategory, on_delete=models.CASCADE, blank=False)
    time = models.ForeignKey(TimeCategory, on_delete=models.CASCADE, blank=False)
    platform = models.ForeignKey(PlatformCategory, on_delete=models.CASCADE, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    players_min = models.IntegerField(blank=False)
    players_min = models.IntegerField(blank=False)
    expands = models.ForeignKey('Game',null=True,blank=True, on_delete=models.CASCADE)


class Match(models.Model):
    players = models.ManyToManyField("Player", related_name="players")
    winners = models.ManyToManyField("Player", related_name="winners")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, blank=False)
    comments = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

