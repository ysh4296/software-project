from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# 클래스형 뷰, 함수형 뷰
# 클래스형 뷰 : 기본적으로 만들어져 있는 뷰를 django에서 만들어놓음.
# 웹 페이지에 접속한다. -> 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답

from django.shortcuts import render, get_object_or_404, redirect
from . models import Restaurant, Review
from . forms import RestaurantForm, ReviewForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

def list(request):
    restaurants = Restaurant.objects.all()
    page = request.GET.get('page') # 파라미터로 넘어온 현재 페이지 값
    paginator = Paginator(restaurants, 5) # 한 페이지에 5개씩 표시
    items = paginator.get_page(page) # 해당 페이지에 맞는 리스트로 필터링
    context = {
        "restaurants": items
    }
    return render(request, 'restaurant/list.html', context)

def create(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/restaurant/list/')
    form = RestaurantForm()
    return render(request, 'restaurant/create.html', {'form': form})

def detail(request, id): # 식당 조회 페이지
    if 'id' is not None:
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all() # 식당에 해당하는 리뷰을 조회
        return render(request, 'restaurant/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/restaurant/list/')

def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        # HttpResponseRedirect을 사용하면 url을 다 써주어야하고, 만약 url이 변경되었을 때 함께 수정해주어야 하는 번거로움이 있음
        # shortcuts의 redirct를 사용하면 url 기반이 아니라 urls.py에 정의한 view name 기반으로 움직이기 때문에
        # url이 변경되더라고 view name이 그대로라면 변경하지 않아도 된다.
        return redirect('restaurant-detail', id=restaurant_id)
    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant': item})
    return render(request, 'restaurant/review_create.html', {'form': form, 'item': item})

def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()
    return redirect('restaurant-detail', id=restaurant_id)