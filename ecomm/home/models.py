from pickle import TRUE
from tkinter import CASCADE
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=200)
    slug = models.TextField(unique=TRUE)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Categories,on_delete= models.CASCADE)
    icon = models.CharField(max_length=200,blank=TRUE)
    slug = models.TextField(unique=TRUE)

    def __str__(self):
        return self.name
STATUS = (('active','Active'),('','Default'))
class Slider(models.Model):
    name=models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')  
    text = models.TextField(blank=TRUE)
    rank = models.IntegerField()
    status = models.CharField(max_length=100,choices=STATUS , blank= True)

    def __str__(self):
        return self.name

class Add(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    text=models.TextField(blank=True)
    rank=models.IntegerField() 

    def __str__(self):
        return self.name

class Brand(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    rank = models.IntegerField()

    def __str__(self):
        return self.name

LABELS=(('new','New'),('hot','Hot'),('sale','Sale'),('','default'))
STOCK=(('In Stock','In Stock'),('Out of Stock','Out of Stock'))
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    discounted_price=models.IntegerField(default=0)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    #brand = models.ForeignKey(Brand,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='media')
    descriptions=models.TextField(blank=True)
    specification=models.TextField(blank=True)
    slug=models.TextField(unique=True)
    labels = models.CharField(max_length=100,choices=LABELS)
    stock = models.CharField(max_length=100,choices=STOCK)

    def __str__(self):
        return self.name

class Review(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    review = models.TextField(blank=True)
    date=models.CharField(max_length=100)
    slug=models.TextField()
    #point = models.IntegerField(default = 1)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'media')
    profession= models.CharField(max_length=100)
    comment=models.TextField()
    rating = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cart(models.Model):
    username=models.CharField(max_length=300)
    slug =models.TextField(max_length=500)
    quantity=models.IntegerField(default = 1)
    total = models.FloatField()
    checkout = models.BooleanField(default = False)
    items = models.ForeignKey(Product ,on_delete=models.CASCADE)
    
    def str(self):
        return self.username
        





