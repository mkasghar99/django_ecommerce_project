# store/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.models import User  # Import User model
from django.contrib.auth import login
from django.contrib.auth import logout
from .forms import RegistrationForm
from .forms import UserLoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .utils import add_to_cart, remove_from_cart, cart_summary




@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

@login_required
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'store/product_form.html', {'form': form})

@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'store/product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'store/product_confirm_delete.html', {'product': product})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('product_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('product_list')

def public_product_list(request):
    products = Product.objects.all()
    # Define the number of products per page
    items_per_page = 2

    # Create a Paginator instance
    paginator = Paginator(products, items_per_page)

    # Get the current page number from the request's GET parameters
    page_number = request.GET.get('page')

    # Get the Page object for the current page
    page = paginator.get_page(page_number)

    return render(request, 'store/public_product_list.html', {'page': page})

def add_to_cart_view(request, product_id):
    add_to_cart(request, product_id)
    return redirect('cart')

def remove_from_cart_view(request, product_id):
    remove_from_cart(request, product_id)
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    total_price, total_items = cart_summary(cart)

    # Calculate item prices
    cart_items = []
    for product_id, quantity in cart.items():
        product = Product.objects.get(pk=product_id)
        item_price = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_price': item_price,
        })

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'total_items': total_items,
    }

    return render(request, 'store/cart.html', context)