from django.contrib import admin
from django.urls import path
from website.views import *

 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addProduct',addProduct ,name='addProduct'),
    path('product',product ,name='product'),
    path('signUp/', signUp, name='signUp'),
    path('addOrder',addOrder,name='addOrder'),
    path('orders',orders,name='orders'),
    path('', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    # path('addSpecs/', addSpecs, name='addSpecs'),
    path('productOrder', productOrder, name='productOrder'),

]