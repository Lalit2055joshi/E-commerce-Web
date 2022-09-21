from itertools import product
from django.shortcuts import render,redirect
from .models import *
from django.views.generic import View
import datetime
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



