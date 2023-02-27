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
* 인코더의 마지막 timestep의 hidden state vetor는 디코더에 첫 timestep의 입력
* 인코더에서 수집한 정보를 잘 저장하여 디코더에 전달, 디코더는 전달 받은 정보를 바탕으로 단어를 예측하고 순차적으로 출력함으로써 대응
* 생성 task에서 디코더 모델에 넣어주는 첫 단어를 `Start Token`, `SoS(Start of Sentence Token)`라고 함
* `Start Token`들을 단어장에 정의해두고 디코더에 입력값으로 넣어줌으로써 첫 출력 단어 예측
* 마지막에 `EoS(End of Sentence Token)`이 생성되면 문장 생성을 종료


<br>

### Attention
* RNN 기반의 모델 구조의 hidden state vector의 dimension이 정해져 있음
* 이 특성으로 인해 마지막 timestep의 고정된 차원의 vector에 전체 시퀀스 정보를 압축하여 저장
* 아무리 LSTM이 long term dependency를 해결했다 하더라도 멀리 있는 정보는 변질, 소실
* 이 문제를 보완하기 위해 등장

<br>

### Attention 동작 원리
* 디코더는 인코더의 마지막 timestep의 hidden state vetor에만 의존
* `Attention`에서 인코더는 모든 timestep의 hidden state vetor를 디코더에 제공
* 디코더에서 각 timestep에서 단어를 생성할 때 필요한 인코더의 hidden state vector를 선별하여 예측에 활용





