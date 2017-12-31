from django.conf.urls import url, include
from users.views import User, user_login

urlpatterns = [
    url(r'^$', User.as_view()),
    url(r'^login/$', user_login)
]