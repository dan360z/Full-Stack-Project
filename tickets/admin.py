from django.contrib import admin
from .models import Ticket, TicketStatus

# Register your models here.
admin.site.register(Ticket)
admin.site.register(TicketStatus)