from django.db import models
from datetime import datetime
# Create your models here.
class User(models.Model):
	userid = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=70)
	fullname = models.CharField(max_length=140)
	Username = models.CharField(max_length=10)
	password = models.CharField(max_length=20)
	followers = models.IntegerField(default=0, null=True)
	following = models.IntegerField(default=0, null=True)
	
	

class Post(models.Model):
	postid = models.AutoField(primary_key=True)
	Createdthispost= models.ForeignKey(User, null=True)
	Userwhodidit= models.ForeignKey(User, related_name='Posts', null=True)
	postlink = models.CharField(max_length=140)
	title = models.CharField(max_length=140)
	likecounter = models.IntegerField(default=0, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	share = models.IntegerField(default=0, null=True)
	commentcounter= models.IntegerField(default=0, null=True)
	

class Comments(models.Model):
	commentid = models.AutoField(primary_key=True)
	useridcommenter = models.ForeignKey('User')
	postidcommentedon = models.ForeignKey('Post')
	commentlink = models.CharField(max_length=140)


def get_time_diff(self):
	if self.created_at:
		now = datetime.datetime.utcnow().replace(tzinfo=utc)
		timediff = now - self.created_at
		return timediff