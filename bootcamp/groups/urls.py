from django.conf.urls import url
#
from bootcamp.groups import views
#
app_name = 'groups'
urlpatterns = [
    url(r'^create/$', views.CreateGroupView.as_view(), name='create'),
    url(r'^$', views.GroupsListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\d+)/$', views.GroupsListView.as_view(), name='detail'),

]
