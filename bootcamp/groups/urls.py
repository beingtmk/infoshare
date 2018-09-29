from django.conf.urls import url
#
from bootcamp.groups import views
#
app_name = 'groups'
urlpatterns = [
    url(r'^create/$', views.CreateGroupView.as_view(), name='create'),
    url(r'^$', views.GroupsListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\d+)/$', views.GroupDetailView.as_view(), name='detail'),
    url(r'^request_membership/(?P<pk>\d+)/$', views.request_membership, name='request_membership'),
    url(r'^request_handler/(?P<pk>\d+)/$', views.request_handler, name='request_handler'),

]
