from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User
 
 
class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	fbid = models.IntegerField()

 
def __unicode__(self):
	return self.user.get_full_name()
 
 
#===========================================================================
# SIGNALS
#===========================================================================
def signals_import():

	from tastypie.models import create_api_key
	 
	models.signals.post_save.connect(create_api_key, sender=User)
	 
signals_import()