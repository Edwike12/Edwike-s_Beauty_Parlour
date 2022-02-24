from django.urls import path
from . import views

urlpatterns=[
   path('',views.index,name = 'index'),
   path('profile/', views.profile, name='profile'),
   path('update_profile/<int:id>', views.update_profile, name='update_profile'),
   path('products/', views.products, name='products'),
   path('checkout/', views.checkout, name='checkout'),
   path('updates/', views.updates, name='updates'),
   path('cart/', views.cart, name='cart'),

]   