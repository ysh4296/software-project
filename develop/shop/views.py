from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm
from .models import Category, Product


def index(request):
    text_var = 'shopping bag develop'
    return HttpResponse(text_var)


def all_products_by_category(request, category_slug=None):
    category_page = None
    products_list = None

    if category_slug is not None:
        category_page = get_object_or_404(Category, slug=category_slug)
        products_list = Product.objects.filter(
            category=category_page,
            available=True,
        )
    else:
        products_list = Product.objects.all().filter(available=True)

    paginator = Paginator(products_list, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    context = {
        'category': category_page,
        'products': products,
    }

    return render(request, 'shop/category.html', context)


def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(
        Product,
        category__slug=category_slug,
        slug=product_slug,
    )

    context = {
        'product': product,
    }

    return render(request, 'shop/product.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request, 'shop:all_products')
            else:
                return redirect(request, 'signup')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})


def signout_view(request):
    logout(request)
    return redirect(request, 'shop:all_products')
