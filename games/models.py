from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=30)
    player = models.ForeignKey(Player, related_name="games")
    score = models.IntegerField(default=0, null=True, blank=True)

    def __unicode__(self):
        return self.name