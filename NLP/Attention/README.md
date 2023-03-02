## 🏷️ Seq2Seq Model
### Seq2Seq Model
* RNN 구조 중 many-to-many 구조에 해당
* 입력도 시퀀스, 출력도 시퀀스
* 입출력은 보통 단어 단위의 문장

<br>


* `Encoder`, 인코더 
  * 입력 문장을 읽는 RNN 모델
* `Decoder`, 디코더 
  * 출력 문장을 순차적으로 단어 하나하나씩 생성하는 RNN 모델
* 서로 파라미터를 공유하지 않음
* 인코더의 마지막 time step의 hidden state vetor는 디코더에 첫 time step의 입력
* 인코더에서 수집한 정보를 잘 저장하여 디코더에 전달, 디코더는 전달 받은 정보를 바탕으로 단어를 예측하고 순차적으로 출력함으로써 대응
* 생성 task에서 디코더 모델에 넣어주는 첫 단어를 `Start Token`, `SoS(Start of Sentence Token)`라고 함
* `Start Token`들을 단어장에 정의해두고 디코더에 입력값으로 넣어줌으로써 첫 출력 단어 예측
* 마지막에 `EoS(End of Sentence Token)`이 생성되면 문장 생성을 종료에서 결과를 생성할 때 인코더의 몇 번째 time step에 더 집중할지 스코어 형태로 표현
* 각 디코더의 tiem step마다 인코더


<br>

## 🏷️ Attention
### Seq2Seq Model의 문제점
* RNN 기반의 모델 구조의 hidden state vector의 dimension이 정해져 있음
* 이 특성으로 인해 마지막 time step의 고정된 차원의 vector에 전체 시퀀스 정보를 압축하여 저장
* 아무리 LSTM이 long term dependency를 해결했다 하더라도 멀리 있는 정보는 변질, 소실
* 이 문제를 보완하기 위해 등장

<br>

### Attention 동작 원리 (1)
* `Seq2Seq Model`의 디코더는 인코더의 마지막 time step의 hidden state vetor에만 의존
* `Attention`에서 인코더는 모든 time step의 hidden state vetor를 디코더에 제공
* 디코더에서 각 time step에서 단어를 생성할 때 필요한 인코더의 hidden state vector를 선별하여 예측에 활용

<br>

* 디코더가 각 time step에서 결과를 생성할 때 인코더의 몇 번째 time step에 더 집중할지 스코어 형태로 표현
* 각 디코더의 time step마다 인코더의 hidden state vector와의 유사도 계산
* 인코더의 몇 번째 time step의 정보다 더 필요한지 파악

<br>

### Attention 동작 원리 (2)
* `Seq2Seq Model`의 경우 이전 hidden state vector와 현재 time step의 입력 값으로 디코더의 hidden state vector 계산
* `Attention`의 경우
  * 현재 step의 디코더 hidden state vector와 인코더 각각의 step hidden state vector를 내적해서 `Attention scores`(내적 기반 유사도)를 구함
  * `Attention scores`를 소프트맥수 함수를 통과시켜 유사도에 대응하는 확률 값 계산
  * 구해진 확률들을 인코더 각각의 hidden state vector에 부여다는 가중치로 사용하여 가중 평균인 `Attention output`이라는 하나의 벡터를 구함
  * 마지막 아웃풋 레이어에 디코더 time step의 hidden state vector와 `Attention output`을 concat해서 입력



<br>

## 🏷️ Teacher Forcing
### Teacher Forcing이란?
* 디코더의 다음 time step에 입력 값으로, 이전 time step의 결과 값이 아닌 정답 값을 넣어 학습하는 형태
* 예를 들어, i love you를 예측할 때
  * `<SOS>`를 입력 받은 첫 time step이 i를 예측, 출력하고 i에 대한 정보를 다음 time step에 넘겨주면 상관 없지만
  * 만약 다른 단어를 예측하고 넘겨준다면 모든 time step이 꼬이게 됨
  * 이를 방지하기 위해 이전 타임 스텝의 예측 값이 아닌 정답 값 `i`에 대한 벡터를 다음 time step에 전달


<br>

### 장점
* 디코더에서 추론(inference) 할 때, 틀린 값이 입력 값으로 들어가지 않으므로 빠른 학습 가능

<br>

### 단점
* train 데이터로 학습할 때와 test 데이터로 학습할 때 환경이 다름

> * 그래서 Teacher Forcing을 적절히 섞어 사용
> * 모델 학습 초반에는 Teacher Forcing을 통해 학습
> * 이후 어느 정도 모델의 예측 정확도가 올라오면 정답 값이 아닌 예측 값을 전달하여 학습

<br>

## 🏷️ Attention Mechanisims
### 다양한 Attention Mechanisims
* 인코더의 각각의 step의 hsv와 유사도를 구할 때 사용하는 방법
* `Luong-dot`
  * 간단한 내적을 통해 유사도 측정
  * 학습 가능한 파라미터가 존재하지 않음 
* `Luong-general`
  * 유사도를 구하고자 하는 두 벡터 사이에, 학습 가능한 파라미터로 구성된 행렬 사용
* `Luong-concat`
  * 유사도를 구하고자 하는 두 벡터를 concat ➡️ $x$
  * concat한 벡터를 선형 변환
  * 선형 변환 벡터를 비선형성 후 다시 션형 변환
  * 선형변환($\tanh$(선형변환($x$)))



<br>

### Attention의 장점 
* 기계 번역에서의 성능 향상 
  * 각 디코더의 step마다 인코더의 어떤 step에 더 집중해야하는지 알려주기 때문
* 기존 Seq2Seq 구조에서는 인코더의 마지막 time step의 hsv를 통해 정보를 넘겼는데 여기서 병목 현상 발생
  * 어텐션은 정보를 한 번에 전달하는 것이 아니기 때문에 이 문제 해결
* RNN의 한계점인 오차역전파 과정에서 기울기 소실 문제를 해결
  * 역전파 과정에서 서로 멀리 있어도 여러 step을 거치는 것이 아니라 어텐션 구조를 통해 한 번에 역전파될 수 있기 때문


<br>

## 🏷️ 출력 값 생성 알고리즘
### 3가지 생성 기법
* `Greedy decoding`
  * 생성하는 현재 시점에 가장 좋은 것(스코어가 높은 것)을 생성하는 알고리즘
  * 가장 좋은 한 가지를 고려하기 때문에 예측을 잘못할 경우 정확도가 떨어짐
* `Exhaustive search`
  * 가능한 모든 경우의 수를 고려하여 생성하는 알고리즘
  * 너무 오래 걸림
* `Beam search`
  * 위 두 가지 기법의 중간에 있는 기법
  * 매 time step마다 k개의 경우의 수를 고려하여 생성
  * 생성 속도와 성능을 고려한 차선책
  * k : beam size라고 부르며, 대체로 5 ~ 10 사이의 값을 가짐
  * `EOS` 토큰을 예측할 때까지 예측 진행
  * `EOS`를 예측한 경로의 가설은 임시 메모리에 저장하고 나미저 경로 예측 진행
  * 예측 완료된 가설들 중 가장 스코어가 높은 가설을 생성
    * 다만 문장이 길수록 스코어가 낮아지기 때문에 time step의 개수로 스코어를 나눠 평균 값을 최종 스코어로 활용

<br>

## 🏷️ BLEU score
### Precision and Recall
* Precision, 정밀도
  * 맞은 단어의 수 / 예측한 문장의 길이
  * 키워드 검색을 했을 때 검색 결과 문서들이 얼마나 의도에 부합하는가
* Recall, 재현율 
  * 맞은 단어의 수 / 정답 문장의 길이
  * 키워드 검색을 했을 때 검색 결과 문서들이 키워드 문서집에서 얼마나 나왔는가
  * 소환율, 얼마나 정답에서 알맞게 소환했는가
* F-measure
  * Precision과 Recall의 조화평균
  * $\frac{precision * recall}{\frac{1}{2}(precision + recall)}$

<br>

### 3가지 평균
* 산술평균 : n개의 값을 더한 후, n으로 나눠준 값
* 기하평균 : n개의 값을 모두 곱한 값의 제곱근
* 조화평균 : 주어진 값들을 역수로 취하여 산술평균을 구한 뒤 역수를 취한 값
> 모든 경우에서 산술평균 >= 기하평균 >= 조화평균 의 값을 가짐

<br>

### BLEU score 특징
* `recall`이 아닌 `precision` 기반
* 번역에서 정답 문장의 몇 단어가 빠져도(재현율이 떨어져도) 문장의 의미가 유사할 수 있지만, 문장에 없는 단어가 오역되어 들어오면(정밀도가 떨어져면) 영향이 크기 때문
* 문장을 평가할 때 `n-gram`(보통 1~4)의 n값에 따라 문장을 나눠 정답 값과 얼마나 일치하는지 다각도 평가
* `n-gram` 평가 방식을 사용할 때, 단어들의 일치도가 높을지라도 정답 문장과 연속적으로 단어가 일치하지 않는다면 `BLEU score` 값이 0이 나올 수 있음

<br>

### BLEU score 구하는 방법
* n=1~4에 대한 각각의 `precision`의 `기하평균`을 구함
  * precision 값의 기하평균을 구하는 이유 : 좀 더 작은 값에 많은 가중치를 부여하여 평균 계산하기 위함
  * 조화평균의 경우 작은 값에 지나치게 가중치를 부여하기 때문에 사용하지 않음
* 문장의 길이가 짧은 경우를 보정하기 위해, `brevity penalty`를 적용하여 위에서 구한 기하평균과 곱함
* `brevity penalty`
  * reference 문장보다 짧은 문장을 예측했을 경우, 1 이하의 값을 곱해서 precision의 값을 낮게 보정

$$BLEU=\min(1, \frac{len\_of\_prediction}{len\_of\_reference})(\prod_{i=1}^4precision_i)^\frac{1}{4}$$