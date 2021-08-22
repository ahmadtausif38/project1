from django.db.models.query_utils import Q
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.views import View 
from django.contrib import messages
from home.models import product
from home.models import cart
from home.models import orderplaced
from home.models import customer
from home.models import contacts
# Create your views here.
def login(request):
    return render(request,'login.html')

def home(request):
    pro=product.objects.all()

    return render(request,'index.html',{'prod':pro})

def search(request):
    qur=request.GET.get('search').lower()
    #return HttpResponse(qur)
    #item=product.objects.filter(pro_name__icontains=qur)  
    item=[item for item in product.objects.all() if qur in item.pro_name.lower() or qur in item.pro_brand.lower() or qur in item.pro_category.lower()]
    
    return render(request,'search.html',{'items':item})

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        data=contacts(name=name,email=email,message=message)
        data.save()
        print("Data sbmitted")
        messages.success(request,"Your Message is Sucessfully submitted...")
        
    return render(request,'contact.html')
def helpandfeedback(request):
    return render(request,'helpandfeedback.html')

def add_to_cart(request):
    user=request.user
    #print(user)  this will show the user name who is currently login
    product_id=request.GET.get('prod_id')
    product1= product.objects.get(id=product_id)
    cart(user=user,product=product1).save()
    return redirect('/show_cart')

def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        
        cart1=cart.objects.filter(user=user)
        cart_pro=[p for p in cart.objects.all() if p.user == user]
        if cart_pro:
            price=0.0  
            delivery=50.0
            amt=999
            for i in cart_pro:           
                temp=i.qty * i.product.pro_price
                price=temp+price
                print(price)
            
            
            price2=price+delivery
            return render(request,'add_to_cart.html', {'amt':amt,'cart1':cart1,'price2':price2,'price':price,'delivery':delivery})
        else:
            return render(request,'empty_cart.html')
def gallery(request):
    pro=product.objects.all()

    return render(request,'gallery.html',{'prod':pro})
    #return render(request,'gallery.html')

class product_detail_view(View):
    def get(self,request,pk):
        pro=product.objects.all()
        prod=product.objects.get(pk=pk)
        return render(request,'product_details.html',{'product':prod,'pro':pro})


# def product_details(request):
#     pro=product.objects.all()
#     return render(request,'product_details.html',{'prod':pro})

                #Filter By Category
def mobile(request):
    pro=product.objects.filter( Q(pro_category='Mob')  )
    return render(request,'mobile.html',{'prod':pro})
    #return render(request,'mobile.html')

def earphone(request):
    pro=product.objects.filter( Q(pro_category='Ear')  )
    return render(request,'earphone.html',{'prod':pro})

def camera(request):
    pro=product.objects.filter( Q(pro_category='Cam')  )
    return render(request,'camera.html',{'prod':pro})

def laptop(request):
    pro=product.objects.filter( Q(pro_category='Lap')  )
    return render(request,'laptop.html',{'prod':pro})

                #Filter By Brand

def apple(request):
    pro=product.objects.filter( Q(pro_brand='Apple')  )
    return render(request,'apple.html',{'prod':pro})
def samsung(request):
    pro=product.objects.filter( Q(pro_brand='Samsung')  )
    return render(request,'samsung.html',{'prod':pro})
def mi(request):
    pro=product.objects.filter( Q(pro_brand='Mi')  )
    return render(request,'mi.html',{'prod':pro})

def realme(request):
    pro=product.objects.filter( Q(pro_brand='Realme')  )
    return render(request,'realme.html',{'prod':pro})
def sony(request):
    pro=product.objects.filter( Q(pro_brand='Sony')  )
    return render(request,'sony.html',{'prod':pro})