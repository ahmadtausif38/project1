from django.contrib import admin
from.models import product,orderplaced,cart,customer
from.models import contacts
# Register your models here.


class Admin_view(admin.ModelAdmin):
    list_display=('pro_name','pro_brand','pro_category','pro_price','pro_desc','pro_img')
    list_editable=('pro_price','pro_desc')
    list_per_page=10
    search_fields=('pro_name',)
    list_filter=('pro_category',)

class Contact_view(admin.ModelAdmin):
    list_display=('name','email','message')
    list_editable=('message',)
    list_per_page=10

class Cart_view(admin.ModelAdmin):
    list_display=('id','user','product','qty')
    list_per_page=10
    
class order_view(admin.ModelAdmin):
    list_display=('id','user','customer','product','qty','order_date')
    list_per_page=10

class customer_view(admin.ModelAdmin):
    list_display=('id','user','name')
    list_per_page=10

admin.site.register(product,Admin_view)

admin.site.register(contacts,Contact_view)

admin.site.register(cart,Cart_view)

admin.site.register(orderplaced,order_view)

admin.site.register(customer,customer_view)