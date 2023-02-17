부스트 코스 강의 : 자연어 처리의 모든 것, 
[링크](https://m.boostcourse.org/ai330/intro) <br>
위키독스 : 딥러닝을 이용한 자연어 처리 입문, 
[링크](https://wikidocs.net/book/2155) <br>

# ✅ 자연어 처리의 시작
## 🏷️ 자연어 처리 개요
### NLP 두 분야
* `NLU`, Natural Language Understanding : 인공지능이 글을 이해하는 과정
* `NLG`, Natural Language Generation : 인공지능이 적절한 글을 생성하는 과정 

<br>

### NLP 주요 tasks
* Low-level parsing
  * `Tokenization` : 문장을 단어 단위로 쪼개나가는 과정
  * `stemming` : 어근을 추출하는 과정
* Word and phrase level, 단어 및 구문 수준
  * NER, Named Entity Recognition : 단일 단어, 여러 단어로 이루어진 고유명사 인식 ex) 뉴욕 타임즈
  * POS, Part Of Speech tagging : 문장 내 언어들의 품사를 알아내는 과정
* Sentence level, 문장 수준
  * Sentiment analysis : 감정 분석
  * machine translation : 기계 번역
* Multi-sentence and paragraph level, 다수의 문장 및 문단 수준
  * Entailment prediction : 두 문장 간의 논리적인 내포, 모순관계 예측
  * question answering : 독해 기반 질의 응답
  * dialog systems : 대화를 수행할 수 있는 기술
  * summarization : 문서를 한 줄 요약하는 기술 

<br>

### Text Mining
* 특정 키워드의 빈도수 시간에 따라 분석
* 비슷한 키워드 그룹화, 문서 군집화
* 소셜 미디어의 키워드 분석

<br>

### 자연어 처리 발전 과정
* ML/DL 모델은 일반적으로 숫자로 이루어진 데이터가 입출력
* `Word-Embedding` : 텍스트 데이터를 단어 단위로 분리하고 특정한 차원의 벡터로 변환하는 것
* RNN 모델이 NLP 핵심 모델로 자리 잡음 ➡️ LSTM, GRU
* attention, Transformer 모델로 대체
  * 큰 성능 향상, 자연어 처리 외에도, 영상 처리, 시계열 예측, 신약 개발 등 다양한 분야에서 활용
  * task 마다 존재하던 특화된 모델을 하나로 통합

<br>

### BOW
* 딥러닝이 활용되기 이전 단어 및 문자를 숫자로 표현하는 방법
  * 문장 기반으로 단어장을 만듦
  * 각 단어에 대하여 원핫 벡터 생성
* 이를 활용한 문서 분류기 ➡️ 나이브 베이즈 분류기, Naive Bayes Classifier
  * 단어들이 등장 확률을 이용하여 문서의 카테고리 분류
  * 만약 훈련 데이터에 없는 단어가 테스트로 주어지면 확률은 무조건 0이 되므로 분류 불가능한 문제점
  * 이를 해결하기 위해 여러가지 regularzation 활용
* Word Embedding과 다른 점
  * 모든 단어 원핫 벡터간의 유클리드 거리 = $\sqrt{2}$
  * 모든 단어 원핫 벡터간의 코사인 유사도 = 0
  * 단어 의미 상관 없이 모두가 동일한 관계

<br>

## 🏷️ 자연어 처리와 벡터
### Word Embedding
* 각 단어들을 특정한 차원의 한 점, 벡터로 표현
* 비슷한 의미의 단어는 비슷한 좌표로 매핑

<br>

### Word2Vec
* 거리가 인접한 좌표의 단어는 의미가 비슷할 것이라는 가정
* 특정 단어의 주변 단어는 특정 단어와 관련성이 높은 단어 
* 주변에 등장하는 단어들을 통해 한 단어의 의미를 알 수 있다는 것에서 착안
* 학습 데이터를 기반으로 주변 단어를 확률 분포로 예측  
* 기계 번역, 감정 분석, image captioning에서 활용

<br>

### GloVe
* Word2Vec과의 차이점
  * 손실 함수의 차이
  * 각 입력, 출력 단어 쌍들에 대해 한 윈도우 내에서 총 몇 번 동시에 등장했는지 사전에 계산한 뒤 로그를 취함
  * 입력 워드의 임베딩 벡터와 출력 워드의 임베딩 벡터의 내적값이 최대한 가까워질 수 있도록 함
* `Word2Vec`에서는 특정한 단어 쌍이 자주 등장한 경우 자연스럽게 여러 번 학습됨으로써 두 워드 임베딩 벡터의 내적 값이 더 커지도록 함 
* `GloVe`에서는 단어 쌍들이 등장한 횟수를 미리 계산하고 로그를 취한 뒤, 두 워드 임베딩 벡터의 내적 값과 차이를 loss로 설정하고 학습을 진행
  * Word2Vec에 비해 중복된 계산을 줄여줄 수 있다는 장점
  * 더 빠르게 학습 진행
  * 보다 더 적은 데이터에서도 잘 동작
* 두 모델 모두 텍스트 데이터에 기반하여 워드 임베딩을 학습하는 알고리즘
