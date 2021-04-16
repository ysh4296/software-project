# Order_Management_Diagram
![UseCaseDiagram](https://user-images.githubusercontent.com/29910793/114296154-889acf00-9ae4-11eb-8198-1341aeda2539.png)

서브그룹: 조중현, 전현욱
1. Order_Management의 Use-case를 도출하면서 저번주에 논의한 내용으로는 부족하다고 판단하였음. 
2. Actor에 배달원 추가 하였음. 주문현황과 배달현황을 확인하는 actor가 필요했음. 

|      Actor  |Actor's goal         |UC                   
|--------------|--------------------|------------------
|구매자 |주문하기              |O-UC1, O-UC2, O-UC3             
|구매자 |필터링을 통해 가게 찾기 |O-UC1, UC2    
|구매자 |필터링을 통해 메뉴 찾기 |O-UC2
|구매자,판매자,배달원 |주문 현황 |O-UC5 
|구매자 |메뉴 장바구니에 추가 |O-UC11, O-UC3     
|구매자 |장바구니에 있는 메뉴 삭제 |O-UC11, O-UC3  
|구매자 |장바구니에 있는 메뉴 수량 변경|O-UC12, O-UC3 
|구매자 |즐겨찾기 이용 |O-UC7
|구매자 |결제방식 선택하기 |O-UC10 
|구매자 |추가적인 요청사항 전달 |O-UC11 
|구매자,판매자,배달원 |배달 현황 확인 |O-UC14  
|구매자 |주문취소 |O-UC3, O-UC4
|구매자 |주문후 자신의 총 주문금액을 확인할 수 있다 |O-UC10

# Order_Management Usecase

O-UC1: Search

O-UC2: Filter

O-UC3: Order

O-UC4: Order_Cancel

O-UC5: Manage_Shopping_Bag

O-UC6: Order_Status

O-UC7: Favorites

O-UC8: Shop_Filter

O-UC9: Menu_Filter

O-UC10: Payment_Method

O-UC11: Additional_Req

O-UC12: Menu_Edit

O-UC13: Menu_Quatity

O-UC14: Show_Delivery_Status

## Description

Order_Status는 내가 뭘 주문하였는지 확인

Payment_Method는 결제방식 및 수령방식을 선택함

Show_Delivery_Status는 배달현황을 보여는 주는 것

  

방문수령: 주문접수완료 -> 조리중 -> 픽업가능

배달수령: 주문접수완료 -> 조리중 -> 배달 중 -> 배달완료 or 주문취소
