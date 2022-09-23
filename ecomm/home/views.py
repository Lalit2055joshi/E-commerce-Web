from itertools import product
from pickle import NONE
from pyexpat.errors import messages
from django.shortcuts import render , redirect
from .models import *
from django.views.generic import View
import datetime
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.

class Base(View):
    views = {}
    views['categories'] = Categories.objects.all()
    views['brands'] = Brand.objects.all()
    
    

class HomeView(Base):
    def get(self,request):
        self.views
        self.views['subcategories'] = Subcategory.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads'] = Add.objects.all()
        self.views['hots'] = Product.objects.filter(labels = 'hot')
        self.views['sale'] = Product.objects.filter(labels = 'sale')
        self.views['news'] = Product.objects.filter(labels = 'new')
        self.views['feedback']= Feedback.objects.all()

        return render(request,'index.html',self.views)

class ProductDetailView(Base):
    def get(self,request,slug):
        self.views
        self.views['details'] = Product.objects.filter(slug = slug )
        self.views['reviews'] = Review.objects.filter(slug = slug )
        subcat = Product.objects.get(slug = slug).subcategory

        self.views['subcat_product']=Product.objects.filter(subcategory = subcat)
        
        return render(request,'product-detail.html',self.views)

def review(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        review=request.POST['review']
        slug = request.POST['slug']
        x = datetime.datetime.now()
        date= x.strftime("%c")
        
        data = Review.objects.create(
            name =name,
            email=email,
            review=review,
            date = date,
            slug = slug,
        )
        data.save()

        return redirect(f'/details/{slug}')

class CategoryView(Base):
    def get(self,request,slug):
        self.views
        cat_id = Categories.objects.get(slug = slug).id
        self.views['cat_product'] = Product.objects.filter(category_id = cat_id)
        return render(request,'product-list.html',self.views)        

class SearchView(Base):
    def get(self,request):
        self.views
        if request.method =="GET":
            query=request.GET['query']
            self.views['search_product']= Product.objects.filter(name__icontains = query)
            self.views['search_for']=query
        return render(request,'search.html',self.views)        

def signup(request):
    if request.method == 'POST':
        f_name = request.POST['first_name']
        l_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request,'the username is already taken')
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                 messages.error(request,'the username is already taken')
                 return redirect('/signup')
            else:
                data = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name =f_name,
                    last_name = l_name
                )
                data.save()
                return redirect('/')

        else:
            messages.error(request,'password does not match')    
    return render(request,'signup.html')

from django.contrib.auth import login , logout

def login(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username , password = password )
        if user is not NONE:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'The User Name Or Password does not match')
            return redirect('/login')    
    return render(request,'login.html')         

def logout(request):
    auth.logout(request)
    return redirect('/')

def add_to_cart(request,slug):
    username=request.user.username
    if Cart.objects.filter(slug = slug,username= username,checkout = False).exists():
        
