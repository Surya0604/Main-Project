from django.urls import path
from App import views




app_name = 'App'
urlpatterns = [
    path('home/',views.home,name='home'),
    path('signup/',views.signupage,name='signup'),
    path('',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
	path('cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('buy/',views.buy,name='buy'),
    path('success/',views.success,name='success'),
    path('thank/',views.thank,name='thank'),
  
]