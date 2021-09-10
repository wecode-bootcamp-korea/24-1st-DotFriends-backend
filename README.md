# DotFriends

---

## 1. 프로젝트 소개

---

- 라인캐릭터 커머스사이트인, 라인프렌즈 클론 프로젝트

- 총 기간은 2주였지만 frontend와 backend와의 통신에서 오류가 발생할 수 있고 멘토님들의 리뷰도 반영하기 위해 개발기간을 10일로 잡았습니다
- frontend 개발팀원들이 모여 react기반의 초기세팅을 진행했습니다

### 1.1. 사이트 컨셉

- 라인프렌즈 사이트 자체를 따라하기 보다는 재치있는 아이디어를 통해, Line 이 아니라 Dot Friends 로 이름을 정했습니다
- 코로나시대에 맞게 사람과 사람을 연결하는 Line이 아니라 개인 혼자 (Dot) 집에서 지낼 때 활용할 수 있는 상품을 판매하는 컨샙을 잡았습니다

### 1.2. 개발 기간 및 인원

#### 1.2.1. 개발기간

2021.08.30 - 2021.09.09

#### 1.2.2. 개발인원

- FrontEnd
  - 금보배, 박은정, 주철진
- BackEnd
  - 신우주, 김동준, 서동규

### 데모영상

## 2. 테크 스택 및 협업툴
---

### 2.1. 테크 스택

#### Frontend
html
scss
javascript
react

#### Backend
Django ```3.2.4```
django-cors-headers ```3.7.0```
mysqlclient ```2.0.3```
bcrypt ```3.2.0```
pyjwt ```2.1.0```
pymysql ```1.0.2```
python ```3.7```

### 2.2. 협업도구

Slack
Github
Trello

## 3. 구현기능
---
### Frontend

#### Leonard 주철진님

- `[Nav]` :
- `[Product List]` :

#### Sally 금보배님

- 라인프렌즈 사이트 컨샙 설정

#### Edward 박은정님

- 각각의 API데이터에 대한 (캐러셀)슬라이드
- header 배경이미지 변경될 때마다 scale 애니메이션효과구현
- Footer 레이아웃

### Backend
#### Boss 서동규님
- 
- 

#### Moon 신우주님
- 
- 

#### Brown 김동준님
- 
- 

## Reference

---

- 이 프로젝트는 [라인프렌즈샵](https://brand.naver.com/linefriends/?nt_source=emnet_google_sa&nt_medium=search&nt_detail=store&nt_keyword=%EB%9D%BC%EC%9D%B8%EC%8A%A4%ED%86%A0%EC%96%B4&gclid=CjwKCAjw4KyJBhAbEiwAaAQbE93SzYQM2APropv_Ed2sO5bOHfEYnNEbiFW2_WzL52GNw2gXiBwVtBoCZIQQAvD_BwE) 사이트를 참조하여 학습목적으로 만들었습니다
- 학습수준의 프로젝트로 만들었기 때문에 이 코드 및 데모영상을 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.


## 4. API
---
### 4.1. 사용자
#### 4.1.1 회원가입
##### url
```{base_url}/user/sign-up```
##### method
```POST```
##### body
email : ```이메일``` ```string```
password : ```비밀번호``` ```string```
address : ```주소``` ```string```
name : ```이름``` ```string```
check_password : ```비밀번호 확인``` ```string```
phone_number : ```휴대폰 번호``` ```string```

---
#### 4.1.2 로그인
##### url
```{base_url}/user/sign-in```
##### method
```POST```
##### headers
Authorization : ```토큰``` ```token```
##### body
email : ```이메일``` ```string```
password : ```패스워드``` ```string```




### 4.2. 상품
#### 4.2.1. 상품 리스트 조회
##### url
```{base_url}/product```
##### method 
```GET```
##### query parameters
option: ```옵션``` ```‘new’```, ```‘sale’```
order: ```정렬기준``` ```‘-id‘```, ```‘-popular‘```, ```‘-created_at‘```, ```‘-updated_at‘```
search: ```검색값``` ```string``` 
offset: ```조회 시작점``` ```int```
limit: ```조회 상품 개수``` ```int``` 
category: ```카테고리``` ```1,2,3,'new','sale'```

---
#### 4.2.2. 상품 상세 조회
##### url
```{base_url}/product/<int:product_id>```
##### method
```GET```

---
#### 4.2.3. 찜하기
##### url
```{base_url}/mainproduct/likes```
##### method
```POST```
##### headers
Authorization : ```토큰``` ```token```
##### body
isLiked : ```찜하기 여부``` ```True```,```False```


### 4.3. 장바구니
#### 4.3.1. 생성
##### url
```{base_url}/cart```
##### method
```POST```
##### headers
Authorization : ```토큰``` ```token```
##### body
product_id : ```상품 ID``` ```string```
quantity : ```상품 수량``` ```int```

---
#### 4.3.2. 조회
##### url
```{base_url}/cart```
##### method
```GET```
##### headers
Authorization : ```토큰``` ```token```

---
#### 4.3.3 수정
##### url
```{base_url}/cart/<int:product_id>```
##### method
```PATCH```
##### headers
Authorization : ```토큰``` ```token```
##### body
quantity : ```수량``` ```int```

---
#### 4.3.4 삭제
##### url
```{base_url}/cart?product_id=int...&product_id=int```
##### method
```DELETE```
##### headers
Authorization : ```토큰``` ```token```
