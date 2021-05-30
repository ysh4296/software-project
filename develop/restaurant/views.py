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


####### 리스트모델인 클래스형 뷰로 선언
class list_model(ListView):
    ####### seller 에게만 등록 버튼이 보이도록 check_user 이용
    def check_user(self, username):
        if username.user_type == 'seller':
            return True
        return False

    def get(self, request):
        nval = self.check_user(request.user)
        rest = Restaurant.objects.filter(user=request.user).exists()
        if rest == True:
            ids = Restaurant.objects.filter(user=request.user).values_list('pk', flat=True)
        else:
            ids = [-1]
        ###### 가게가 승인된 것만(TRUE) 저장
        restaurants = Restaurant.objects.filter(accepted=True).all()
        page = request.GET.get('page')  # 파라미터로 넘어온 현재 페이지 값
        paginator = Paginator(restaurants, 5)  # 한 페이지에 5개씩 표시
        items = paginator.get_page(page)  # 해당 페이지에 맞는 리스트로 필터링
        context = {
            "restaurants": items,'rest' : rest,'rest_id' : ids[0]
        }
        return render(request, 'restaurant/list.html', context)

#################################################### 이제 지워도되는 부분 #################################################
#def list(request):
#    restaurants = Restaurant.objects.filter(accepted=True).all()
#    page = request.GET.get('page')  # 파라미터로 넘어온 현재 페이지 값
#    paginator = Paginator(restaurants, 5)  # 한 페이지에 5개씩 표시
#    items = paginator.get_page(page)  # 해당 페이지에 맞는 리스트로 필터링
#    context = {
#        "restaurants": items
#    }
#    return render(request, 'restaurant/list.html', context)
#
#def create(request):
#    if request.method == "POST":
#        form = RestaurantForm(request.POST)
#        if form.is_valid():
#            new_item = form.save()
#        return HttpResponseRedirect('/restaurant/list/')
#    form = RestaurantForm()
#    return render(request, 'restaurant/create.html', {'form': form})
########################################################################################################################

##05월30일  1105 추가
class Shop_model(ListView):
    ########## 식당이름 중복인지 조회
    def checkshop(self, request):
        nval = Restaurant.objects.filter(name=request.POST['name']).all() #식당 이름이 중복인지 조회
        if nval.exists():
            return False
        rval = Restaurant.objects.filter(user=request.user).all()
        if rval.exists():
            return False
        return True

    ######## shop 만드는 페이지 띄우기
    def get(self, request):
        rest = Restaurant.objects.filter(user=request.user).exists()
        if rest == True:
            ids = Restaurant.objects.filter(user=request.user).values_list('pk', flat=True)
        else:
            ids = [-1]
        form = RestaurantForm()
        return render(request, 'restaurant/create.html', {'form': form,'rest' : rest,'rest_id' : ids[0]})

    ######## shop이 중복이면 변화 없음, shop이 중복이 아니면 요청이 넘어가는데 현재 ACCEPTED 상태가 아니라서 안보임
    def post(self, request):
        form = RestaurantForm(request.POST)
        nval = self.checkshop(request)
        if nval == True and form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
        return HttpResponseRedirect('/restaurant/list/')



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
        rest = Restaurant.objects.filter(user=request.user).exists()
        if rest == True:
            ids = Restaurant.objects.filter(user=request.user).values_list('pk', flat=True)
        else:
            ids = [-1]
        if 'id' is not None:
            item = get_object_or_404(Restaurant, pk=id)
            reviews = Review.objects.filter(restaurant=item).all()  # 식당에 해당하는 리뷰을 조회
            val = self.checklog(item,request.user.username)
            return render(request, 'restaurant/detail.html', {'item': item, 'reviews': reviews,'val' : val,'rest' : rest,'rest_id' : ids[0]})
        return HttpResponseRedirect('/restaurant/list/',{'rest' : rest})

class Review_model(ListView):
    def get(self, request, restaurant_id):
        user = request.user
        rest = Restaurant.objects.filter(user=request.user).exists()
        if rest == True:
            ids = Restaurant.objects.filter(user=request.user).values_list('pk', flat=True)
        else:
            ids = [-1]
        #form = ReviewForm(request.POST)
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        form = ReviewForm(initial={'restaurant': item, 'reviewer': request.user.username})
        return render(request, 'restaurant/review_create.html', {'form': form, 'item': item,'rest' : rest,'rest_id' : ids[0]})

    def post(self, request, restaurant_id):
        user = request.user
        rest = Restaurant.objects.filter(user=request.user).exists()
        if rest == True:
            ids = Restaurant.objects.filter(user=request.user).values_list('pk', flat=True)
        else:
            ids = [-1]
        form = ReviewForm(request.POST)
        print(request.POST)
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
        rest = Restaurant.objects.filter(user=request.user).exists()
        if rest == True:
            ids = Restaurant.objects.filter(user=request.user).values_list('pk', flat=True)
        else:
            ids = [-1]
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        form = MenuaddForm(initial={'restaurant': item})
        return render(request, 'restaurant/menu_add.html', {'form': form, 'item': item,'rest': rest,'rest_id' : ids[0]})

    def post(self, request, restaurant_id):
        user = request.user
        rest = Restaurant.objects.filter(user=request.user).exists()
        if rest == True:
            ids = Restaurant.objects.filter(user=request.user).values_list('pk', flat=True)
        else:
            ids = [-1]
        form = MenuaddForm(request.POST)
        item = get_object_or_404(Restaurant, pk=restaurant_id)
        if form.is_valid():
            print(form.cleaned_data['name'])
            val = self.checklog(item,form.cleaned_data['name'])
            if val == False:
                messages.warning(request,"같은 이름의 메뉴가 있습니다.")
                return render(request, 'restaurant/menu_add.html', {'form': form, 'item': item,'rest' : rest,'rest_id' : ids[0]})
            else:
                new_item = form.save()
        else:
            messages.warning(request, "메뉴의 모든 요소를 작성해주십시오.")
            return render(request, 'restaurant/menu_add.html', {'form': form, 'item': item,'rest' : rest,'rest_id' : ids[0]})
        return redirect('restaurant-detail', id=restaurant_id)


