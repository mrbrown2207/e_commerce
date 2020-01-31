from django.contrib import admin
from .models import Order, OrderLineItem


# Register your models here.
class OrderLineAdminInLine(admin.TabularInline):
    model = OrderLineItem


"""
The admin interface has the ability to edit more than one model
on a single page. This is known as inlines.
"""


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInLine, )


admin.site.register(Order, OrderAdmin)
