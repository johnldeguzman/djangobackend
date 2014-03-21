from django.conf.urls import patterns, include, url
from api.resources import UserResource, PostResource, PostResources
from django.contrib import admin
from tastypie.api import Api
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PostResource())
v1_api.register(PostResources())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mimicproduction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include (v1_api.urls)),
  
) 

