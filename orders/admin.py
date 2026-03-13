from django.contrib import admin
from orders.models import Order,OrderedItem

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display=['owner',
                  'order_status',
    ]# to display the id, owner, order status, total price, delete status and created at fields of the order model in the admin panel when we click on the orders model in the admin panel of the application
    search_fields=('owner',
                   "id",
    )# to add a search bar in the admin panel of the orders model, so that we can search for the orders based on the username of the owner of the order in the admin panel of the application

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderedItem)