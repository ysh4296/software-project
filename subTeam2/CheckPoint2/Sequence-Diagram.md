## Sequence Diagram
## UC1 Login
### Version #1
![login](https://user-images.githubusercontent.com/29909322/118359738-e2008d00-b5bf-11eb-8bcf-5af59295c964.jpg)
---
### Version #2
![login2](https://user-images.githubusercontent.com/29909322/118360178-7e775f00-b5c1-11eb-8857-7b1b98abf27d.png)

- Version1 에서는 Controller에서 직접 입력된 유저 정보를 DB의 정보와 비교하였다.
- Version2 에서는 위 기능을 Controller와 분리하여 Authenticator라는 클래스를 통해 수행한다.
- 분리를 통해 다른 부분에서 authenticate가 필요한 경우 가져다 쓸 수 있는 확장성을 얻었다.

## UC2 Add_User
### Version #1
![signup](https://user-images.githubusercontent.com/29909322/118359735-df9e3300-b5bf-11eb-977a-3bd5028c084b.jpg)

## UC3 Edit_User
### Version #1
![edit](https://user-images.githubusercontent.com/29909322/118359743-e5941400-b5bf-11eb-90e0-a2fd62caa27f.jpg)

## UC4 Logout
### Version #1
![logout](https://user-images.githubusercontent.com/29909322/118359742-e462e700-b5bf-11eb-85da-4e68676b7ba6.jpg)
