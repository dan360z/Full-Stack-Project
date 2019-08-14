from django.conf.urls import url
from tickets.views import full_ticket



urlpatterns = [
    url(r'^(?P<pk>\d+)/$', full_ticket, name='full_ticket'),
]