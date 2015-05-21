from django.conf.urls.defaults import *
from accounts import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', views.login, name='login'),
)
