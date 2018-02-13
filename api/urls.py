from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from education_mgmt import settings
from api.views import *
from rest_framework.authtoken import views as tokenView

urlpatterns = patterns('',
    url(r'^login/', tokenView.obtain_auth_token),
    url(r'^register/$', user_registration, name='user_registration'),

    url(r'^school/add/$', school_create, name='school-create'),
    url(r'^school/list/$', school_list, name='school-list'),
    url(r'^school/details/(?P<pk>[0-9]+)/$', school_details, name='school-detail'),
    url(r'^school/update/(?P<pk>[0-9]+)/$', school_update, name='school-update'),
    url(r'^school/delete/(?P<pk>[0-9]+)/$', school_delete, name='schoolt-delete'),

    url(r'^university/list1/$', university_list1, name='university_list1'),
    url(r'^university/list2/$', university_list2, name='university_list2'),
    url(r'^university/delete/(?P<pk>[0-9]+)/$', university_delete, name='university_delete'),
    url(r'^university/add/$', add_university, name='add-university'),

    url(r'^student/add/$', student_create, name='student-create'),


)
