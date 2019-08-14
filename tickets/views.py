from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Ticket
# Create your views here.


def get_tickets(request):
    """This renders the index page and displays all tickets"""

    tickets = Ticket.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "index.html", {'tickets': tickets})

def full_ticket(request, pk):
    """
    This returns a single ticket based on the ticket ID and
    displays it in fullticket.html
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.save()

    return render(request, "fullticket.html", {'ticket': ticket})    
