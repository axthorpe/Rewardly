from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('accounts.views',
    url(r'^$', 'dashboard', name='dashboard'),
    url(r'^login/$', 'login', name='login'),
    url(r'^register/$', 'register', name='register'),
)
