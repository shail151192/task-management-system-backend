from django.conf.urls import url
from views import *


urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', TaskDetailView.as_view()),
    url(r'^$', TaskListView.as_view())
]

