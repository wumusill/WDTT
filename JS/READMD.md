# ✅ JS
## 🐯 변수
### 변수 선언 : var
```js
var 변수 이름 = 할당 값;
```
* 문자와 숫자, 기호 $와 _만 사용
* 첫글자가 숫자가 될 수 없음
* 대소문자 구별, 예약어는 사용 불가능
* ex) var var 불가능

<br>

### 변수 선언 : const
```js
const 이름 = '구자현';
const 직업 = '억만장자';
```
* 원주율과 같이 고정된 값이나 앞으로 변하지 않을 값은 `const`를 사용하여 변수 선언
* 변수 재선언, 재할당 모두 불가능

<br>

### 변수 선언 : let
```js
let 주수 = '청주';
주소 = '서울';
```
* 변수 재선언 불가능
* 재할당 가능

<br>

### 변수의 타입
```js
// number
document.write(`typeof(5) : ${typeof(5)} <br>`)
document.write(`typeof(5.5) : ${typeof(5.5)} <br>`)

// string
document.write(`typeof('5') : ${typeof('5')} <br>`)
document.write(`typeof('jahyungu') : ${typeof('jahyungu')} <br>`)
document.write(`typeof('1' + 1) : ${typeof('1' + 1)} <br>`)

// string 11, js는 type이 다른 자료의 연산을 허용
document.write(`'1' + 1 : ${'1' + 1} <br>`) 

// undefined
document.write(`typeof(x) : ${typeof(x)} <br>`)
document.write(`typeof(undefined) : ${typeof(undefined)} <br>`)

// object
document.write(`typeof([1, 2, 3, 4]) : ${typeof([1, 2, 3, 4])} <br>`)
document.write(`typeof({'one':'하나', 'two':'둘'}) : ${typeof({'one':'하나', 'two':'둘'})} <br>`)

// number, NaN
document.write(`typeof('js' / 2) : ${typeof('js' / 2)} <br>`)
document.write(`typeof('jahyungu' / 2) : ${typeof('jahyungu' / 2)} <br>`)

// boolean
document.write(`typeof(true) : ${typeof(true)} <br>`)

// object : 값을 가지는 객체
// null : 아무것도 없는 것
// js에서 오류라고 인정했으나, 호환성을 위해 수정하지 않음
let test = null
document.write(`typeof(test) : ${typeof(test)} <br>`)
```

<br>

### 변수의 형변환
[참고 자료](https://ko.javascript.info/type-conversions) <br>
* `String()` : string 타입으로 변환
```js
let one = 1;
document.write(`<p> one + one : ${one + one} </p>`);
document.write(`<p> String(one) + String(one) : ${String(one) + String(one)} </p>`);
```

<br>

* `Number()` : number 타입으로 변경
```js
let one = '1';
document.write(`<p> one + one : ${one + one} </p>`);
document.write(`<p> Number(one) + Number(one) : ${Number(one) + Number(one)} </p>`);
```

<br>

* `Boolean()` : boolean 타입으로 변경
```js
// true
document.write(`<p> Boolean(1) : ${Boolean(1)} </p>`);
document.write(`<p> Boolean(' ') : ${Boolean(' ')} </p>`);
document.write(`<p> Boolean([]) : ${Boolean([])} </p>`);
document.write(`<p> Boolean([0]) : ${Boolean([0])} </p>`);
document.write(`<p> Boolean('0') : ${Boolean('0')} </p>`);
document.write(`<p> Boolean(-1) : ${Boolean(-1)} </p>`);

// false
document.write(`<p> Boolean(0) : ${Boolean(0)} </p>`);
document.write(`<p> Boolean('') : ${Boolean('')} </p>`);
```

<br>

## 🐯 연산
### 할당연산, 증강연산 
```js
var x, y, z;
x = 5;
y = 9;

// y값을 하나 증가 시키겠다는 코드, y=10
y++;
++y;

// x값을 하나 감소 시키겠다는 코드, x=4
x--;
--x;

// 기존의 변수의 값을 활용하여 재할당 하고싶을 경우
x += 2;
```

<br>

### template literal
```js
var 이름 = '구자현';
var 나이 = 10;

document.write('제 이름은 ' + 이름 + ' 제 나이는 ' + 나이 + '입니다.');
document.write(`제 이름은 ${이름}입니다. 제 나이는 ${나이} 입니다.`);
```
* python의 f-string과 같은 기능
* 작은 따옴표`'`가 아닌 backtick(`) 사용
* 중괄호 앞에 `$` 입력

<br>

### 비교연산
```js
var x, y, z;
x = 10;
y = 20;
z = '10';

document.write(x > y, '<br>');              // false
document.write(x < y, '<br>');              // true
document.write(x >= y, '<br>');             // false
document.write(x <= y, '<br>');             // true
document.write(`x == z : ${x==z} <br>`);    // true
document.write(`x === z : ${x===z} <br>`);  // false
document.write(`x != y : ${x!=y} <br>`);    // true
```
* 등호가 2개, `==`일 때는 type을 확인하지 않음
* 등호가 3개, `===`일 때는 type을 확인

<br>

### 논리연산
* `and`, `or`, `not`
* `and` = 곱
* `or` = 합
* `true` = 1
* `false` = 0
```js
// or 연산
document.write(`true || true : ${true || true} <br>`);
document.write(`true || false : ${true || false} <br>`);
document.write(`false || true : ${false || true} <br>`);
document.write(`false || false : ${false || false} <br>`);

// and 연산
document.write(`true && true : ${true && true} <br>`);
document.write(`true && false : ${true && false} <br>`);
document.write(`false && true : ${false && true} <br>`);
document.write(`false && false : ${false && false} <br>`);

// not 연산
document.write(`!true : ${!true} <br>`);
document.write(`!false : ${!false} <br>`);
```

<br>

## 🐯 함수
* `function`을 이용하여 함수 선언
* `return` 구문이 없으면 `return undefined`
```js
function circle(r){
    return r * r * 3.14
    }

document.write(circle(4))
```

<br>

### Arrow function
* 익명 함수
* python lambda와 유사 
* `함수이름 = (파라미터) => 연산;`
```js
let sumArrorFunction = (x, y) => x + y;
```

<br>

### 함수 표현식
* 함수 선언문은 함수를 어디서나 호출 가능
* 함수 표현식은 해당 표현식 이후에 호출 가능
```js
// 함수 선언문
function sum(x, y){
    return x + y;
}

// 함수 표현식
let sumXY = function(x, y){
    return x + y;
};
```

<br>

### 콜백 함수
```js
// 콜백 함수
function sum(x, y, z){
    z(x + y);
    return x + y;
}

function documentWrite(s){
    document.write('콜백 함수', s);
}

sum(100, 20, documentWrite)
```