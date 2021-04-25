# Order_Management_Diagram


![use_case](https://user-images.githubusercontent.com/29854638/115251364-71538580-a165-11eb-9933-4f8005d47ea8.PNG)


서브그룹: 조중현, 전현욱
1. Order_Management의 Use-case를 도출하면서 저번주에 논의한 내용으로는 부족하다고 판단하였음. 
2. Actor에 배달원 추가 하였음. 주문현황과 배달현황을 확인하는 actor가 필요했음. 



|      Actor  |Actor's goal         |UC                   
|--------------|--------------------|------------------
|구매자 |필터링, 정렬, 검색을 통해 원하는 가게 및 메뉴 찾기. |O-UC1             
|구매자 |검색한 피자집의 정보를 확인 |O-UC1    
|구매자 |배장 및 메뉴 즐겨찾기 기능 이용 |O-UC6
|구매자 |메뉴를 장바구니에 추가 | O-UC7
|구매자 |장바구니에 있는 메뉴 삭제 |O-UC9     
|구매자 |장바구니에 있는 메뉴 수량 변경 | O-UC8 
|구매자 |현재 장바구니의 상태 확인|O-UC7, O-UC8, O-UC9 
|구매자 |주문하기|O-UC2
|구매자 |결제방식 선택하기 |O-UC2 
|구매자 |추가적인 요청사항 전달 |O-UC2 
|구매자 |자신의 주문내용 및 현재 배달상황 확인|O-UC3 
|구매자 |주문취소 |O-UC5
|판매자, 배달원 |배달 현황 업데이트(판매자의 주문수락/거절 포함) |O-UC4

# Order_Management Usecase

O-UC1: Search

O-UC2: Order

O-UC3: Order_Info_Check

O-UC4: Delivery_Status_Update

O-UC5: Cancel_Order

O-UC6: Favorites

O-UC7: Menu_Add

O-UC8: Menu_Quantity_Change

O-UC9: Menu_Delete

## Description

Order_Info_Check에서는 구매자가 자신의 주문정보 및 현재 배달상황 열람가능

배달현황의 단계
주문요청-> 주문수락(판매자) or 주문취소(판매자)-> 배달중(배달원)-> 배달완료(배달원)
-괄호의 내용은 업데이트 actor

## Traceability Matrix
![스크린샷(40)](https://user-images.githubusercontent.com/29910793/115995965-693d8f00-a618-11eb-8a22-6a444e959d35.png)




