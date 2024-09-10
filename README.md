# Spartamarket-DRF-Project
백엔드 역할 수행 + Django REST Framework를 이용한 RESTful API
<br>
<br>
<br>
<br>
## Introduction of project
각 유저가 자신의 물건을 등록하고 탐색할 수 있는 웹사이트의 백엔드 부분을 Django REST Framework를 사용해
구현하고 Postman으로 관리
<br>
<br>
<br>
<br>
## Period of project
- 24.09.05 ~ 24.09.09
<br>
<br>
<br>
<br>

## Enviroment of development
- Visual Studio Code
- Django 4.2
- Djangorestframework 3.15.2
- Postman
<br>
<br>
<br>
<br>

## ERDiagram

<img width="694" alt="ERD" src="https://github.com/user-attachments/assets/211ac1a4-f3dc-41cd-8a58-b824de348d4d">
<br>
<br>
<br>

## 주요기능
- - **회원가입**
    - **Endpoint**: **`/api/accounts`**
    - **Method**: **`POST`**
    - **조건**: username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력하며 성별, 자기소개 생략 가능
    - **검증**: username과 이메일은 유일해야 하며, 이메일 중복 검증(선택 기능).
    - **구현**: 데이터 검증 후 저장.
    - **검증 추가사항**: 회원가입시 비밀번호의 확인을 위해 password와 password2가 일치하지 않을시 error 메세지 발생

    회원가입시 입력사항

    <img width="959" alt="회원가입1" src="https://github.com/user-attachments/assets/8b8c0d93-3a40-48b1-8711-e2ef9285022f">
    
    200
    
    <img width="944" alt="회원가입2" src="https://github.com/user-attachments/assets/366d970b-3b1c-4784-99b4-fb5827b9fd7b">
    
    400
    
    <img width="959" alt="회원가입3" src="https://github.com/user-attachments/assets/05992796-af21-43ef-bbf8-9f97d7120113">

- - **로그인**
    - **Endpoint**: **`/api/accounts/login`**
    - **Method**: **`POST`**
    - **조건**: 사용자명과 비밀번호 입력 필요.
    - **검증**: 사용자명과 비밀번호가 데이터베이스의 기록과 일치해야 함.
    - **구현**: 성공적인 로그인 시 토큰을 발급하고, 실패 시 적절한 에러 메시지를 반환.
    - **구현 추가사항**: fresh_token을 이용하여 access_token의 재발급

    로그인시 입력사항 및 200
    
    <img width="948" alt="로그인1" src="https://github.com/user-attachments/assets/36789299-34eb-4cb9-9e3b-52ba782ec753">
    
    400
    
    <img width="956" alt="로그인3" src="https://github.com/user-attachments/assets/5ec338fd-c13d-4059-8fda-332650934829">
    
    access_token의 재발급
    
    <img width="946" alt="로그인2" src="https://github.com/user-attachments/assets/1696ec1c-f93d-43e5-86f7-2f934af0a5ed">

- - **프로필 조회**
    - **Endpoint**: **`/api/accounts/<str:username>`**
    - **Method**: **`GET`**
    - **조건**: 로그인 상태 필요.
    - **검증**: 로그인 한 사용자만 프로필 조회 가능
    - **구현**: 로그인한 사용자의 정보를 JSON 형태로 반환.

    200
    
    <img width="955" alt="프로필조회" src="https://github.com/user-attachments/assets/ef5bacff-3042-49f2-81c4-eedff37d719d">
    
    404
    
    <img width="968" alt="프로필조회2" src="https://github.com/user-attachments/assets/716c0afb-cf64-41c6-9320-0609e00dafe2">
    
    401
    
    <img width="965" alt="프로필조회3" src="https://github.com/user-attachments/assets/63efccf4-4ed0-4380-a5c4-57fdaeec34c1">

- - **상품 등록**
    - **Endpoint**: **`/api/products`**
    - **Method**: **`POST`**
    - **조건**: 로그인 상태, 제목과 내용, 상품 이미지 입력 필요.
    - **구현**: 새 게시글 생성 및 데이터베이스 저장.
   
    200
    
    <img width="961" alt="상품등록1" src="https://github.com/user-attachments/assets/c5d4f8c9-fa4f-4497-923b-401ec1e08d7b">

    401
    
    <img width="955" alt="상품등록2" src="https://github.com/user-attachments/assets/bbc6814e-fe2f-40a1-9ae4-83ce8ac6b0c5">
   
- - **상품 목록 조회**
    - **Endpoint**: **`/api/products`**
    - **Method**: **`GET`**
    - **조건**: 로그인 상태 불필요.
    - **구현**: 모든 상품 목록 반환.

    200
    
    <img width="953" alt="상품목록조회" src="https://github.com/user-attachments/assets/dc314aa2-d3a9-42d3-9b8b-cd5300976337">

- - **상품 수정**
    - **Endpoint**: **`/api/products/<int:productId>`**
    - **Method**: **`PUT`**
    - **조건**: 로그인 상태, 수정 권한 있는 사용자(게시글 작성자)만 가능.
    - **검증**: 요청자가 게시글의 작성자와 일치하는지 확인.
    - **구현**: 입력된 정보로 기존 상품 정보를 업데이트.

    200
    
    <img width="957" alt="상품수정1" src="https://github.com/user-attachments/assets/4c5f32db-fada-42cd-9cfe-a72808343714">

    401
    
    <img width="960" alt="상품수정2" src="https://github.com/user-attachments/assets/d3a982d2-a8ef-4e2a-b15e-ab1ee278fd1d">

- - **상품 삭제**
    - **Endpoint**: **`/api/products/<int:productId>`**
    - **Method**: **`DELETE`**
    - **조건**: 로그인 상태, 삭제 권한 있는 사용자(게시글 작성자)만 가능.
    - **검증**: 요청자가 게시글의 작성자와 일치하는지 확인.
    - **구현**: 해당 상품을 데이터베이스에서 삭제.

    200
    
    <img width="958" alt="상품삭제1" src="https://github.com/user-attachments/assets/ac49d90c-15fb-4677-93d6-1030d4c3b731">

    401
    
    <img width="961" alt="상품삭제2" src="https://github.com/user-attachments/assets/569406ca-957d-44cb-b1df-fbd540faa783">

## 추가기능
- - **로그아웃**
    - **Endpoint**: **`/api/accounts/logout`**
    - **Method**: **`POST`**
    - **조건**: 로그인 상태 필요.
    - **구현**: 토큰 무효화로 로그아웃 처리 가능.

    200
    
    <img width="958" alt="로그아웃1" src="https://github.com/user-attachments/assets/09b4ece8-1ca7-4c19-a173-21d2a7124324">
    
    400
    
    <img width="952" alt="로그아웃2" src="https://github.com/user-attachments/assets/d31684df-37c3-4aec-9ddd-0106fa40e545">

- - **본인 정보 수정**
    - **Endpoint**: **`/api/accounts/<str:username>`**
    - **Method**: **`PUT`**
    - **조건**: 이메일, 이름, 닉네임, 생일 입력 필요하며, 성별, 자기소개 생략 가능
    - **검증**: 로그인 한 사용자만 본인 프로필 수정 가능. 수정된 이메일은 기존 다른 사용자의 이메일과 username은 중복되면 안 됨.
    - **구현**: 입력된 정보를 검증 후 데이터베이스를 업데이트.
   
    200
    
    <img width="954" alt="회원정보수정1" src="https://github.com/user-attachments/assets/dfc97040-1045-40ae-9a00-6fa6492dc7ea">

    401
    
    <img width="955" alt="회원정보수정2" src="https://github.com/user-attachments/assets/b938d912-64cc-425a-a51f-308044d86730">


- - **회원 탈퇴**
    - **Endpoint**: **`/api/accounts`**
    - **Method**: **`DELETE`**
    - **조건**: 로그인 상태, 비밀번호 재입력 필요.
    - **검증**: 입력된 비밀번호가 기존 비밀번호와 일치해야 함.
    - **구현**: 비밀번호 확인 후 계정 삭제.

    200
    
    <img width="956" alt="회원탈퇴1" src="https://github.com/user-attachments/assets/94f294e4-40fb-4381-9ce1-a3ddff6cc880">
    
    400
    
    <img width="960" alt="회원탈퇴2" src="https://github.com/user-attachments/assets/03b7d082-3d74-46c4-a679-b8344b13dd48">

    401
    
    <img width="958" alt="회원탈퇴3" src="https://github.com/user-attachments/assets/09def37b-161e-4570-a1a9-774566df1b8e">




    
    

