from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
def product(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request,'website/product.html',context)
def productOrder(request):
    p_orders = ProductOrder.objects.all()
    for p in p_orders:
        print("p",p.order)
    context = {
        'p_orders':p_orders,
    }
    return render(request,'website/productOrder.html',context)
def orders(request):
    ord = Orders.objects.all()
    context = {
        'orders':ord,
    }
    return render(request,'website/order.html',context)
def signUp(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form=createuserform()
        customerform=createcustomerform()
        if request.method=='POST':
            form=createuserform(request.POST)
            customerform=createcustomerform(request.POST)
            if form.is_valid() and customerform.is_valid():
                user=form.save()
                #setting user as thje login user in customer table
                customer=customerform.save(commit=False)
                customer.user=user
                customer.save()
                return redirect('login')
        context={
            'form':form,
            'customerform':customerform,
        }
        return render(request,'website/signUp.html',context)

def addOrder(request):
    form = createproductorderform()
    if (request.method == 'POST'):
        form = createproductorderform(request.POST)
        if form.is_valid()  :
           form.save()
        else:
            print(form.errors)

        return redirect('orders')
    context = {'form': form}
    return render(request, 'website/addOrder.html', context)
def addProduct(request):
    form=createproductform()
    if(request.method=='POST'):
        form=createproductform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'website/addProduct.html',context)
def addSpecs(request):
    form=createspecsform()
    if(request.method=='POST'):
        form=createspecsform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'website/specs.html',context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('product')
    else:
       if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
       context={}
       return render(request,'website/login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('/')


