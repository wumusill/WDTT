# ✅ 자연어 처리와 딥러닝
## 🏷️ RNN, Recurrent Neural Network
### RNN
$h_t=f_W(h_{t-1}, x_t)$ <br>
* $h_{t-1}$ : 이전 은닉층의 벡터 
* $x_t$ : 입력 벡터
* $f_W$ : RNN function with parameters W
* $W$는 모든 타임스탭에서 동일한 값을 공유하는 것이 특징

<br>

$h_t=f_W(h_{t-1}, x_t)=tanh(W_{xh}x_t+W_{hh}h_{t-1})$ <br>
$y_t=W_{hy}h_t$ 

* $h$가 2차원, 입력 벡터 $x$가 3차원 이라면 $W$는 2 by 5 행렬
* $W$ 중 2by3은 입력 벡터와 연산 = $W_{xh}$
* 2by2는 이전 은닉층 벡터와 연산 = $W_{hh}$
* 비선형 근사를 위해 활성화 함수 통과

<br>

### Types of RNNS
* One-to-one
  * Standard NN
  * 키, 몸무게, 나이 등을 입력 받아 고혈압/저혈압을 분류

<br>

* One-to-many
  * Image Captioning ➡️ 하나의 이미지를 입력 받고 여러 카테고리 중 알맞게 분류
  * 입력이 첫 layer에만 존재 ➡️ 이후 layer에는 입력 데이터와 같은 사이즈의 0으로 이루어진 행렬 or 벡터 입력

<br>

* Many-to-one
  * Sentiment Classification ➡️ 여러 단어를 받아 감정 분석, Positive or Negative

<br>

* Many-to-many
  * Machine Translation
  * Video classification on frame level

<br>

## 🏷️ Character-level Language Model
### Language Model
* 주어진 문자열, 단어들의 순서를 바탕으로 다음 단어를 맞추는 task
* 같은 원리를 이용하여 코드 구현, 논문, 줄글 작성 가능

<br>

## 🏷️ LSTM, GRU
### LSTM
* Long Short-Term Memory
* 기울기 소실/증폭을 방지하고 필요한 정보를 학습할 수 있도록 하는 아이디어에서 시작

<br>

* RNN과 달리 이전 은닉층에서 두 가지의 벡터를 전달 받음 $=c_t, h_t$
* 모든 은닉층의 두 벡터 $(c_t, h_t)$ 를 개선하는 모델 
* $(c_t, h_t)=LSTM(x_t, c_{t-1}, h_{t-1})$
* $c_t$가 더 완전한 핵심 정보가 담긴 벡터
* $h_t$는 $c_t$를 한 번 더 가공, 필터링 후 해당 은닉층에 노출할 만한 정보를 담은 벡터

<br>

* input
* forget gate
  * 시그모이드 활용
  * 과거 정보($h_{t-1}$)를 얼마나 기억할지 결정
  * 시그모이드를 통해 0~1 사이 값을 곱함으로써 정보의 일부를 전달
  * 위 정보를 cell state에 update
* input gate
  * $tanh(W_c\cdot[h_{t-1}, x_t]+b_c)$
  * $tanh$ 함수로 -1과 1사이의 값을 가지는 현재 정보 + 시그모이드를 통해 계산된 과거 정보
  * 위 정보를 cell state에 update
  * 덧셈 연산으로 인해 기울기 소실 문제가 사라짐 ➡️ Gradient를 복사해주는 효과 ➡️ 더 멀리 전달 가능
* output gate
  * 시그모이드 활용
  * $o_t=\sigma(W_c\cdot[h_{t-1}, x_t]+b_o)$
  * $h_t=o_t\cdot tanh(C_t)$
  * 결과물을 예측하고 다음 은닉층으로 $h_t$ 전달
* $h_t$는 현재 타임스텝의 예측 값을 내기 위해 사용되는 벡터, $c_t$에서 필터링된 지금 당장 필요한 정보
* $c_t$는 기억해야할 모든 정보를 담고 있는 벡터


<br>

### GRU
* Gated Recurrent Unit
* LSTM에 비해 경량화, 적은 메모리 사용, 빠른 계산이 가능하도록 구현한 모델
* LSTM에 존재하는 두 가지 벡터 $(h_t, c_t)$ 를 $h_t$로 일원화
* 그러나 동작 원리는 굉장히 유사

<br>

* input gate 역할을 하는 $z_t$
* $z_t=\sigma(W_z\cdot[h_{t-1}, x_t])$
* forget gate 대신 $1-z_t$ 벡터 사용
* input gate가 커질수록 forget gate는 작아지는 구조


<br>

# ✅ 순환 신경망(Recurrent Neural Network)
[참고 자료](https://wikidocs.net/48558)
## 순환 신경망, RNN
* 입력과 출력을 시퀀스 단위로 처리하는 가장 기본적인 시퀀스 모델
* 은닉층의 노드에서 활성화 함수를 통해 나온 결과값을 츨력층 방향으로 보내면서, 다시 은닉층 노드의 다음 계산의 입력으로 보내는 특징
* 순환 신경망과 재귀 신경망은 전혀 다른 개념

<br>

## 양방향 순환 신경망
* Bidirectional Recurrent Neural Network
* RNN이 풀고자 하는 문제 중에서는 과거 시점의 입력 뿐만 아니라 미래 시점의 입력에 힌트가 있는 경우도 많음
* 그래서 이전과 이후의 시점 모두를 고려해서 현재 시점의 예측을 더욱 정확히 할 수 있도록 고안

<br>

## 장단기 메모리, LSTM
* 바닐라 RNN은 출력 결과가 이전의 계산 결과에 의존
* 바닐라 RNN은 비교적 짧은 시퀀스에 대해서만 효과를 보임
* `장기 의존성 문제(the problem of Long-Term Dependencies)`
  * 첫 입력값에 대한 정보가 뒤로 갈수록 손실
  * 가장 중요한 정보가 앞 쪽에 위치할 경우 뒤로 충분히 전달되지 않을 수 있음
  * 이러한 RNN의 단점을 보완한 것이 LSTM

<br>

* LSTM은 은닉층의 메모리 셀에 셀 상태(cell state)라는 값을 추가
* 입력, 망각, 출력 게이트를 추가
* 긴 시퀀스의 입력을 처리하는데 탁월한 성능

### 입력 게이트
* 현재 정보를 기억하기 위한 게이트
* $i_t=\sigma(W_{xi}x_t+W_{hi}h_{t-1}+b_i)$ ➡️ 0~1
* $g_t=\tanh(W_{xg}x_t+W_{hg}h_{t-1}+b_g)$ ➡️ -1~1
* 입력 게이트에서 선택된 기억 ➡️ $i_t\circ g_t$


<br>

### 삭제 게이트
* 기억을 삭제하기 위한 게이트
* $f_t=\sigma(W_{xf}x_t+W_{hf}h_{t-1}+b_f)$
* 현재 시점 $t$의 $x$값과 이전 시점 $t-1$의 hidden state가 시그모이드 함수를 통과 ➡️ 0~1 사이의 값 ➡️ 이 값이 삭제 과정을 거친 정보의 양
* 0에 가까울수록 정보가 많이 삭제
* 1에 가까울수록 이전 정보를 온전히 기억


<br>

### cell state
* $C_t=f_t\circ C_{t-1}+i_t\circ g_t$
* 삭제 게이트의 결과 + 입력 게이트에서 선택된 기억 ➡️ 현재 시점의 $t$ ➡️ 다음 $t+1$ 시점의 셀로 정보 전달

<br>

* $f_t$가 0이라면 $C_{t-1}$는 현재 timestep의 cell state를 결정하기 위한 영향력이 0
* $i_t$가 0이라면 $C_t$는 현재 timestep의 cell state를 결정하기 위한 영향력이 0
* 삭제 게이트는 이전 시점의 입력을 얼마나 반영할지 의미
* 입력 게이트는 현재 시점의 입력을 얼마나 반영할지 의미

<br>

### 츌력 게이트와 은닉 상태
* $o_t=\sigma(W_{xo}x_t+W_{ho}h_{t-1}+b_o)$
* $h_t=o_t\circ \tanh(c_t)$

<br>

* 출력 게이트 ➡️ 현재 시점 $t$의 $x$값, 이전 시점 $t-1$의 hidden state가 시그모이드 통과
* 현재 시점 $t$의 hidden state 결정
* cell state의 값이 하이퍼볼릭탄젠트 함수를 통과 ➡️ -1~1
* 출력 게이트의 값과 연산 후 값이 걸러지는 효과 발생하여 hidden state가 됨
* hidden state 값도 출력층으로 향함


<br>

## 게이트 순환 유닛, GRU
* 출력, 입력, 삭제 게이트가 존재하는 LSTM
* 반면 GRU는 업데이트 게이트와 리셋 게이트 두 가지 존재
* GRU는 LSTM보다 학습 속도가 빠르고 비슷한 성능을 보임

<br>

* 기존 LSTM을 사용하면서 최적의 하이퍼파라미터를 찾았다면 굳이 GRU로 바꿀 필요 없음 
* 보통 데이터의 양이 적을 때는 매개 변수의 양이 적은 GRU가 조금 더 나음
* 데이터 양이 많으면 LSTM이 조금 더 나음
