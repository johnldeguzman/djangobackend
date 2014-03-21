from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie import fields
from models import *
from tastypie.authorization import Authorization

class UserResource(ModelResource):
	Posts = fields.ToManyField('api.resources.PostResources', 'Posts', full=True, null=True)
	class Meta:
		queryset = User.objects.all()
		resource_name='User'
		excludes =['password', 'email']
	
	
class UserResources(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name='User'
		excludes =['password', 'email','followers','following', 'userid']

class PostResource(ModelResource):
	
	Userwhodidit = fields.ForeignKey(UserResources,'Userwhodidit', full=True)

	class Meta:
		queryset = Post.objects.all()
		authorization= Authorization()
		resource_name='Post'
		allowed_methods = ['get', 'put', 'delete', 'post']
		ordering = ['created_at',]


class PostResources(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        excludes = ['Userwhodidit']

