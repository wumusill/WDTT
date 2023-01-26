# ✅ HTML, CSS
## 웹의 동작 방식
1️⃣ 브라우저에 도메인 입력 `ex) www.google.com`
2️⃣ 브라우저가 DNS 에서 도메인과 매칭되는 IP 를 가져옴
   > DNS 란?
   * 
3️⃣ `Request` : 브라우저가 인터넷을 통해 IP 를 이용해 구글 서버에 접속
4️⃣ `Response` : 구글 서버에서 html 코드를 받아옴
5️⃣ 브라우저가 받아온 파일을 해석

## terminal 에서 구글 IP 조회
```
>>> nslookup www.google.com

Non-authoritative answer:
Name:	www.google.com      # 구글 도메인
Address: 142.250.207.36     # 구글 IP
```