from django.contrib import admin
from django.urls import path
from . import views
            #Step-15
urlpatterns = [
    path('',views.amatra),
    path('search',views.search),
    path('home', views.home),
    path('cart', views.cart),
    path('pay', views.pay),
    path('payment', views.payment),
    path('products_child', views.products_child),
    path('products_men', views.products_men),
    path('products_women', views.products_women),
    path('signin', views.signin),
    path('signup', views.signup),
    path('signout', views.signout,name='signout'),
    path('w_handbags', views.w_handbags.as_view(),name='w_handbags'),
    path('w_footwear', views.w_footwear.as_view(),name='w_footwear'),
    path('w_jewel', views.w_jewel.as_view(),name='w_jewel'),
    path('m_shirt', views.m_shirt.as_view(),name='m_shirt'),
    path('m_watch', views.m_watch.as_view(),name='m_watch'),
    path('m_shades', views.m_shades.as_view(),name='m_shades'),
    path('wishlist', views.wishlist),
]           
                #