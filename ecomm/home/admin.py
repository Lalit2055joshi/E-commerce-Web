from itertools import product
from unicodedata import category
from django.contrib import admin
from .models  import *
# Register your models here.
admin.site.register(Categories)
admin.site.register(Subcategory)
admin.site.register(Slider)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Add)
admin.site.register(Review)
admin.site.register(Feedback)

