# β JS
## π― λ³μ
### λ³μ μ μΈ : var
```js
var λ³μ μ΄λ¦ = ν λΉ κ°;
```
* λ¬Έμμ μ«μ, κΈ°νΈ $μ _λ§ μ¬μ©
* μ²«κΈμκ° μ«μκ° λ  μ μμ
* λμλ¬Έμ κ΅¬λ³, μμ½μ΄λ μ¬μ© λΆκ°λ₯
* ex) var var λΆκ°λ₯

<br>

### λ³μ μ μΈ : const
```js
const μ΄λ¦ = 'κ΅¬μν';
const μ§μ = 'μ΅λ§μ₯μ';
```
* μμ£Όμ¨κ³Ό κ°μ΄ κ³ μ λ κ°μ΄λ μμΌλ‘ λ³νμ§ μμ κ°μ `const`λ₯Ό μ¬μ©νμ¬ λ³μ μ μΈ
* λ³μ μ¬μ μΈ, μ¬ν λΉ λͺ¨λ λΆκ°λ₯

<br>

### λ³μ μ μΈ : let
```js
let μ£Όμ = 'μ²­μ£Ό';
μ£Όμ = 'μμΈ';
```
* λ³μ μ¬μ μΈ λΆκ°λ₯
* μ¬ν λΉ κ°λ₯

<br>

### λ³μμ νμ
```js
// number
document.write(`typeof(5) : ${typeof(5)} <br>`)
document.write(`typeof(5.5) : ${typeof(5.5)} <br>`)

// string
document.write(`typeof('5') : ${typeof('5')} <br>`)
document.write(`typeof('jahyungu') : ${typeof('jahyungu')} <br>`)
document.write(`typeof('1' + 1) : ${typeof('1' + 1)} <br>`)

// string 11, jsλ typeμ΄ λ€λ₯Έ μλ£μ μ°μ°μ νμ©
document.write(`'1' + 1 : ${'1' + 1} <br>`) 

// undefined
document.write(`typeof(x) : ${typeof(x)} <br>`)
document.write(`typeof(undefined) : ${typeof(undefined)} <br>`)

// object
document.write(`typeof([1, 2, 3, 4]) : ${typeof([1, 2, 3, 4])} <br>`)
document.write(`typeof({'one':'νλ', 'two':'λ'}) : ${typeof({'one':'νλ', 'two':'λ'})} <br>`)

// number, NaN
document.write(`typeof('js' / 2) : ${typeof('js' / 2)} <br>`)
document.write(`typeof('jahyungu' / 2) : ${typeof('jahyungu' / 2)} <br>`)

// boolean
document.write(`typeof(true) : ${typeof(true)} <br>`)

// object : κ°μ κ°μ§λ κ°μ²΄
// null : μλ¬΄κ²λ μλ κ²
// jsμμ μ€λ₯λΌκ³  μΈμ νμΌλ, νΈνμ±μ μν΄ μμ νμ§ μμ
let test = null
document.write(`typeof(test) : ${typeof(test)} <br>`)
```

<br>

### λ³μμ νλ³ν
[μ°Έκ³  μλ£](https://ko.javascript.info/type-conversions) <br>
* `String()` : string νμμΌλ‘ λ³ν
```js
let one = 1;
document.write(`<p> one + one : ${one + one} </p>`);
document.write(`<p> String(one) + String(one) : ${String(one) + String(one)} </p>`);
```

<br>

* `Number()` : number νμμΌλ‘ λ³κ²½
```js
let one = '1';
document.write(`<p> one + one : ${one + one} </p>`);
document.write(`<p> Number(one) + Number(one) : ${Number(one) + Number(one)} </p>`);
```

<br>

* `Boolean()` : boolean νμμΌλ‘ λ³κ²½
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

## π― μ°μ°
### ν λΉμ°μ°, μ¦κ°μ°μ° 
```js
var x, y, z;
x = 5;
y = 9;

// yκ°μ νλ μ¦κ° μν€κ² λ€λ μ½λ, y=10
y++;
++y;

// xκ°μ νλ κ°μ μν€κ² λ€λ μ½λ, x=4
x--;
--x;

// κΈ°μ‘΄μ λ³μμ κ°μ νμ©νμ¬ μ¬ν λΉ νκ³ μΆμ κ²½μ°
x += 2;
```

<br>

### template literal
```js
var μ΄λ¦ = 'κ΅¬μν';
var λμ΄ = 10;

document.write('μ  μ΄λ¦μ ' + μ΄λ¦ + ' μ  λμ΄λ ' + λμ΄ + 'μλλ€.');
document.write(`μ  μ΄λ¦μ ${μ΄λ¦}μλλ€. μ  λμ΄λ ${λμ΄} μλλ€.`);
```
* pythonμ f-stringκ³Ό κ°μ κΈ°λ₯
* μμ λ°μ΄ν`'`κ° μλ backtick(`) μ¬μ©
* μ€κ΄νΈ μμ `$` μλ ₯

<br>

### λΉκ΅μ°μ°
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
* λ±νΈκ° 2κ°, `==`μΌ λλ typeμ νμΈνμ§ μμ
* λ±νΈκ° 3κ°, `===`μΌ λλ typeμ νμΈ

<br>

### λΌλ¦¬μ°μ°
* `and`, `or`, `not`
* `and` = κ³±
* `or` = ν©
* `true` = 1
* `false` = 0
```js
// or μ°μ°
document.write(`true || true : ${true || true} <br>`);
document.write(`true || false : ${true || false} <br>`);
document.write(`false || true : ${false || true} <br>`);
document.write(`false || false : ${false || false} <br>`);

// and μ°μ°
document.write(`true && true : ${true && true} <br>`);
document.write(`true && false : ${true && false} <br>`);
document.write(`false && true : ${false && true} <br>`);
document.write(`false && false : ${false && false} <br>`);

// not μ°μ°
document.write(`!true : ${!true} <br>`);
document.write(`!false : ${!false} <br>`);
```

<br>

## π― ν¨μ
* `function`μ μ΄μ©νμ¬ ν¨μ μ μΈ
* `return` κ΅¬λ¬Έμ΄ μμΌλ©΄ `return undefined`
```js
function circle(r){
    return r * r * 3.14
    }

document.write(circle(4))
```

<br>

### Arrow function
* μ΅λͺ ν¨μ
* python lambdaμ μ μ¬ 
* `ν¨μμ΄λ¦ = (νλΌλ―Έν°) => μ°μ°;`
```js
let sumArrorFunction = (x, y) => x + y;
```

<br>

### ν¨μ ννμ
* ν¨μ μ μΈλ¬Έμ ν¨μλ₯Ό μ΄λμλ νΈμΆ κ°λ₯
* ν¨μ ννμμ ν΄λΉ ννμ μ΄νμ νΈμΆ κ°λ₯
```js
// ν¨μ μ μΈλ¬Έ
function sum(x, y){
    return x + y;
}

// ν¨μ ννμ
let sumXY = function(x, y){
    return x + y;
};
```

<br>

### μ½λ°± ν¨μ
```js
// μ½λ°± ν¨μ
function sum(x, y, z){
    z(x + y);
    return x + y;
}

function documentWrite(s){
    document.write('μ½λ°± ν¨μ', s);
}

sum(100, 20, documentWrite)
```

<br>

## π― μ μ΄λ¬Έ
### if
```js
let score = 89;
let money = 1000;

if(score > 90){
    document.write('μ°Έ μνμ΅λλ€! <br>');
    money += 100000
} else if (score > 80){
    document.write('μνμ΅λλ€! <br>');
    money += 10000
} else if (score > 70){
    document.write('νμ΅λλ€! <br>');
    money += 1000
} else{
    money = 0
}
```

<br>

### μΌν­μ°μ°μ
* python comprehensionκ³Ό μ μ¬
* ν μ€λ‘ μμ±νλ μ½λκ° κΈΈμ΄μ§λ©΄ `?`, `:` λ€μμ μ€ λ°κΏμ΄ μΌλ°μ 
```js
let x = 3;

x == 2? 
document.write('ifλ¬ΈμΌλ‘ μ€νλμμ΅λλ€.') :
document.write('elseλ¬ΈμΌλ‘ μ€νλμμ΅λλ€.')

// λ³μ μ μΈ
let result = x == 3 ? true : false;

document.write(result)

// μ ifλ¬Έ κ΅¬ν
let score = 69;
let money = 1000;

score > 90 ? money += 100000 :
score > 80 ? money += 10000 :
score > 70 ? money += 1000 : money = 0
```

<br>

### Switch
* λ³μμ caseμ μλ£νμ΄ λ°λμ κ°μμΌ ν¨
* ifλ¬Έμ switchλ¬ΈμΌλ‘ λ³νν  μ μκ³  switchλ¬Έλ ifλ¬ΈμΌλ‘ λ³ν κ°λ₯
* λͺ©μ , μ©λμ λ§κ² μ¬μ©
```js
let num = 1;

switch (num) {
    case 0:
        document.write('0λ²μ§Έ caseμλλ€.')
        break;
    case 1:
        document.write('1λ²μ§Έ caseμλλ€.')
        break;
    case 2:
        document.write('2λ²μ§Έ caseμλλ€.')
        break;    
    default:
        break;
}

// μ¬λ¬ caseλ₯Ό νλλ‘ μ²λ¦¬νλ κ²λ κ°λ₯
let num = 1;

switch (num) {
    case 0:

    case 1:
        document.write('1λ²μ§Έ caseμλλ€.')
        break;
    case 2:
        document.write('2λ²μ§Έ caseμλλ€.')
        break;    
    default:
        break;
}

// μ΄λ° κ²λ κ°λ₯
switch (new Date().getDay()) {
    case 0:
        document.write('μΌμμΌμλλ€.')
        break;
    case 1:
        document.write('μμμΌμλλ€.')
        break;
    case 2:
        document.write('νμμΌμλλ€.')
        break;
    case 3:
        document.write('μμμΌμλλ€.')
        break;
    case 4:
        document.write('λͺ©μμΌμλλ€.')
        break;
    case 5:
        document.write('κΈμμΌμλλ€.')
        break;
    case 6:
        document.write('ν μμΌμλλ€.')
        break;
    default:
        break;
}
```


<br>

### for
```js
// 0~9κΉμ§ μΆλ ₯νλ κ΅¬λ¬Έ
for (var i = 0; i < 10; i++) {
    document.write(i, '<br>')
}

// 0~100μ ν©μ μΆλ ₯νλ κ΅¬λ¬Έ
let s = 0;
for (var i = 0; i < 101; i++) {
    s += i
}
document.write(s, '<br>')

// 0~100 μ€ μ§μλ§ ν©μ μΆλ ₯νλ κ΅¬λ¬Έ
let s = 0;
for (var i = 0; i < 101; i+=2) {
    s += i
}
document.write(s, '<br>')

// κ΅¬κ΅¬λ¨, μ΄μ€ forλ¬Έ
for (var i = 2; i < 10; i++) {
    for (var j = 1; j < 10; j++) {
        document.write(`${i} X ${j} = ${i*j} <br>`)
    }
}

// 100 μ΄νμ μμ°μ μ€ 3μ λ°°μμ 5μ λ°°μμ ν©
let s = 0
for (var i = 1; i < 101; i++) {
    if (i % 3 == 0) {
        s += i
    } else if (i % 5 == 0) {
        s += i
    }
}

let s = 0
for (var i = 1; i < 101; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
        s += i
    }
}
```

<br>

### forEach, for_in, for_of
```js
let array = [10, 20, 30, 40, 50];

array.forEach(e => console.log(e));

// for in, arrayμ indexλ₯Ό μν
for (var variable in array) {
    document.write(array[variable], '<br>');
}

// for of, arrayμ valueλ₯Ό μν
for (var variable of array) {
    document.write(variable, '<br>');
}
```

<br>

### while
```js
let num = 0;

// μ‘°κ±΄μ λ§μ λλ§ μ€ν
while (num < 11) {
    document.write(num, '<br>')
    num += 1;
}

// μ‘°κ±΄μ λ§μ§ μλλΌλ μ΅μν νλ²μ μ€ν
do {
    document.write(num, '!! <br>')
    num += 1;
} while (num < 11);
```
<br>

### break, continue
```js
let num = 0;

while (num < 11) {
    num++;
    if (num > 5){
        continue;
    }
    document.write(num, '<br>') 
}

let num = 0;

while (num < 11) {
    num++;
    if (num > 5){
        break;
    }
    document.write(num, '<br>') 
}
```

<br>

## π― Map, Set, this
### Map
* `object`μ μ μ¬
* `object`μ λ€λ₯Έ μ  : `key`κ°μΌλ‘ λ¬Έμκ° μλλΌ λ€λ₯Έ μλ£νλ€λ μ¬μ© κ°λ₯
```js
let m = new Map();

// mapμ μλ£λ₯Ό λ£λ μ½λ
// set(key, val)
m.set('νλ', '1');
m.set(1, 'νλ');
m.set(true, 1);
m.set(false, 0);

// keyμ λμνλ value μΆλ ₯νλ μ½λ
console.log(m.get('νλ'));
console.log(m.get(1));

// keyλ₯Ό κ°μ§κ³  μλμ§ νμΈ
console.log(m.has(true));

// μμλ₯Ό μ­μ νλ μ½λ
console.log(m.delete('νλ'));
console.log(m.has('νλ'));

// mκ³Ό mμ sizeλ₯Ό μΆλ ₯νλ μ½λ
console.log(m)
console.log(m.size)

// for of κ΅¬λ¬ΈμΌλ‘ map μν
for (var variable of m) {
    console.log(`mμ μννκ³  μμ΅λλ€. ${variable}`)
    // μΈλ±μ±λ κ°λ₯
    console.log(`mμ μννκ³  μμ΅λλ€. ${variable[0]}`)
}

// keyλ§ μΆλ ₯
m.keys()
// valueλ§ μΆλ ₯
m.values()
// items μΆλ ₯
m.entries()
```

<br>

### Set
* μ§ν© κΈ°λ₯
* μ€λ³΅μ νμ©νμ§ μμ
* `Map`κ³Ό λ©μλ μ μ¬
  * `delete()`
  * `has()`
  * `clear()`
```js
let s = new Set('abcde')
console.log(s)

// Setμ κΈΈμ΄ μΆλ ₯
console.log(s.size)

// Setμ μμ μΆκ°
s.add('f')
console.log(s)

// Set μν
for (var variable of s) {
    console.log(`sλ₯Ό μννκ³  μμ΅λλ€ ${variable}`)
}
```

<br>

### this
* python class self μ μ μ¬
* κ°μ²΄ μκΈ° μμ μ νμ©ν  λ μ¬μ©
```js
let νΈν = [{
    'μ΄λ¦': 'νλνΈν',
    'μμΉ': 'μ μ£Όλ μ μ£Όμ 00',
    'κ°κ²©': {'A':50000, 'B':30000, 'C':15000},
    'λ°©μκ°μ': 50,
    'μμ½μμ' : 25,
    'λ¨μλ°©μκ°μ' : function(){return this.λ°©μκ°μ - this.μμ½μμ}
}, {
    'μ΄λ¦': 'λνΈν',
    'μμΉ': 'μ μ£Όλ μ μ£Όμ 01',
    'κ°κ²©': {'A':10000, 'B':60000, 'C':30000},
    'λ°©μκ°μ': 100,
    'μμ½μμ' : 30,
    'λ¨μλ°©μκ°μ' : function(){return this.λ°©μκ°μ - this.μμ½μμ}
}, {
    'μ΄λ¦': 'μνΈν',
    'μμΉ': 'μ μ£Όλ μ μ£Όμ 02',
    'κ°κ²©': {'A':80000, 'B':50000, 'C':30000},
    'λ°©μκ°μ': 120,
    'μμ½μμ' : 80,
    'λ¨μλ°©μκ°μ' : function(){return this.λ°©μκ°μ - this.μμ½μμ}
}]

// ν¨μκΈ° λλ¬Έμ λ§μ§λ§μ () μΆκ°
console.log(νΈν[0]['λ¨μλ°©μκ°μ']())
console.log(νΈν[1]['λ¨μλ°©μκ°μ']())
console.log(νΈν[2]['λ¨μλ°©μκ°μ']())
```

<br>

## π― JSON
* HTML
  * λ§ν¬μ μΈμ΄
  * λ°μ΄ν°λ₯Ό μκ°ννλ κ°μ₯ κ°λ¨ν λ°©λ²
* CSS
  * HTMLμ μκ°μ μΈ ν¨κ³Όλ₯Ό μ£ΌκΈ° μν¨
* Javascript
  * μ¬κΈ°μλΆν° νλ‘κ·Έλλ° μΈμ΄
  * λ¨μ λ¬Έμ μμμμ μλͺμ λΆμ΄λ£λ μ΄λ€ νμλ₯Ό ν  μ μκ° ν΄μ£Όλ μΈμ΄
* XML
  * HTMLλ³΄λ€ λ³΄λ€ κ°κ²°νκ² λ°μ΄ν° νμ
  * λ°±μλ, νλ‘ νΈμλμ λ°μ΄ν°λ₯Ό μ μ‘ν  λ μ¬μ©
  * HTMLκ° λμΌνκ² ν΄μ κ°λ₯
* JSON
  * λ°±μλμμ JSONμΌλ‘ λ°μ΄ν°λ₯Ό μ μ‘ν΄μ£Όλ©΄ νλ‘ νΈμλμμ μλ°μ€ν¬λ¦½νΈλ‘ μ²λ¦¬
```js
// λ°μ λ°μ΄ν°λ₯Ό μλ°μ€ν¬λ¦½νΈκ° μ²λ¦¬ν  μ μλ κ°μ²΄λ‘ λ³ν
JSON.parse()

// λ°μ΄ν° μ μ²΄λ₯Ό νλμ λ¬Έμμ΄λ‘ λ³ννκ³  μΆμ λ μ¬μ©
// μλ°μ€ν¬λ¦½νΈ κ°μ²΄λ₯Ό λ€λ₯Έ μ νλ¦¬μΌμ΄μμΌλ‘ μ λ¬ κ°λ₯
JSON.stringify()

// μ λ μ½λλ₯Ό κΉμ λ³΅μ¬λ‘ νμ©
let l = [10, 20, 30];
let a = l;

// aλ₯Ό λ³κ²½νλ lλ λ³κ²½λ¨
a[0] = 1000;

// μλμ κ°μ΄ μ¬μ©
// λ©λͺ¨λ¦¬ ν¨μ¨μ΄ μ’μ§ μμ νμ€νΈν  λλ§ μ¬μ©
let l = [10, 20, 30];
let a = JSON.parse(JSON.stringify(l));

a[0] = 1000;

// this, functionμ νμ©νμ¬ κ΅¬νν μ°μ°μ mapμ νμ©ν΄ κ΅¬ν
console.log(νΈν.map(νΈν => ({
    'μ΄λ¦': 'μνΈν',
    'μμΉ': 'μ μ£Όλ μ μ£Όμ 02',
    'κ°κ²©': {'A':80000, 'B':50000, 'C':30000},
    'λ°©μκ°μ': 120,
    'μμ½μμ' : 80,
    'λ¨μλ°©μκ°μ' : νΈν.λ°©μκ°μ - νΈν.μμ½μμ
})));

let a = [5, 4, 10, 3, 2, 1];
// μ€λ¦μ°¨μ μ λ ¬
console.log(a.sort((a, b) => (a - b)));

// λ΄λ¦Όμ°¨μ μ λ ¬
console.log(a.sort((a, b) => (b - a)));
```