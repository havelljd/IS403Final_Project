from django.db import models
from datetime import datetime

# Create your models here.
class user (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)

    def __str__(self):
        return(self.first_name + ' ' + self.last_name)

class home_team (models.Model):
    home_team_name = models.CharField(max_length = 30)
    nickname = models.CharField(max_length=30)

    def __str__(self):
        return(self.home_team_name)
class away_team (models.Model):
    away_team_name = models.CharField(max_length = 30)
    nickname = models.CharField(max_length=30)

    def __str__(self):
        return(self.away_team_name)

class game (models.Model):
    Home_Team=models.ForeignKey(home_team, on_delete=models.DO_NOTHING)
    Away_Team=models.ForeignKey(away_team, on_delete=models.DO_NOTHING)
    date_played = models.DateField(default=datetime.today, blank = True)
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)



    def __str__(self):
        return('Game id ' + str(self.id) )
class bet (models.Model):
    user_id = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    game_id = models.ForeignKey(game, on_delete=models.DO_NOTHING)
    user_team_pick = models.ForeignKey(home_team, on_delete=models.DO_NOTHING)

    def __str__(self):
        return('Game ID: ' + str(self.game_id) + ' User ID ' + str(self.user_id) + ' Picked Team ' + str(self.user_team_pick))

# The user will input first, last, middle names

# User will pick their home (who they think will win) and away team, the date the game was played, and the scores for both teams

#User will then create their bet by selecting the game, and then the team they think will win. (maybe they decide if they got it right or not)

#Users can insert a team as well



