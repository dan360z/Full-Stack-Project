from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class TicketStatus(models.Model):
    """
    This is the ticket status choices
    """
    ticket_status = models.CharField(
        max_length=11,
        unique=True,
        choices=(("Open", "Open"),("Closed", "Closed")))
    class Meta:
        verbose_name = ("Ticket Status")
        verbose_name_plural = ("Ticket Status")

    def __str__(self):
        return self.ticket_status    


class Ticket(models.Model):
    """
    This is a ticket
    """
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    details = models.TextField()
    ticket_status = models.ForeignKey(TicketStatus, null=True)
    date_created = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    published_date = models.DateTimeField(blank=False, null=False, default=timezone.now)
    upvotes = models.IntegerField(default=0)

    def __str__(self):
        return "{0} Type: {1} Status: {2}".format(self.title, self.category, self.ticket_status)
