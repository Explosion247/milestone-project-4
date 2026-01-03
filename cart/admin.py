from django.contrib import admin
from .models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date', 'grand_total')

    fields = ('order_number',
              'date',
              'first_name',
              'last_name',
              'email',
              'phone_number',
              'grand_total'
              )

    list_display = ('order_number',
                    'date',
                    'first_name',
                    'last_name',
                    'grand_total'
                    )
    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)