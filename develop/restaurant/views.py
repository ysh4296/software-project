from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# 클래스형 뷰, 함수형 뷰
# 클래스형 뷰 : 기본적으로 만들어져 있는 뷰를 django에서 만들어놓음.
# 웹 페이지에 접속한다. -> 페이지를 본다.
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다. -> 응답
from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Review, Orderlog, Menu
from .forms import RestaurantForm, ReviewForm, MenuaddForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib import messages

def list(request):
    user = request.user
    restaurants = Restaurant.objects.all()
    page = request.GET.get('page')  # 파라미터로 넘어온 현재 페이지 값
    paginator = Paginator(restaurants, 5)  # 한 페이지에 5개씩 표시
    items = paginator.get_page(page)  # 해당 페이지에 맞는 리스트로 필터링
    context = {
        "restaurants": items
    }
    return render(request, 'restaurant/list.html', context)

def create(request):
    user = request.user
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/restaurant/list/')
    form = RestaurantForm()
    return render(request, 'restaurant/create.html', {'form': form})

def review_delete(request, restaurant_id, review_id):
    user = request.user
    item = get_object_or_404(Review, pk=review_id)
    item.delete()
    return redirect('restaurant-detail', id=restaurant_id)

class detail_model(ListView):
    def checklog(self, item, username):
        nval = Review.objects.filter(reviewer=username).all() & Review.objects.filter(restaurant=item).all() # 식당에 해당하는 리뷰을 조회
        if nval.exists():
            return False
        rval = Orderlog.objects.filter(reviewer=username).all() & Orderlog.objects.filter(restaurant=item).all()
        if rval.exists() == False:
            return False
        return True

    def get(self, request, id):
        user = request.user
        if 'id' is not None:
            item = get_object_or_404(Restaurant, pk=id)
            reviews = Review.objects.filter(restaurant=item).all()  # 식당에 해당하는 리뷰을 조회
            val = self.checklog(item,request.user.username)
            return render(request, 'restaurant/detail.html', {'item': item, 'reviews': reviews,'val' : val})
        return HttpResponseRedirect('/restaurant/list/')

class Review_model(ListView):
    def get(self, request, restaurant_id):
        user = request.user
        #form = ReviewForm(request.POST)
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        form = ReviewForm(initial={'restaurant': item, 'reviewer': request.user.username})
        return render(request, 'restaurant/review_create.html', {'form': form, 'item': item})

    def post(self, request, restaurant_id):
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurant-detail', id=restaurant_id)

class Menu_add(ListView):
    def checklog(self, item, menu_name):
        val = Menu.objects.filter(name=menu_name).all() & Menu.objects.filter(restaurant=item).all() # 같은이름의 메뉴가 있는지 검색
        if val.exists():
            return False
        return True

    def get(self, request, restaurant_id):
        user = request.user
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        form = MenuaddForm(initial={'restaurant': item})
        return render(request, 'restaurant/menu_add.html', {'form': form, 'item': item})

    def post(self, request, restaurant_id):
        user = request.user
        print(USER_SELLER)
        form = MenuaddForm(request.POST)
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        if form.is_valid():
            print(form.cleaned_data['name'])
            val = self.checklog(item,form.cleaned_data['name'])
            if val == False:
                print("duplication error")
                messages.warning(request,"같은 이름의 메뉴가 있습니다.")
                return render(request, 'restaurant/menu_add.html', {'form': form, 'item': item})
            else:
                new_item = form.save()
        else:
            messages.warning(request, "메뉴의 모든 요소를 작성해주십시오.")
            return render(request, 'restaurant/menu_add.html', {'form': form, 'item': item})
        return redirect('restaurant-detail', id=restaurant_id)


