# ✅ HTML, CSS
## 🕸️ 웹의 동작 방식
1️⃣ 브라우저에 도메인 입력 `ex) www.google.com` <br>
2️⃣ 브라우저가 DNS 에서 도메인과 매칭되는 IP 를 가져옴
> DNS 란?
   * Domain Name System
   * 호스트의 도메인 이름을 네트워크 주소로 바꾸거나 그 반대의 변환을 수행할 수 있도록 개발
   * 도메인을 IP 주소로 변환하고 라우팅 정보를 제공하는 분산형 데이터베이스 시스템

3️⃣ `Request` : 브라우저가 인터넷을 통해 IP 를 이용해 구글 서버에 접속 <br>
4️⃣ `Response` : 구글 서버에서 html 코드를 받아옴 <br>
5️⃣ 브라우저가 받아온 파일을 해석

<br>

## terminal 에서 구글 IP 조회
```
>>> nslookup www.google.com

Non-authoritative answer:
Name:	www.google.com      # 구글 도메인
Address: 142.250.207.36     # 구글 IP
```

<br>

## 🏷️ 글자 태그
### `<br>` 
* html은 텍스트를 enter 로 분리해도 연속된 여백(공간)을 다 병합 
* enter를 친 것 같이 텍스트를 분리하고 싶다면 `<br>` 태그 활용
### `<hr>`
* `<br>` + 실선 추가
### `<a>` 
* 클릭하면 지정된 링크로 이동, 같은 경로에 있는 파일의 이름을 지정하면 해당 파일 다운로드
### `<strong>`, `<b>`
* 텍스트 bold 처리, 강조 효과
> * html5 에서는 `<strong>` 권장 
> * 시각 장애인들을 위한 음성 지원 시 `<strong>`이 음성 강조 의미를 가지기 때문
> * `<b>` 는 html5 이전에 사용되던 태그

### `<em>`, `<i>`
* 텍스트 italic 처리
> * `<em>` 태그 권장
> * `<i>` 는 html5 이전에 사용되던 태그


### `<mark>`
* 하이라이트, 형광펜 같은 효과
### `<sub>`
* 아래첨자
### `<sup>`
* 위첨자

<br>

## 🏷️ 콘텐츠 그룹 태그
### `<ol>`
* order list
* 순서가 있는 내용을 출력할 때 사용 
* `<ol type="i" or "I">` : 로마자
* `<ol type="a" or "A">` : 알파벳


### `<ul>`
* unorder list
* 순서가 없는 내용을 출력할 때 사용
* 웹 상단에 메뉴를 표현할 때 자주 사용


### `<dl>`, `<dt>`, `<dd>`
* `<dl>` : definition list
* `<dt>` : definition term, 정의할 용어
* `<dd>` : definition description, 용어를 설명하는 태그, 들여쓰기 처리 됨
> * 태그를 용도에 맞게 사용하지 않으면 검색 엔진이 신뢰하지 않음


### `<div>`
* 여러 태그, 내용들을 묶어주는 태그


<br>

## 🏷️ 미디어 태그
### img
* `<img src="이미지 링크" alt="이미지가 출력되지 않을 때 출력할 대체 문구">`

### audio
* `<audio src="">`

### video
* `<video src="">`

> * 최근 audio, video 태그를 사용하기 보다는 동영상의 소스코드를 불러와서 사용
> * 서버에다가 저장해두고 사용하면 네트워크 부하 & 용량 차지

<br>

## 🏷️ form
### input
* `<input type="text">`
* `<input type="password">`
  * 복사 불가능
* `<input type="date">`
* `<input type="time">`
* `<input type="range">`
* `<input type="color">`
* `<input type="radio">`
  * 중복 불가능한 선택에서 사용
  * ex) 당신의 성별은?
* `<input type="checkbox">`
  * 중복 가능한 선택에서 사용
  * ex) 선호하는 언어는?
* `<input type="file">`

### textarea
* 장문의 여러 줄의 데이터를 입력 받을 떄 사용

<br>

## 🏷️ table
```html
<table width="100%" height="200px">
   <!-- table row1 -->
   <tr> 
      <!-- table head -->
      <!-- 데이터 가운데 정렬 + bold -->
      <th>구분</th>
      <th>이름</th>
      <th>판매량</th>
   </tr>
   <!-- table row2 -->
   <tr>
      <!-- table data -->
      <td>1</td>
      <td>해리포터</td>
      <td>100</td>   
   </tr>
   <!-- table row3 -->
   <tr>
      <td>2</td>
      <td>아바타</td>
      <td>200</td>
   </tr>
   <tr>
      <!-- 2개의 column을 병합 -->
      <td colspan="2">총 판매량</td>
      <td>300</td>
   </tr>
</table>
```

<br>

## ⚜️ CSS
### 1️⃣ HTML 문서 내부 CSS
* `<style>` 태그를 이용하여 `<head>` 안에 정의
```html
<head>
    <style>
        h1{color:red;}
    </style>
</head>
```

### 2️⃣ 외부 CSS
* `<link rel="stylesheet" href="css 파일 경로">` 를 `<head>` 안에 정의
```html
<head>
   <link rel="stylesheet" href="005.css">
</head>

<!-- 두 가지가 동시에 쓰면 아래에 있는 코드로 적용 -->
<!-- 내부 style 스타일 적용 -->
<head>
   <link rel="stylesheet" href="005.css">
   <style>
        h1{color:red;}
    </style>
</head>

<!-- 외부 css 파일 스타일 적용-->
<head>
   <style>
        h1{color:red;}
    </style>
   <link rel="stylesheet" href="005.css">
</head>
```
### 3️⃣ 태그 속성을 이용
```html
<h2 style="color: blue;">blue</h2>
```

### 4️⃣ id, class
* 같은 태그지만 각기 다른 스타일을 적용하고 싶을 때 사용
* `id`의 경우 같은 페이지에서 고유값이어야 함
* `id`에 style을 지정할 때는 `#id{}` 로 정의
```html
<style>
   #one{
      color:red;
   }
</style>
<h1 id="one">hello</h1>
<h1 id="two">hello</h1>
```
* `class`는 스타일 중첩 가능
* `class`에 style을 지정할 때는 `.class{}` 로 정의
```html
<style>
   .one{
      color:red;
   }
   .two{
      font-size:20px;
   }
</style>
<h1 class="one two">hello</h1>
<h1 class="two">hello</h1>
```

### 5️⃣ (고정, 가변) 크기 단위
* 고정 크기 단위
  * 기준점에 상관없이 고정되는 단위
  * px, pt, in, cm, mm
* 가변 크기 단위
  * 기준점에 따라 크기가 바뀌는 단위
  * em, %, rem, vw
  * 5em = 500%

### 6️⃣ margin, padding
* margin
  * border를 기준으로 바깥에 있는 여백
* padding
  * border를 기준으로 내부에 있는 여백
```html
<style>
   h2{
      border: 1px solid black;
      <!-- 상 우 하 좌 (시계 방향) -->
      padding: 20px 2px 10px 30px;
      margin: 60px;
   }
</style>
```


### 7️⃣ 색상
* `opacity`
  * 색상 불투명도 조정
  * .class{opacity:0.5;}
* `color`
  * #blue, #red
  * #000000 ~ #ffffff : 6자리 중 앞에서 두자리씩 R, G, B 값

<br>

## 🐰 HTML5 주요 아웃라인 엘리먼트
### 1️⃣ `<article>`
* 다른 곳에 단독으로 사용이 가능한 내용을 담는 엘리먼트
* 다른 곳에 퍼갔을 때 어색하지 않은 내용
* 잡지의 기사, 게시글, 댓글, 위젯 등
* 중첩해서 사용할 경우 하위 article들은 상위 article에 관련된 내용임을 의미
### 2️⃣ `<section>`
* 문서에서 일반적인 섹션의 의미
* 하나의 주제로 그룹화된 컨텐츠
* 각 섹션의 주제는 일반적으로 섹션 요소의 하위 항목으로 제목을 포함시켜 식별
> article vs section
> * 사람마다 문서 구조를 다르게 판단해서 사용하기 때문에 정답은 없음
> * article 안에 여러 section이 있기도 하고 section 안에 여러 article이 있기도 함
### 3️⃣ `<header>`
* Sectioning content : 헤딩과 풋터의 범위, article, aside, nav, section이 해당
* Sectioning content의 헤더
* 일반적으로 헤딩 엘리먼트를 포함하지만 반드시 그럴 필요는 없음
* 헤딩 없이 목차, 검색폼 같은 내용을 header로 감싸도 무방
### 4️⃣ `<footer>`
* Sectioning content의 풋터
* 순서상 반드시 Sectioning content의 끝에 위치할 필요는 없음
### 5️⃣ `<nav>`
* navigation
* 링크의 묶음
* 모든 링크 묶음에 사용할 필요는 없음
* 일반적으로 메인 네비게이션 역할의 링크 묶음에 사용
### 6️⃣ `<aside>`
* 페이지의 주요 내용의 흐름과 관련없는 다른 내용
* 사이드바 형탵의 디자인으로 자주 표현
* 각주에는 aside를 사용하지 않음
### 7️⃣ `<h1> ... <h6>`
* Sectioning content의 제목
* 서브타이틀로는 사용하면 안됨
* 비록 `<h2>` 더라도 제목 태그는 그 단락의 대장이어야 함

<br>

## 🐰 reset css
* css 가 연결되어 있지 않은 html 코드를 웹에 출력해보면 제목은 굵고 큰 텍스트, 문단 사이에는 한 줄 공백 등 기본 스타일을 적용해서 보여줌
* 하지만 디자인할 때는 이런 기본 스타일이 방해
* 기본 스타일을 모두 없애주고 백지에서 디자인을 시작하기 위해 사용하는 css
* 보통 회사마다, 개발자 마다 각자의 reset css를 가지고 있음

<br>

## 🐰 display : inline vs block, inline-block
### inline
* 입력된 텍스트만큼의 영역 차지
* `class{display: inline;}`
* p 태그의 경우 기본값
### block
* 부모 content의 폭만큼 영역 차지
* width 값을 조정해줄 필요가 없음
* `class{display: block;}`
* div 태그의 경우 기본값
* 상단의 주요 아웃라인 엘리먼트 기본값
### inline-block
* inline 처럼 수평으로 배치
* block 처럼 width, height 설정 가능
  * inline 은 width, height 조정 불가능
* rem
  * root em
  * html 의 최상위 엘리먼트의 폰트 사이즈
  * 특별하게 설정 되어있지 않다면 모든 브라우저는 16px 로 정해져 있음
```css
.class{
   /* 사이즈가 다른 두 인라인 요소를 위로 맞추는 방법 */
    vertical-align: top;

    /* css3 부터 지원하는 기능 */
    width: calc(30% - 2em);
```

<br>

## 🐰 float
[참고 자료](https://ofcourse.kr/css-course/float-%EC%86%8D%EC%84%B1)
* left
  * 왼쪽에 떠다니는 블록 박스 생성
  * 페이지 내용은 박스 오른쪾에 위치하여 위에서 아래로 흐름
* right
  * 오른쪽에 부유하는 블록 박스를 생성
  * 페이지 내용은 왼쪽에 위치하며 위에서 아래로 흐름
```css
.class{
   float: left;
}
```


* html 태그 맨 마지막에 위치하는 가상 엘리먼트 만드는 방법
```css
.class:after{
    content: '';
    clear: left;
    display: block;
    height: 0;
    visibility: hidden;
}
```

<br>

## 🐰 flexbox
[참고 자료](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox)
* 인터페이스 내의 아이템 공간 배분과 강력한 정렬 기능을 제공하기 위한 1차원 레이아웃 모델
* block 요소들을 inline 처럼 옆으로 보여주고 싶을 때 사용
* internet explorer 10 부터 지원
* 10의 경우 속성의 이름이 다름
* 10을 지원해야하는 프로그램이라면 따로 확인해야 함
```css
.class{
   /* 브라우저 높이의 50% 차지 */
   height: 80vh;
   background: gray;

   display: flex;
   /* 축의 방향 결정 */
   flex-direction: row;

   /* 메인 축에 내용물 정렬 방식 */
   /* flex-start, flex-end, center, space-between, space-around */
   justify-content: space-between;

   /* 메인 축의 수직 방향으로 내용물 정렬 방식 */
   /* stretch, flex-start, flex-end, center */
   align-items: stretch;

   /* 내용을 제외한 여백의 비율 */
   flex-grow: 1;
   /* 내용물을 포함한 비율 */
   flex-basis: 0;

   /* flex 값을 설정하면 flex-basis: 0 자동 설정 */
   flex: 1;
}
```

<br>

## 🐰 checkbox

```html
<label for="input-check">체크하세요</label>
<input type="checkbox" class="input-check" id="input-check">

<label for="input-check">
   체크하세요
   <input type="checkbox" class="input-check" id="input-check">
</label>
```
* label 의 for 속성과 input 의 id 속성이 같으면 label을 클릭해도 체크 가능

<br>

```css
/* class1 뒤에 나오는 class2 중 같은 항렬에만 해당하는 css */
.class1 ~ .class2 {
   background: #fff000;
}

/* class1 바로 뒤에 나오는 class2 이면서 같은 항렬에만 해당하는 css */
.class1 + .class2 {
   background: #fff000;
}


/* 체크박스에 체크가 됐을 경우 작동하는 css */
.class1:checked ~ .class2 {
   background: #fff000;
}
```

<br>

## 🐰 position
[참고 자료](https://developer.mozilla.org/ko/docs/Web/CSS/position)
```css
p {
   /* 기본값 static */
   position: sticky;
   top: 20px;

   /* 숫자가 높을수록 위로 z축 상단에 위치 */
   z-index: 10;
}
```
* 문서 상에 요소를 배치하는 방법을 지정할 때 사용
* `absolute` : 절대 위치
* `relative` : 상대 위치
* `fixed` : 스크롤 상관 없이 위치 고정
* `sticky` : 스크롤로 지정된 위치에 가게되면 고정
* `absolute`, `relative`, `fixed`, `sticky` 등의 position은 `static` 보다 z축 상단에 위치
* position이 `static`이 아니면 늦게 나온 엘리먼트가 상단에 위치
* 순서를 지정해주고 싶다면 `z-index` 활용
  * 숫자가 높을수록 z축 상단 위치
* 부모 요소가 static(기본값)이라면
  * 자식 요소에 설정된 position에 따라 움직임
* 부모 요소가 static이 아니라면
  * 자식 요소에 position을 설정했더라도 부모 영역을 따라가고 부모 영역 안에서 position 결정