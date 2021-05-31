from django.shortcuts import render, get_object_or_404


def thanks(request, order_id):
    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)

    context = {
        'customer_order': customer_order,
    }

    return render(request, 'thanks.html', context)
