# **⚫️ DotFriends**

[![시연동영상](https://images.velog.io/images/sdk1926/post/ed163123-f7c1-4f44-91ef-76fe807dbb82/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-09-11%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2010.41.19.png)](https://youtu.be/T5bOgE7dzwk)

**🌄 이미지를 클릭하면 시연 영상을 시청하실 수 있습니다.**

---

## ⭐️ **프로젝트 소개**

- 라인프렌즈 커머스 사이트 라인프렌즈샵 클론 프로젝트

- 기획, 디자인 시간 단축을 위해 사이트의 디자인과 레이아웃만 참고해서 만들었습니다.

###  **🤔 기획 의도**

- 라인프렌즈 사이트 자체를 따라하기 보다는 재치있는 아이디어를 통해, Line 이 아니라 Dot Friends 로 이름을 정했습니다.

- 코로나시대에 맞게 사람과 사람을 연결하는 Line이 아니라 개인 혼자 (Dot) 집에서 지낼 때 활용할 수 있는 상품을 판매하는 컨셉을 잡았습니다

### **📆 개발 기간**

- 2021.08.30 - 2021.09.09

### **👨‍👩‍👦 개발 인원**

- **FrontEnd**
  - 금보배, 박은정, 주철진
- **BackEnd**
  - 신우주, 김동준, 서동규

## **🎬 시연 영상**
* [시연 영상 보러 가기](https://youtu.be/T5bOgE7dzwk)
---
## 🛠 **테크 스택**

### **Frontend**
* HTML
* CSS
* Javascript
* React

### **Backend**
* Python ```3.7```
* Django ```3.2```
* MYSQL ```5.7```

### **DevOps**
* AWS EC2
* AWS RDS

## **👩‍👩‍👧‍👦 협업 도구**

* Slack
* Github
* Trello

---
## **🚀 구현 기능**

### **Boss 서동규**
- 상품 리스트 조회 API 
- 상품 상세페이지 조회 API

### **Moon 신우주**
- 회원가입, 로그인 API
- 상품 검색 API
- 장바구니 생성 및 조회 API

### **Brown 김동준**
- 
- 
---



## **API 문서**

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

---
## Reference

- 이 프로젝트는 [라인프렌즈샵](https://brand.naver.com/linefriends/?nt_source=emnet_google_sa&nt_medium=search&nt_detail=store&nt_keyword=%EB%9D%BC%EC%9D%B8%EC%8A%A4%ED%86%A0%EC%96%B4&gclid=CjwKCAjw4KyJBhAbEiwAaAQbE93SzYQM2APropv_Ed2sO5bOHfEYnNEbiFW2_WzL52GNw2gXiBwVtBoCZIQQAvD_BwE) 사이트를 참조하여 학습목적으로 만들었습니다
- 학습수준의 프로젝트로 만들었기 때문에 이 코드 및 데모영상을 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다
- 이 프로젝트에서 사용하고 있는 사진 대부분은 위코드에서 구매한 것이므로 해당 프로젝트 외부인이 사용할 수 없습니다.
