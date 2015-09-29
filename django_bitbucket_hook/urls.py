from django.conf.urls import patterns, url
from django_bitbucket_hook import views

urlpatterns = patterns(
    '',
    url(r'^$', views.only_hook),
    url(r'^(?P<name>[\w-]+)$', views.hook_name),
    url(r'^(?P<name>[\w-]+)/(?P<branch>[\w-]+)$', views.hook_name_branch),
)
