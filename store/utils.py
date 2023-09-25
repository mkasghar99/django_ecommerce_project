# store/utils.py
from .models import Product  # Import the Product model

def add_to_cart(request, product_id, quantity=1):
    product_id = str(product_id)
    if 'cart' not in request.session:
        request.session['cart'] = {}
    cart = request.session['cart']

    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session.modified = True

def remove_from_cart(request, product_id):
    product_id = str(product_id)
    if 'cart' in request.session:
        cart = request.session['cart']
        if product_id in cart:
            del cart[product_id]
            request.session.modified = True

def update_cart(request, cart):
    request.session['cart'] = cart
    request.session.modified = True

def clear_cart(request):
    if 'cart' in request.session:
        del request.session['cart']
        request.session.modified = True

def cart_summary(cart):
    total_price = 0
    total_items = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(pk=product_id)
        item_price = product.price * quantity
        total_price += item_price
        total_items += quantity

    return total_price, total_items