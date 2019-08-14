from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm
# Create your views here.


def get_tickets(request):
    """
    This renders the index page and displays all tickets.
    """
    tickets = Ticket.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "index.html", {'tickets': tickets})

def full_ticket(request, pk):
    """
    This returns a single ticket based on the ticket ID and
    displays it in fullticket.html.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, "fullticket.html", {'ticket': ticket})


def upvote(request, pk):
    """
    This increments the upvotes on a ticket by one
    when a user clicks on the Upvote icon.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes += 1
    ticket.save()

    return render(request, "fullticket.html", {'ticket': ticket})


def create_or_edit_ticket(request, pk=None):
    """
    This Creates a new ticket or edits an existing ticket
    if the is a ticket ID.
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            return redirect(full_ticket, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticketform.html', {'form': form})    