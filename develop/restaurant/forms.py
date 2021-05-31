from django import forms
from . models import Restaurant, Review, Menu


from django.utils.translation import gettext_lazy as _

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address']
        labels = {
            'name': _('이름'),
            'address': _('주소'),
        }
        help_texts = {
            'name': _('이름을 입력해주세요.'),
            'address': _('주소를 입력해주세요.'),
        }
        error_messages = {
            'name': {
                'mex_length': _('이름은 30자 이하로 정해주세요.')
            }
        }

# 평점의 선택지
REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant', 'reviewer']
        labels = {
            'point': _('평점'),
            'comment': _('코멘트'),
        }
        widgets = {
            'restaurant': forms.HiddenInput(),  # 리뷰를 달 식당 정보는 사용자에게 보여지지 않도록 한다
            'reviewer': forms.HiddenInput(), #리뷰어의 이름을 입력할 필요는 없다.
            'point': forms.Select(choices=REVIEW_POINT_CHOICES)  # 선택지를 인자로 전달
        }
        help_texts = {
            'point': _('평점을 입력해주세요.'),
            'comment': _('코멘트를 입력해주세요.'),
        }

class MenuaddForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'price', 'component', 'ingredient','restaurant']
        labels = {
            'name': _('메뉴 이름'),
            'component': _('메뉴 구성'),
            'ingredient': _('재료'),
            'price': _('가격'),
        }
        widgets = {
            'restaurant': forms.HiddenInput(),  # 리뷰를 달 식당 정보는 사용자에게 보여지지 않도록 한다
        }
        help_texts = {
            'name': _('메뉴 이름을 입력해주세요.'),
            'component': _('메뉴 구성을 입력해주세요.'),
            'ingredient': _('재료를 입력해주세요.'),
            'price': _('가격을 입력해주세요.'),
        }