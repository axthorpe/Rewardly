from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'accounts.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'dashboard/', 'accounts.views.dashboard', name='dashboard'),
    url(r'rewards/', 'accounts.views.rewards', name='rewards')
)
