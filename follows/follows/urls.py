from django.conf.urls import patterns, include, url
from apis.resources import CreateUserResource, UserResource, SearchResource
from django.contrib import admin
from tastypie.api import Api
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(CreateUserResource())
v1_api.register(UserResource())
v1_api.register(SearchResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'follows.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include (v1_api.urls)),

)
