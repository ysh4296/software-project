from django.db import models

# Create your models here.
# 모델 : 데이터베이스를 SQL없이 다루려고 모델을 사용
# 우리가 데이터를 객체화해서 다루겠다.
# 모델 = 테이블
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값
# /models.py
from users.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    point = models.IntegerField()
    comment = models.CharField(max_length=500)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    reviewer = models.CharField(max_length=150, default = "NONE")
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항 (몇글자까지)
    # 3. Form의 종류
    # 4. Form에서 제약 사항
    # 5. 작성자
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # 모델을 만들었다 => 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정.
    # 마이그레이션(migrate) => 데이터베이스에 모델의 내용을 반영(테이블 생성)
    # 모델을 수정하면, 또다시 migrate해야함

class Orderlog(models.Model):
    reviewer = models.CharField(max_length=150, default = "NONE")
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Menu(models.Model):
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=500)
    component = models.CharField(max_length=500)
    ingredient = models.CharField(max_length=500)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE) # sellor 는 restaurant로 교체
