from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm, MakePaymentForm
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET


def get_tickets(request):
    """
    This renders the index page and displays all tickets.
    """       
    tickets = Ticket.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, "index.html", {'tickets': tickets})


def full_ticket(request, pk):
    """
    This returns a single ticket based on the ticket ID and
    displays it in fullticket.html. A ticket is only editable
    if the current user's email matches the email of the user 
    who created the ticket.
    """
    if request.user.is_authenticated: 
        user = User.objects.get(email=request.user.email)
    else: user = ''

    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, "fullticket.html", {'ticket': ticket}, {'user': user})


@login_required
def upvote(request, pk):
    """
    This increments the upvotes on a ticket by one
    when a user clicks on the Upvote icon.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.upvotes += 1
    voted = True
    ticket.save()

    return render(request, "fullticket.html", {'ticket': ticket, 'voted': voted})


@login_required
def create_or_edit_ticket(request, pk=None):
    """
    This Creates a new bug ticket or edits an existing ticket
    if the is a ticket ID.
    """
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            messages.success(request, "Your ticket has been saved!")
            return redirect(full_ticket, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticketform.html', {'form': form}) 


@login_required
def create_feature_ticket(request):
    """
    This renders a ticket form and a payment form.
    If both forms are valid and a payment is succsessful
    a feature ticket is created.
    """

    if request.method == "POST":

        ticket_form = TicketForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if ticket_form.is_valid() and payment_form.is_valid():

            donation = 0
            donation += int(request.POST.get("donation"))

            try:
                customer = stripe.Charge.create(
                    amount = int(donation * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                #If the payment was successful the ticket is saved.
                ticket_form.instance.category_id = 4
                ticket = ticket_form.save()
                messages.success(request, "Thank you for your donation, your ticket has been saved!")
                return redirect(full_ticket, ticket.pk)            
            else:
                messages.error(request, "Unable to take payment")

        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")                
        
    else:
        ticket_form = TicketForm()
        payment_form = MakePaymentForm()
    
    return render(request, 'featureticketform.html', {'form': ticket_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE})


@login_required
def delete_ticket(request, pk):
    """
    This deletes a ticket.
    """
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.delete()
    messages.success(request, "Your ticket has been deleted!")
    return redirect(get_tickets)    