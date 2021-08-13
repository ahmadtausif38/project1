from django.contrib import admin
from.models import product
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
    

admin.site.register(product,Admin_view)
admin.site.register(contacts,Admin_view1)