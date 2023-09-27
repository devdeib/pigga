from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            return redirect('login')
    return render(request, 'login.html')

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = form.cleaned_data['is_superuser']
            user.is_staff = form.cleaned_data['is_staff']
            user.save()
            return redirect('home') 
    else:
        form = AddUserForm()
    return render(request, 'adduser.html', {'form': form})


def delete_user(request, username):
    user = User.objects.get(username=username)
    user.delete()
    return redirect('users')


def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)


def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'menu_items': menu_items})


def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = MenuItem.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            address = form.cleaned_data.get('address')
            UserProfile.objects.create(user=user, address=address)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})


    
def order_view(request):
     menu_items = MenuItem.objects.all()
     return render(request, 'order_page.html', {'menu_items': menu_items})
 
  
def submit_order(request):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        selected_item_ids = request.POST.getlist('selected_items')
        selected_items = MenuItem.objects.filter(pk__in=selected_item_ids)
        total_price = 0
        for item in selected_items:
          total_price += item.price
        return render(request, 'order_confirmation.html', {'selected_items': selected_items, 'total_price': total_price, 'user_profile': user_profile, 'address': user_profile.address})
    else:
        return redirect('order_page')  # Redirect to the order page if the request method is not POST        



def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')
    form = MenuItemForm()
    return render(request, 'add_menu_item.html', {'form': form})


def menu_item_detail(request, item_id):
    menu_item = get_object_or_404(MenuItem, pk=item_id)
    return render(request, 'menu_item_detail.html', {'menu_item': menu_item})