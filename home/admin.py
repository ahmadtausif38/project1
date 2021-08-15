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

class Admin_view1(admin.ModelAdmin):
    list_display=('name','email','message')
    list_editable=('message',)
    list_per_page=10

class Admin_view2(admin.ModelAdmin):
    list_display=('id','user','product','qty')
    
class Admin_view3(admin.ModelAdmin):
    list_display=('id','user','customer','product','qty','order_date')

class Admin_view4(admin.ModelAdmin):
    list_display=('id','user','name')

admin.site.register(product,Admin_view)

admin.site.register(contacts,Admin_view1)

admin.site.register(cart,Admin_view2)

admin.site.register(orderplaced,Admin_view3)

admin.site.register(customer,Admin_view4)