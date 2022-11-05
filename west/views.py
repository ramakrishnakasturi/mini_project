from ast import Sub
                    #Step-5
from django.http import HttpResponse
                    #
from django.shortcuts import render, redirect
from .models import Item
from django.views import View
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,auth
# Create your views here.

            #Step-26

data1=list()

def amatra(request):
    return render(request, 'amatra.html')

def home(request):
    return render(request, 'home.html')

def cart(request):
    data2=list()
    for i in data1:
        y=Item.objects.get(id=i)
        data2.append(
            {
                'img':y.img,
                'name':y.name,
                'price':y.price,
                'id':y.id,
                'discount':y.discount,
            }
        )
    return render(request,"cart.html",{'data2':data2})


def pay(request):
    

    sum=0
    sub=0
    for i in data1:
        y=Item.objects.get(id=i)
        sum = sum + y.price 
        sub = sub + y.discount

    if request.method == 'POST':
        client = razorpay.Client(auth=("rzp_test_18tCbiFWWxyIJ2", "9jd82P4ZiQ5y5DwZLm6QnOp3"))
        DATA = {"amount": sum-sub,"currency": "INR","payment_capture":"1"}
        payment = client.order.create(data=DATA)  
    
    return render(request, 'pay.html',{'sum':sum,'sub':sub,'amount':(sum-sub)*100,'amount1':sum-sub})


def payment(request):

    total = int(request.POST.get('total'))
    sub = int(request.POST.get('sub'))
    total = total-sub


    return render(request,'payment.html',{'total':total})    


def products_child(request):
    return render(request, 'products_child.html')

def products_men(request):
    return render(request, 'products_men.html')

def products_women(request):
    return render(request, 'products_women.html')

def signin(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        user = User.objects.all()
        user=auth.authenticate(username=username,password=password)
        if(user is not None):
            #print(username)
            auth.login(request,user)
            global current_user
            current_user=username
            return render(request,"home.html",{'username':username})
        else:
            return render(request,"signin.html",{'message':'Invalid Credentials'})
    else:
        return render(request,"signin.html")

def signup(request):
    if(request.method=="POST"):
        username=request.POST['username']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if(password1==password2):
            user=User.objects.create_user(username=username,email=email,password=password1,last_name=last_name)
            user.save()
            return render(request,'signin.html')
        else:
            return render(request,'signup.html',{'message':'Passwords not matching'})
    else:
        return render(request,'signup.html')

def signout(request):
    auth.logout(request)
    return render(request,'home.html')

class w_handbags(View):

    def post(self,request):
        
        product = request.POST.get('product')
        data1.append(product)
        data2=list()
        for i in data1:
            y=Item.objects.get(id=i)
            data2.append(
                {
                    'img':y.img,
                    'name':y.name,
                    'price':y.price,
                    'id':y.id,
                    'dis':y.discount,
                }
            )
        
        print(data1)
        return render(request,"cart.html",{'data2':data2})


    def get(self,request):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Handbags"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                        'dis':i.discount,
                    }
               ) 
            print(i.discount)
        return render(request,"w_handbags.html",{'data':data})

    
class w_footwear(View):
    def post(self,request):
        
        product = request.POST.get('product')
        data1.append(product)
        data2=list()
        for i in data1:
            y=Item.objects.get(id=i)
            data2.append(
                {
                    'img':y.img,
                    'name':y.name,
                    'price':y.price,
                    'id':y.id,
                    'dis':y.discount,
                }
            )
        
        print(data1)
        return render(request,"cart.html",{'data2':data2})

    def get(self,request):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Footwear"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                        'dis':i.discount,
                    }
               ) 
        return render(request,"w_footwear.html",{'data':data})

class w_jewel(View):

    def post(self,request):
        
        product = request.POST.get('product')
        data1.append(product)
        data2=list()
        for i in data1:
            y=Item.objects.get(id=i)
            data2.append(
                {
                    'img':y.img,
                    'name':y.name,
                    'price':y.price,
                    'id':y.id,
                    'dis':y.discount,
                }
            )
        
        print(data1)
        return render(request,"cart.html",{'data2':data2})
    
    def get(self,request):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Jewelery"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                        'dis':i.discount,
                    }
                )    
        return render(request,"w_jewel.html",{'data':data})

class m_shirt(View):
    def post(self,request):
        
        product = request.POST.get('product')
        data1.append(product)
        data2=list()
        for i in data1:
            y=Item.objects.get(id=i)
            data2.append(
                {
                    'img':y.img,
                    'name':y.name,
                    'price':y.price,
                    'id':y.id,
                    'dis':y.discount,
                }
            )
        
        print(data1)
        return render(request,"cart.html",{'data2':data2})

    def get(self,request):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Tshirts"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                        'dis':i.discount,
                    }
                ) 
        return render(request,"m_shirt.html",{'data':data})


class m_watch(View):
    def post(self,request):
        
        product = request.POST.get('product')
        data1.append(product)
        data2=list()
        for i in data1:
            y=Item.objects.get(id=i)
            data2.append(
                {
                    'img':y.img,
                    'name':y.name,
                    'price':y.price,
                    'id':y.id,
                    'dis':y.discount,
                }
            )
        
        print(data1)
        return render(request,"cart.html",{'data2':data2})

    def get(self,request):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Watches"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                        'dis':i.discount,
                    }
                ) 
        return render(request,"m_watch.html",{'data':data})


class m_shades(View):
    def post(self,request):
        
        product = request.POST.get('product')
        data1.append(product)
        data2=list()
        for i in data1:
            y=Item.objects.get(id=i)
            data2.append(
                {
                    'img':y.img,
                    'name':y.name,
                    'price':y.price,
                    'id':y.id,
                    'dis':y.discount,
                }
            )
        
        print(data1)
        return render(request,"cart.html",{'data2':data2})

    def get(self,request):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Shades"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                        'dis':i.discount,
                    }
                ) 
        return render(request,"m_shades.html",{'data':data})


def wishlist(request):
    return render(request, 'wishlist.html')

def search(request):
    s = request.POST['search']
    s = s.lower()
    print(s)
    if(s=="handbags"or s=="handbag"or s=="hand bag"):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Handbags"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                        'dis':i.discount,
                    }
               ) 
        return render(request,"w_handbags.html",{'data':data})
    
    elif(s=="footwear" or s=="shoes" or s=="heels" or s=="sandals"):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Footwear"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                    }
               ) 
        return render(request,"w_footwear.html",{'data':data})

    elif(s=="jewellery" or s=="accessories"):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Jewelery"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                    }
                )    
        return render(request,"w_jewel.html",{'data':data})

    elif(s=="shirts" or s=="shirt" or s=="tshirts" or s=="t-shirts" or s=="t shirts"):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Tshirts"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                    }
                ) 
        return render(request,"m_shirt.html",{'data':data})

    elif(s=="watch" or s=="watches"):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Watches"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                    }
                ) 
        return render(request,"m_watch.html",{'data':data})

    elif(s=="shades" or s=="sunglasses"):
        x=Item.objects.all()
        data=list()
        for i in x:
            if(i.category=="Shades"):
                data.append(
                    {
                        'img':i.img,
                        'name':i.name,
                        'price':i.price,
                        'id':i.id,
                    }
                ) 
        return render(request,"m_shades.html",{'data':data})

    return render(request, "home.html")    
                        #

    