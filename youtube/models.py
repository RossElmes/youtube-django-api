from django.db import models
import re

# Create your models here.

class MatchDetail(models.Model):

    TEAM_CHOICES = [
        ('Team1', 'Team1'),
        ('Team2', 'Team2'),
    ]

    RESULT_CHOICES = [
        ('Team1', 'Team1'),
        ('Team2', 'Team2'),
        ('Draw', 'Draw')
    ]

    date_of_match = models.DateField()
    venue = models.CharField(max_length=255)
    team1 = models.CharField(max_length=100)
    team2 = models.CharField(max_length=100)
    home_team = models.CharField(max_length=5, choices=TEAM_CHOICES)
    team1_score = models.IntegerField()
    team2_score = models.IntegerField()
    result = models.CharField(max_length=5, choices=TEAM_CHOICES)
    youtube_link = models.CharField(max_length=255)
    video_id = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.team1} vs {self.team2} on {self.date_of_match}"
    

class MatchClip(models.Model):
    match = models.ForeignKey(MatchDetail, related_name='match',on_delete=models.CASCADE)
    start_time = models.DecimalField(max_digits=5, decimal_places=2)
    end_time = models.DecimalField(max_digits=5, decimal_places=2)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} at {self.start_time}"
    
class Playlist(models.Model):
    name = models.CharField(max_length=225)
    
    def __str__(self):
        return f"{self.name}"


class PlaylistClips(models.Model):
    clip_id = models.ForeignKey(MatchClip, related_name='clips', on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, related_name='playlists', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.playlist} at {self.clip}"
    
class Codes(models.Model):
    code = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.code}"