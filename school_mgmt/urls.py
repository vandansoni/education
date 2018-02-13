from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from education_mgmt import settings
from school_mgmt.views import blog_home_page

urlpatterns = patterns('',
    url(r'^$', school_mgmt_home_page, name='school_mgmt-home'),
)