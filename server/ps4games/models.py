from django.db import models

class PS4Game(models.Model):
    name = models.CharField(max_length=60, default="")
    release = models.IntegerField(default=0)
    metacritic = models.IntegerField(default=0)
    gptime = models.IntegerField(default=0)
    #eshkali nadarad filde bad ersal nashavad
    #eshkal nadarad fild bad khali ersal shavad
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
