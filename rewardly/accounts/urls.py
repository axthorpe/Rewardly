from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('accounts.views',
    (r'^$', 'dashboard', name='dashboard'),
    (r'^login/$', 'login', name='login'),
    (r'^register/$', 'register', name='register'),
)
