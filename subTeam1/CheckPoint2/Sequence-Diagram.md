## Sequence Diagram
## UC1 sequence diagram
### Version #1
![KakaoTalk_20210508_230015452](https://user-images.githubusercontent.com/29910793/118000645-f9056c00-b380-11eb-89c0-6dbb33c6a6b0.jpg)
---
### Version #2
![KakaoTalk_20210513_001716196](https://user-images.githubusercontent.com/29910793/118000710-06225b00-b381-11eb-82ac-1fc7d91646ab.jpg)

## UC7 sequence diagram
### Version #1
![KakaoTalk_20210509_000149621](https://user-images.githubusercontent.com/29910793/118000805-189c9480-b381-11eb-8ac2-baf2696fbc20.jpg)
---
### Version #2
![usecase7Menuadd](https://user-images.githubusercontent.com/29910793/118136635-49db9a00-b43f-11eb-86bc-4c4928a20809.jpg)
---
### Version #2-var
기존에는 컨트롤러에서 직접 database에 정보를 push하는 방식을 생각해냈지만, 컨트롤러의 부하를 최소한으로 줄이기 위해 bagmaker를 추가로 도입하였다.
![menuaddVar](https://user-images.githubusercontent.com/29910793/118141783-b73df980-b444-11eb-9f7e-1408b9d533ce.jpg)

## UC8 sequence diagram
### Early version
<img width="1757" alt="UC8_sequence diagram" src="https://user-images.githubusercontent.com/29854638/117999888-43d2b400-b380-11eb-947d-0e08146b15b4.png">

## UC9 sequence diagram
### Early version
<img width="959" alt="UC9_sequence diagram" src="https://user-images.githubusercontent.com/29854638/117999897-46cda480-b380-11eb-9d4e-7b181dd384df.png">
**UC8 & UC9 sequence diagram 초기설계 issue**
기존 domain model은 사용자가 장바구니 페이지로 이동한 상태라고 가정하고 설계했다. sequence diagram을 그리면서 장바구니 페이지로 접속하는 과정이 생략되었음을 알았고, '장바구니 버튼' component를 추가하였다. 
---
### Version #2
![UC9](https://user-images.githubusercontent.com/29854638/118155629-61bd1900-b453-11eb-8ae6-635c91e44304.JPG)


