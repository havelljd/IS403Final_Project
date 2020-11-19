from django.db import models

# Create your models here.
class user (models.Model):
    first_name = models.CharField(max_length=30),
    last_name = models.CharField(max_length=30)

class team (models.Model):
    team_name = models.CharField(max_length = 30)

class game (models.Model):
    date_played = models.DateField,
    home_team = models.ForeignKey(team, on_delete=models.DO_NOTHING),
    home_team_score = models.IntegerField,
    away_team = models.ForeignKey(team, on_delete=models.DO_NOTHING),
    away_team_score = models.IntegerField
class bet (models.Model):
    user_id = models.ForeignKey(user, on_delete=models.DO_NOTHING),
    game_id = models.ForeignKey(game, on_delete=models.DO_NOTHING),
    user_team_pick = models.ForeignKey(team, on_delete=models.DO_NOTHING),