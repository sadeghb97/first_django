from django.db import models


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now=True) --> tarikh khodkar sabt mishe


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ('album', 'order')

    def __unicode__(self):
        return '%d: %s' % (self.order, self.title)
