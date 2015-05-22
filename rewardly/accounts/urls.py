from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('accounts.views',
    url(r'^$', 'home', name='home'),
    url(r'^login/$', 'login', name='login'),
    url(r'^register/$', 'register', name='register'),
    url(r'^dashboard/', 'dashboard', name='dashboard'),
    url(r'^rewards/', 'rewards', name='rewards'),
    url(r'get_all_data/', 'get_all_data', name='get_all_data'),
)
