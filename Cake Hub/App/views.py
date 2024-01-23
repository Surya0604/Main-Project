from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from App.models import Product, CartItem
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def signupage(request):
	if request.method == 'POST':
		uname=request.POST.get('username')
		email=request.POST.get('email')
		pass1=request.POST.get('pass1')
		pass2=request.POST.get('cpass1')
		if pass1!=pass2:
			messages.info(request,"user not exist")
		my_user=User.objects.create_user(uname,email,pass1)
		my_user.save()
		return redirect('App:login')
	
		
	return render(request,'signup.html')
def loginpage(request):
	if request.method=='POST':
		username=request.POST.get('username')
		pass1=request.POST.get('pass')
		user=authenticate(request,username=username,password=pass1)
		if user is not None:
			login(request,user)
			return redirect('App:home')
		else:
			messages.info(request,'User Not Exist')
			print('user not exist!!')
			return redirect('App:login')
	return render(request,'login.html')
def logoutpage(request):
	logout(request)
	return redirect('App:login')
	
@login_required(login_url=login)
def home(request):
	products = Product.objects.all()
	return render(request, 'home.html', {'products': products})
@login_required
def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.product.price * item.quantity for item in cart_items)
	return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
	cart_item.quantity += 1
	cart_item.save()
	return redirect('App:view_cart')

def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect('App:view_cart')


def about(request):
	return render(request, 'about.html')	

def contact(request):
	return render(request, 'contact.html')	

def buy(request):
	return render(request, 'buynow.html')	

def success(request):
	return render(request, 'success.html')	

def thank(request):
	return render(request, 'thank.html')	

