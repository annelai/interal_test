from django.conf.urls import patterns, include, url
from django.contrib import admin
from words.views import show_word
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', show_word),
)
