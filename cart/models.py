import uuid

from django.db import models

from events.models import Ticket

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(
        max_length=32, null=False, editable=False
        )
    first_name = models.CharField(
        max_length=50, null=False, blank=False
        )
    last_name = models.CharField(
        max_length=50, null=False, blank=False
        )
    email = models.EmailField(
        max_length=254, null=False, blank=False
        )
    phone_number = models.CharField(
        max_length=20, null=False, blank=False
        )
    date = models.DateTimeField(
        auto_now_add=True
        )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
        )

    def _generate_order_number(self):

        return uuid.uuid4().hex.upper()

    def update_total():
        order_total = Ticket.amount * Ticket.price
        return order_total

    def save(self, *args, **kwargs):

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
