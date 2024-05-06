from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from products.models import Product
from .models import UserProfile, WishList
from .forms import UserProfileForm

# pylint: disable=no-member

@login_required
def profile(request):
    """ Display the user's profile. """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()
    wishlist = WishList.objects.filter(user=request.user)
    

    template = 'profiles/profile.html'
    context = {
        'form': form,     
        'orders': orders,
        'on_profile_page': True
    }
    if wishlist:
        wishlist_objects = wishlist.product.all()
        context['wishlist'] = wishlist_objects
    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    # Get the product
    product = Product.objects.get(pk=product_id)
    wishlist, created = WishList.objects.get_or_create(user=request.user)
    redirect_url = request.POST.get('redirect_url')
    # Check if the product is already in the user's wishlist
    wishlist_exists = WishList.objects.filter(user=request.user, product=product).exists()
    if wishlist_exists:
        # Product is already in the wishlist, handle accordingly (e.g., show a message)
        wishlist.product.remove(product)
        messages.success(request, 'product removed from wishlist')
        return redirect(redirect_url)
    # Add the product to the user's wishlist

    wishlist.product.add(product)
    # Optionally, you can show a success message or redirect to another page
    # return redirect('product_detail', product_id=product_id)  # Redirect to product detail page
    redirect_url = request.POST.get('redirect_url')
    messages.success(request, 'product added to wishlist')
    return redirect(redirect_url)
