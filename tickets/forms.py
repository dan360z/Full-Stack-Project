from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'category', 'details', 'ticket_status', 'published_date',)