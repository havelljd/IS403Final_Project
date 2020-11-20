from django.contrib import admin
from .models import bet, game, home_team, away_team, user
# Register your models here.

admin.site.register(bet)
admin.site.register(game)
admin.site.register(home_team)
admin.site.register(away_team)
admin.site.register(user)