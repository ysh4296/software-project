import stripe
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib import messages

from .models import Cart, CartItem
from shop.models import Product
from order.models import Order, OrderItem


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, __ = Cart.objects.get_or_create(cart_id=_cart_id(request))
    cart_item, is_created = CartItem.objects.get_or_create(
        product=product,
        cart=cart,
        defaults={
            'quantity': '1',
        },
    )

    if not is_created and cart_item.quantity < cart_item.product.stock:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart_detail')


def cart_detail(request, total=0, counter=0, cart_items=None, products=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'Perfect Cushion Shop - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billing_name = request.POST['stripeBillingName']
            billing_address = request.POST['stripeBillingAddressLine1']
            billing_city = request.POST['stripeBillingAddressCity']
            billing_postcode = request.POST['stripeBillingAddressCountryCode']
            billing_country = request.POST['stripeBillingCountryCode']
            shipping_name = request.POST['stripeShippingName']
            shipping_address = request.POST['stripeShippingAddressCity']
            shipping_city = request.POST['stripeShippingAddressCity']
            shipping_postcode = request.POST[
                'stripeShippingAddressCountryCode'
            ]
            shipping_country = request.POST['stripeShippingCountryCode']
            customer = stripe.Customer.create(
                email=email,
                source=token,
            )
            charge = stripe.Charge.create(
                amount=stripe_total,
                currency='gbp',
                description=description,
                customer=customer.id,
            )

            # Creating the order
            try:
                order_details = Order.objects.create(
                    token=token,
                    total=total,
                    email_address=email,
                    billing_name=billing_name,
                    billing_address=billing_address,
                    billing_city=billing_city,
                    billing_postcode=billing_postcode,
                    billing_country=billing_country,
                    shipping_name=shipping_name,
                    shipping_address=shipping_address,
                    shipping_city=shipping_city,
                    shipping_postcode=shipping_postcode,
                    shipping_country=shipping_country,
                )
                order_details.save()
                for cart_item in cart_items:
                    oi = OrderItem.objects.create(
                        product=cart_item.product.name,
                        quantity=cart_item.quantity,
                        price=cart_item.product.price,
                        order=order_details,
                    )
                    oi.save()
                    product = Products.objects.get(id=cart_item.product.id)
                    products.stock = int(
                        cart_item.product.stock - cart_item.quantity
                    )
                    product.save()
                    cart_item.delete()
                    print('The order has been created.')
                return redirect('order:thanks', order_details.id)
            except ObjectDoesNotExist:
                pass
        except stripe.error.CardError as e:
            return False, e

    context = {
        'cart_items': cart_items,
        'total': total,
        'counter': counter,
        'data_key': data_key,
        'stripe_total': stripe_total,
        'description': description,
    }

    return render(request, 'cart.html', context)


def remove_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(
        product=product,
        cart=cart,
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        messages.warning(request, "수량이 1개밖에 없습니다.")

    return redirect('cart:cart_detail')


# 휴지통버튼
def full_remove_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(
        product=product,
        cart=cart,
    )

    cart_item.delete()

    return redirect('cart:cart_detail')
