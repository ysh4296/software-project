# Order_Management_Diagram


![use_case](https://user-images.githubusercontent.com/29854638/115251364-71538580-a165-11eb-9933-4f8005d47ea8.PNG)


서브그룹: 조중현, 전현욱
1. Order_Management의 Use-case를 도출하면서 저번주에 논의한 내용으로는 부족하다고 판단하였음. 
2. Actor에 배달원 추가 하였음. 주문현황과 배달현황을 확인하는 actor가 필요했음. 

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
![스크린샷(33)](https://user-images.githubusercontent.com/29910793/115250899-f8ecc480-a164-11eb-94e1-d4894c21ce1d.png)

