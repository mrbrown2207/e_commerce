from django.contrib import admin
from .models import Product


# Putting things here allows us to do this from the admin panel!! :-)
# Register your models here.
admin.site.register(Product)
