from operator import imod
from re import search
from django.urls import path
from .views import *

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('details/<slug>',ProductDetailView.as_view(),name='details'),
    path('add_review',review,name='add_review'),
    path('category/<slug>',CategoryView.as_view(),name='category'),
    path('signup',signup,name='signup'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),

    ]