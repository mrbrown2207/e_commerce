from django.shortcuts import render, redirect, reverse


# Create your views here.

def view_cart(request):
    """A view that renders the cart contents page"""
    """
    We don't have to pass in a dictionary of cart_contents
    because that context is available everywhere
    """
    return render(request, "cart.html")


def add_to_cart(request):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get("quantity"))

    """
    This is getting from the session. It will either get a
    cart or return an empty dictionary
    """
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request):
    """Adjust the quantity of specified product by specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
