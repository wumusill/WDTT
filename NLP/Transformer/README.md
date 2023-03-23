## 🏷️ Transformer
### Long-Term Dependency
* 앞선 타입 스텝의 정보가 뒤로 전달되면서 손실, 유실, 변질
* `bi-directional RNNs`, `Transformer` 두 가지로 해결 시도
* `bi-directional RNNs`
  * forward와 backward 두 개의 RNN 생성
  * 각 타입 스템의 히든 스테이트를 가져와서 concat ➡️ 2배의 차원 히든 스테이트
  * concat한 히든 스테이트를 이용하여 인코딩 결과 반환
  * 단일 RNN보다 먼 정보를 비교적 잘 반영하나 완벽하지 않음
* `Transformer`
  * 모델에 들어가는 입력과 출력의 세팅은 RNN과 동일
  * 주어진 Query에 대해 어느 Key와 유사도가 높은지 점수 계산
  * 점수에 소프트맥스를 취해 Value 벡터와 곱함
  * 이후 선형 결합을 거쳐 한 개의 아웃풋 벡터를 만들어 주는 것이 Transformer 알고리즘
  * 유사도만 높으면 거리가 멀더라도 정보를 알맞게 가져올 수 있음
  * 거리와 상관없이 작동

<br>

* Query 벡터
  * 현재 타입 스텝에 주어진 입력 벡터가 $W^q$에 의해 변환된 벡터
* Key 벡터
  *  재료 벡터, 유사도를 구하기 위해 Query 벡터와 각각 내적되는 벡터
* Value 벡터
  * 유사도를 구하고 소프트맥스를 취해 구한 각 가중치에 맞게 재료 벡터와 곱한 벡터

<br>

* 예시 문장 : I go home 
  * 디코더의 히든 스테이트 구하는 단계
  * I를 I, go, home 3개의 벡터와 내적을 하여 유사도 계산
  * 유사도를 소프트맥스를 취해 확률로 반환
  * 각 확률을 인코딩 벡터의 가중치하여 곱한 뒤 결과 벡터로 사용
  * 자기 자신에 대한 유사도가 다른 벡터 비해 훨씬 높음
  * 따라서 결과 벡터는 자기 자신 정보만을 주로 포함하는 한계

<br>

* Qery, Key, Value로 어텐션 스코어 구하는 방법
  * 인코딩된 단어에 대해 Query 벡터 구함
  * 각 Key에 대해 내적하여 스코어 구함
  * 스코어를 기존 벡터에 곱하고 선형 결합을 거쳐 한 개의 어텐션 벡터 구함

<br>

## 🏷️  Multi-Head Attention
* Query, Key, Value에 대해 각각 선형변환 후 Query vector에 대한 인코딩 벡터를 구함 
* 멀티헤드 어텐션을 통해 동시에 병렬적으로 여러 버전의 어텐션을 수행
* 어텐션 구조 각 버전의 결괏값을 concat하여 쿼리 벡터에 대한 최종 인코딩 벡터를 얻음
* 헤드가 8개일 때 어텐션 결과 벡터가 3이라면 최종 인코딩 벡터는 24차원
* 최종 인코딩 벡터를 다시 선형 변환하기 위해 $W$와 곱하여 원하는 차원의 벡터로 변환 

<br>

### Multi-Head Attention이 필요한 이유
* 같은 단어라도 다른 기준으로 여러 측면에서 정보를 가져와야 할 수도 있음
```
I went to the school
I studied hard
I came back home
I took a rest 
```
* I 에 다한 Query 벡터를 인코딩할 경우
* 주체의 행동(went, studied), 장소(school, home)에 해당하는 정보를 뽑을 수 있음

<br>

### RNN vs Attention
* RNN은 $d^2$, Attention은 $n^2$의 복잡도 ($d$ : 벡터의 차원, $n$ : 입력값의 길이)
* 벡터의 차원은 조절 가능한 하이퍼파라미터이나 입력값의 길이는 가변적
* 따라서 더 긴 문장을 사용하게 되면 계산량과 메모리 사이즈 증가
* 하지만 Attention은 GPU core만 충분하다면 모두 병렬처리 가능
* RNN 모델을 동작이 재귀적이기에 타입스텝이 진행되기를 기다릴 수 밖에 없음

