from django.contrib import admin
from .models import Ticket, TicketStatus, Category

# Register your models here.
admin.site.register(TicketStatus)
admin.site.register(Category)
admin.site.register(Ticket)