from django.urls import path, re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate, login, logout

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('users/', views.users, name="users"),
    path('adduser/', views.add_user, name='add_user'),
    path('delete_user/<str:username>/', views.delete_user, name='delete_user'),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"), 
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('login/', views.login_user, name= "login"),
    path('signup/', views.sign_up, name="sign_up"),
    path('order/', views.order_view, name='order_page'),
    path('order_confirmation/', views.submit_order, name='submit_order'),
    path('add_menu_item/', views.add_menu_item, name='add_menu_item'),
    path('menu/item/<int:item_id>/', views.menu_item_detail, name='menu_item_detail'),

]
