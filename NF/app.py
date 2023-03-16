from flask import Flask, render_template, request
# 데이터를 저장할 리스트
from collections import deque
# 모델과 관련 메소드를 사용하기 위한 import
from saved.model import *

app = Flask(__name__)

# 모델 가중치가 저장 경로 
PATH = '/Users/jahyeon_gu/WDTT/NF/saved'

# 모델 선언
model = transformer(
    vocab_size=VOCAB_SIZE,
    num_layers=NUM_LAYERS,
    dff=DFF,
    d_model=D_MODEL,
    num_heads=NUM_HEADS,
    dropout=DROPOUT)

# 저장된 가중치 모델에 입히기
model.load_weights(f'{PATH}/test_model')

# 메세지를 저장할 리스트
msgs = deque([], maxlen=5)

@app.route('/')
def base():
    # 홈화면을 갈때마다 메세지 저장된 리스트 클리어
    msgs.clear()
    return render_template('base.html')

@app.route('/chat', methods=['GET', "POST"])
def chat():
    # POST 요청 받았을 때 작동
    if request.method == "POST":
        # 폼에 입력된 메세지에 접근
        send = request.form.to_dict()["send"]
        # 입력된 메세지로 모델 답장 받기
        pred = predict(send)
        # 메세지와 예측값을 리스트에 저장
        msgs.append((send, pred))

        # render chat.html, 메세지가 저장된 리스트 함께 전달
        return render_template('chat.html', msgs=msgs)
    
    return render_template("chat.html")

if __name__ == '__main__':
    app.run()
