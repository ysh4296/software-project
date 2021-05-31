# Final _ check point

## 1. 목차
1. 구현 범위
   1. UC1 Search
   2. UC7 Menu Add
   3. UC8 Menu_quantity_change
   4. UC9 Menu_delete
   
2. 결론  

3. 느낀점  

## 2. 구현범위
### Usecase-1 Search
- 주어진 검색바에 원하는 keyword를 입력하여 검색을 한다.
![Search](https://user-images.githubusercontent.com/29910793/120190225-445dbc80-c253-11eb-9d42-ca348d0dd194.gif)
- 완전하게 구현하진 못하였음
---
### Usecase-7 Menu Add (장바구니에)
 - 특정 피자 가게의 페이지에 접속한 상태에서는 위에 피자가게 로고와 함께, 등록된 피자의 목록이 뜬다. 
 - 특정 메뉴를 선택하면 메뉴 정보와 함께 Add Cart버튼이 활성화 된다.
 - Add Cart 버튼을 누르면 장바구니에 상품이 담긴다. ( 이 부분은 원래 장바구니 창으로 이동하지 않고 팝업으로 장바구니 담기 성공을 띄우려고 했으나, 구현의 어려움을 겪어서 노선을 변경하였음)
#### :small_blue_diamond: Detail!
![Honeycam 2021-05-31 23-09-44](https://user-images.githubusercontent.com/29854638/120205784-521c3d80-c265-11eb-9a57-29b2101e887e.gif)

---
### Usecase-8 Menu_quantity_change
  - 장바구니에 메뉴가 담긴 상태에서 +, - 버튼으로 수량 조정 가능
  - 수량이 1개인 상태에서 -버튼을 누르면, 위에 "수량이 1개밖에 없습니다" 경고창을 띄운다.
  - 각 상품의 수량에 따른 가격을 볼 수 있다.
  - 장바구니의 총 금액을 볼 수 있다.
  - continue shopping을 눌러서 다시 상품들이 있는 페이지로 이동할 수 있다.
#### :small_blue_diamond: 전체적 기능!
![Honeycam 2021-05-31 23-19-24](https://user-images.githubusercontent.com/29854638/120206849-aaa00a80-c266-11eb-9049-5246c8c7cfc1.gif)
#### :small_blue_diamond: 수량 1개일 때, 수량감소 버튼 클릭 시 경고발생
![Honeycam 2021-05-31 23-17-38](https://user-images.githubusercontent.com/29854638/120206675-73c9f480-c266-11eb-9d0b-307bf985c111.gif)

---
### Usecase-9 Menu_delete
  - 장바구니에서 메뉴 옆의 휴지통 버튼을 클릭하면 메뉴가 삭제됨.
#### :small_blue_diamond: detail!
![Honeycam 2021-05-31 23-20-30](https://user-images.githubusercontent.com/29854638/120206988-d15e4100-c266-11eb-8289-65495831af19.gif)

---

### 결론
1. 사용언어 및 기술스택: python, django, html, css, js
2. About 프로젝트
- 처음에 정한 30%를 완벽하게 구현하진 못했지만, requirement분석->설계->개발 까지의 단계를 경험할 수 있었음
- 다른 subteam들과의 의사소통을 통해서 비교적 큰 범위의 프로젝트를 수행하였음
- class, sequence diagram을 작성할 때와 실제 개발에는 차이가 있음을 깨달았음. (아마도 diagram작성 시에는 django framework를 사용하는 것을 염두에 두지 않아서 그런듯함). 이런 점들이 개발을 어렵게 만드는 요인이었음


###  구현하면서 느낀 점
- 이전에는 경험하지 못한 전혀 다른 방식으로 이번 프로젝트를 시작했습니다. 그 과정에서 기존에는 생각하지 못하거나 신경 쓰지 않던 부분들을 고심하면서 프로젝트에 임하게 되었습니다. 개발자로서의 입장을 어느 정도 내려놓고 고객의 요구 사항을 만족을 최우선으로 생각하는 방향으로 나아갔습니다. 
- 개발을 하면서 한 번도 고객의 입장을 생각해본적이 없었는데, 이번 프로젝트 경험으로 많은 고민을 하게 되었음. 한 학기동안 열심히 했지만, 이런 종류의 프로젝트를 수행한 경험이 부족해서 많이 어려웠음. 무엇보다도 팀원 내의 의사소통이 '왜' 중요한지를 많이 느꼈음. 개발 부분에서의 부족함이 많았지만 어려울 때 도와주고 각자 최선을 다한 팀원들에게 고마움을 느꼈음

