from django.conf.urls import url
from .views import full_ticket, upvote, create_or_edit_ticket



urlpatterns = [
    url(r'^(?P<pk>\d+)/$', full_ticket, name='full_ticket'),
    url(r'^upvote/(?P<pk>\d+)/$', upvote, name='upvote'),
    url(r'^new/$', create_or_edit_ticket, name='create_ticket'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_ticket, name='edit_ticket'),
]