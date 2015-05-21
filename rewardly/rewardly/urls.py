from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'accounts.views.dashboard', name='dashboard'),
    url(r'^accounts/', include('accounts.urls')),
]
