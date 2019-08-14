from django.conf.urls import url
from tickets.views import full_ticket, upvote



urlpatterns = [
    url(r'^(?P<pk>\d+)/$', full_ticket, name='full_ticket'),
    url(r'^upvote/(?P<pk>\d+)/$', upvote, name='upvote'),
]