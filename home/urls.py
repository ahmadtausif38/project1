from django.urls import path
from home import views

urlpatterns=[
    path('',views.login,name='login'),
    #cart
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('show_cart',views.show_cart,name='show_cart'),
    path('plus_item',views.plus_item),
    path('minus_item',views.minus_item),

    path('index',views.home,name='home'),
    path('search',views.search,name='search'),
    
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('helpandfeedback',views.helpandfeedback,name='helpandfeedback'),
    path('gallery',views.gallery,name='gallery'),

    # path('product_details',views.product_details,name='product_details'), 
     path('product_details/<int:pk>',views.product_detail_view.as_view(),name='product_details'),
      
   #Filter By Category
     path('mobile',views.mobile,name='mobile'),
     path('camera',views.camera,name='camera'),
     path('laptop',views.laptop,name='laptop'),
     path('earphone',views.earphone,name='earphone'),

     #Filter By Brand
     path('apple',views.apple,name='apple'),
     path('samsung',views.samsung,name='samsung'),
     path('sony',views.sony,name='sony'),
     path('mi',views.mi,name='mi'),
     path('realme',views.realme,name='realme'),



]