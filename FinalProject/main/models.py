from django.db import models
from datetime import datetime

# Create your models here.


class game (models.Model):
    Home_Team=models.CharField(max_length = 30)
    Away_Team=models.CharField(max_length = 30)
    date_played = models.DateField(default=datetime.today, blank = True)
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)



    def __str__(self):
        return('Game id ' + str(self.id) )

# The user will input first, last, middle names

# User will pick their home (who they think will win) and away team, the date the game was played, and the scores for both teams

#User will then create their bet by selecting the game, and then the team they think will win. (maybe they decide if they got it right or not)

#Users can insert a team as well



