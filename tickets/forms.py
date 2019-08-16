from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'email', 'details', 'ticket_status')

class MakePaymentForm(forms.Form):
   
    donation = forms.IntegerField(label="Donation Amount", required=False, min_value=5, max_value=999, widget=forms.NumberInput(attrs={'placeholder': 'Minimum donation: £5'}))
    credit_card_number = forms.CharField(label='Credit card number', required=False, widget=forms.TextInput(attrs={'placeholder': '**** **** **** ****'}))
    card_expiry = forms.CharField(label='Expiry Date (MM/YYYY)', required=False, widget=forms.TextInput(attrs={'placeholder': 'MM/YYYY'}))
    cvv = forms.CharField(label='Security code (CVV)', required=False, widget=forms.TextInput(attrs={'placeholder': 'CVV'}))
    stripe_id = forms.CharField(widget=forms.HiddenInput)        
