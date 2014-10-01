from django.contrib import admin

# Register your models here.
from games.models import Game, Player

admin.site.register(Player)
admin.site.register(Game)