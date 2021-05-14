## Sequence Diagram
## UC1 sequence diagram
### Early version
### Version #1
![KakaoTalk_20210508_230015452](https://user-images.githubusercontent.com/29910793/118000645-f9056c00-b380-11eb-89c0-6dbb33c6a6b0.jpg)
---
### Version #2
![KakaoTalk_20210513_001716196](https://user-images.githubusercontent.com/29910793/118000710-06225b00-b381-11eb-82ac-1fc7d91646ab.jpg)
---
### __Version #1__에서 #2로의 변화
- 초기 설계 당시 Usecase-1:Search의 범위를 검색까지 생각했었지만, 도메인 모델에서 범위를 가게 선택까지 포함하게 바꾸었다.
- 이를 위해 version #2에서 추가적인 변수와 flow에 변화를 주었다.  위와 같은 변화를 줌으로써 첫번째 Search flow 과정에서 loop를 추가해야 할 필요성을 느끼게 되어 이를 추가하게 되었다.
- 추가적인 variation을 고민해 보았지만, class가 불필요하게 많아지거나, flow의 흐름이 길어지게 되는 경우가 발생하여 이 version으로 결정하게 되었다.
### Final version

## UC7 sequence diagram
### Version #1
![KakaoTalk_20210509_000149621](https://user-images.githubusercontent.com/29910793/118000805-189c9480-b381-11eb-8ac2-baf2696fbc20.jpg)
---
### Version #2
![usecase7Menuadd](https://user-images.githubusercontent.com/29910793/118136635-49db9a00-b43f-11eb-86bc-4c4928a20809.jpg)
---
### __Version #1__에서 #2로의 변화
- Usecase-7:MenuAdd의 범위도 초기 설계와 다르게 바꾸었다. Usecase-7은 Usecase-1 다음으로 바로 이어지게 설계가 되었기 때문에 생긴 결과이다.
- 앞부분의 store_select 부분을 삭제하여, 이에따라 시작하는 page가 Search page가 아닌 Menu page이다.
- Flow가 바뀜에 따라 필요가 없어진 pagemaker와 Searcher class를 삭제했다.
### Version #2-var
![menuaddVar](https://user-images.githubusercontent.com/29910793/118141783-b73df980-b444-11eb-9f7e-1408b9d533ce.jpg)
- 기존에는 컨트롤러에서 직접 database에 정보를 push하는 방식을 생각해냈지만, 컨트롤러의 부하를 최소한으로 줄이기 위해 bagmaker를 추가로 도입하였다.
### Final version

## UC8 sequence diagram
### Early version
<img width="1757" alt="UC8_sequence diagram" src="https://user-images.githubusercontent.com/29854638/117999888-43d2b400-b380-11eb-947d-0e08146b15b4.png">

### UC8 Version #1
![UC8_ver1](https://user-images.githubusercontent.com/29854638/118299239-7664e400-b51b-11eb-9169-bc2ec5b18c04.jpg)
 - __바뀐 점__
-- 초기설계에 존재했던 +,- 버튼, 장바구니 버튼, shopping bag page를 interface page가 모두 포함하므로 interface page 통합했다.
--    초기 버전에서는 ‘bagmaker’, 장바구니 총 금액을 계산해주는 '금액계산기’가 존재했었는데 금액계산기의 기능을 bagmaker가 해도 무관하다고 판단해서 shopping bag maker라는 component로 합쳤다. (bagmaker+금액계산기 = shopping bag maker)
--   기존에는 장바구니에 존재하는 메뉴 리스트를 bagmaker가 직접 관리했는데, 이번에는 shopping bag list라는 component를 추가해서 장바구니 리스트 정보를 따로 관리했다.

### UC8 Version #2
![UC8_ver2](https://user-images.githubusercontent.com/29854638/118300994-84b3ff80-b51d-11eb-94c5-66936ca95672.jpg)
- __version1 관련 고민__
-- version1에서는 초기 장바구니 생성 시 controller->Page Maker->shopping bag maker->list의->DB 순서로 요청을 전달하는데,  굳이 pagemaker을 거쳐서 전달할 필요가 있을까? 라는 고민을 하였다.
-- 기존에는 shopping bag maker, shopping bag list라는 component 2개를 사용해서, 장바구니 관련 연산을 처리하였다. shopping bag maker은 shopping bag list 생성 및 요소제거, list의 금액 계산을 수행하며, shopping bag list는 장바구니 리스트의 목록 데이터를 유지한다. 대부분의 연산이 shopping bag maker에서 이뤄지는 상황이고, list가 maker에게 장바구니 리스트 정보를 리턴하는 상황에서  둘로 나눌 필요가 있을까? 라는 고민을 하였다. 
-- 기존에는 page생성 시에, shopping bag maker->pagemaker로 직접 정보를 return하고 pagemaker가 page를 생성하는 방식이었는데, 다른 UC와의 통일성을 위해 다른 방식으로 수정하는 방향으로 결정했다.

- __바뀐 점__
-- 기존에는 DB만 존재했는데, DB connection을 class로 두고, DB라는 actor을 도입했다.
-- 초기 장바구니 생성 시, controller->shopping bag list->DB연결->DB(actor)을 거쳐서 요청을 전달하는 것으로 수정했다. (pagemaker 경유 X)
-- shopping bag maker와 shopping bag list를 합쳐서 shopping bag list로 명명했다. 
-- controller가 pagemaker에게 page생성을 요청하면 pagemaker가 page를 생성한다.



## UC9 sequence diagram
### Early version
<img width="959" alt="UC9_sequence diagram" src="https://user-images.githubusercontent.com/29854638/117999897-46cda480-b380-11eb-9d4e-7b181dd384df.png">

- UC8 & UC9 sequence diagram 초기설계 issue </br>
기존 domain model은 사용자가 장바구니 페이지로 이동한 상태라고 가정하고 설계했다. sequence diagram을 그리면서 장바구니 페이지로 접속하는 과정이 생략되었음을 알았고, '장바구니 버튼' component를 추가하였다. 

### UC9 version #1
![version1](https://user-images.githubusercontent.com/29854638/118283546-73152c80-b50a-11eb-9213-78a351711f74.jpg)
- 초기설계에 존재했던 삭제버튼, 장바구니 버튼, shopping bag page를 결국에 interface page가 포함하므로 interface page로 합쳤다. 
- 초기 버전에서는 'bagmaker', 장바구니 총 금액을 계산해주는 '금액계산기'가 존재했었는데 금액계산기의 기능을 bagmaker가 해도 무관하다고 판단해서 shopping bag maker라는 component로 합쳤다. (bagmaker+금액계산기 = shopping bag maker)
- 기존에는 장바구니에 존재하는 메뉴 리스트를 bagmaker가 직접 관리했는데, 이번에는 shopping bag list라는 component를 추가해서 장바구니 리스트 정보를 따로 관리했다.
--- 
- __초기 버전 flow__
--__장바구니 초기생성__:  장바구니 버튼->controller->bagmaker->DB->금액계산기->pagemaker
--__menu_delete__: 삭제버튼->controller->bagmaker->금액계산기->bagmaker->controller->DB->pagemaker
- __version1 flow__
--__장바구니 초기생성__: interface page->controller->pagemaker->shopping bag maker-> list->DB->list-> shopping bag maker->pagemaker
--__menu_delete__: interface page->shopping bag maker->list->shopping bag maker->DB->pagemaker


- --
### UC9 Version #2
![UC8_version2 (2)](https://user-images.githubusercontent.com/29854638/118298048-ec684b80-b519-11eb-8560-510baa71b501.jpg)
- __version1 관련 고민__
-- version1에서는 초기 장바구니 생성 시 controller->Page Maker->shopping bag maker->list의->DB 순서로 요청을 전달하는데,  굳이 pagemaker을 거쳐서 전달할 필요가 있을까? 라는 고민을 하였다.
-- 기존에는 shopping bag maker, shopping bag list라는 component 2개를 사용해서, 장바구니 관련 연산을 처리하였다. shopping bag maker은 shopping bag list 생성 및 요소제거, list의 금액 계산을 수행하며, shopping bag list는 장바구니 리스트의 목록 데이터를 유지한다. 대부분의 연산이 shopping bag maker에서 이뤄지는 상황이고, list가 maker에게 장바구니 리스트 정보를 리턴하는 상황에서  둘로 나눌 필요가 있을까? 라는 고민을 하였다. 
-- 기존에는 page생성 시에, shopping bag maker->pagemaker로 직접 정보를 return하고 pagemaker가 page를 생성하는 방식이었는데, 다른 UC와의 통일성을 위해 다른 방식으로 수정하는 방향으로 결정했다.

- __바뀐 점__
-- 기존에는 DB만 존재했는데, DB connection을 class로 두고, DB라는 actor을 도입했다.
-- 초기 장바구니 생성 시, controller->shopping bag list->DB연결->DB(actor)을 거쳐서 요청을 전달하는 것으로 수정했다. (pagemaker 경유 X)
-- shopping bag maker와 shopping bag list를 합쳐서 shopping bag list로 명명했다. 
-- controller가 pagemaker에게 page생성을 요청하면 pagemaker가 page를 생성한다.







