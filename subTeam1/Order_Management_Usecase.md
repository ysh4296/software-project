# Order_Management_Diagram


![use_case](https://user-images.githubusercontent.com/29854638/115251364-71538580-a165-11eb-9933-4f8005d47ea8.PNG)


서브그룹: 조중현, 전현욱
1. Order_Management의 Use-case를 도출하면서 저번주에 논의한 내용으로는 부족하다고 판단하였음. 
2. Actor에 배달원 추가 하였음. 주문현황과 배달현황을 확인하는 actor가 필요했음. 

# Requirements
REQ-1: 구매자는 상호명, 피자 메뉴 이름등을 검색하여 원하는 검색결과를 얻는다.
REQ-2: 구매자는 자신이 지정한 우선순위(예: 별점순, 리뷰순, 거리순)로 피자집을 정렬해서 볼 수 있다.
REQ-3: 구매자는 피자집의 정보(예: 메뉴, 위치, 전화번호)를 확인할 수 있다.
REQ-4: 구매자는 검색의 편의성을 위해 피자집 및 메뉴에 대해 즐겨찾기 할 수 있다.
REQ-5: 구매자는 자신의 기호에 맞춰 필터링(가게, 금액, 거리, 피자) 기능을 사용할 수 있다.
REQ-6: 구매자는 메뉴를 장바구니에 담을 수 있다.
REQ-7: 구매자는 자신의 장바구니의 상태(총 금액, 메뉴 종류 및 수량)를 확인할 수  있어야 한다.
REQ-8: 구매자는 장바구니에 들어있는 메뉴를 수정할 수 있다.
REQ-9: 구매자는 판매자가 주문을 수락하기 전에는 주문을 취소할 수 있다. 
REQ-10: 구매자는 추가 요청사항을 피자집(판매자)에게 전달할 수 있다..
REQ-11: 구매자는 결제 방식(온라인결제, 수령시 결제)을 선택할 수 있다.  
REQ-12: 구매자는 배달 현황을 확인할 수 있다.
REQ-13: 판매자는 구매자의 주문정보(주소, 메뉴)를 확인할 수 있다.
REQ-14: 판매자는 구매자의 주문요청을 수락 또는 취소할 수 있다.
REQ-15: 판매자는 구매자의 주문요청을 수락할 수 있다.
REQ-16: 판매자는 배달 현황을 업데이트 할 수 있다.

|      Actor  |Actor's goal         |UC                   
|--------------|--------------------|------------------
|구매자 |필터링, 정렬, 검색을 통해 원하는 가게 및 메뉴 찾기. |O-UC1             
|구매자 |검색한 피자집의 정보를 확인 |O-UC1    
|구매자 |배장 및 메뉴 즐겨찾기 기능 이용 |O-UC5
|구매자 |메뉴를 장바구니에 추가 |O-UC3, O-UC8
|구매자 |장바구니에 있는 메뉴 삭제 |O-UC3, O-UC10     
|구매자 |장바구니에 있는 메뉴 수량 변경 |O-UC3, O-UC9 
|구매자 |현재 장바구니의 상태 확인|O-UC3 
|구매자 |주문하기|O-UC2
|구매자 |결제방식 선택하기 |O-UC2 
|구매자 |추가적인 요청사항 전달 |O-UC2 
|구매자,판매자,배달원 |배달 현황 확인 |O-UC4  
|구매자, 판매자 |주문취소 |O-UC6
|판매자, 배달원 |배달 현황 업데이트 |O-UC4

# Order_Management Usecase

O-UC1: Search

O-UC2: Order

O-UC3: Manage_Shopping_Bag

O-UC4: Order_Status

O-UC5: Delivery_Status

O-UC6: Cancel_Order

O-UC7: Favorites

O-UC8: Menu_Add

O-UC9: Menu_Quantity_Change

O-UC10: Menu_Delete

## Description

Order_Status는 내가 뭘 주문하였는지 확인 및 Delivery_Status, Cancel_Order include

Delivery_Status는 배달현황을 보여는 주는 것

배달현황
주문요청-> 주문수락 or 주문취소(판매자)-> 배달중(판매자)-> 배달완료(배달원)

## Traceability Matrix
![스크린샷(35)](https://user-images.githubusercontent.com/29910793/115740607-f2ab5200-a3c9-11eb-8164-3ff086807e07.png)


