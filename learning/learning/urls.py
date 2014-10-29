# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from geography import views




from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^questions/$', views.QuestionBase.as_view()),
    url(r'^questions/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
    url(r'^play/$', views.PlayBase.as_view()),
    url(r'^user/$', views.UserView.as_view()),
    url(r'^user/(?P<pk>[^\/]+)/$', views.UserDetailedView.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)
