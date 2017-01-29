from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name="userinfo")
    id_card = models.CharField(max_length=30,blank = True)
    title = models.CharField(max_length=30,blank = True)
    describe = models.CharField(max_length=200,blank = True)
    play_url = models.CharField(max_length=200,blank=True)
    websocket_url = models.CharField(max_length=200,blank=True)
    STATUSES = (
        (u'default', u'default'),
        (u'apply', u'apply'),
        (u'black', u'black'),
        (u'ok', u'ok'))
    status = models.CharField(max_length=10, choices=STATUSES,default = 'default')
    SWITCH = (
        (u'open', u'open'),
        (u'close', u'close'))
    switch = models.CharField(max_length=10, choices=SWITCH,default = 'close') 
    def __unicode__(self):
        return self.user.username