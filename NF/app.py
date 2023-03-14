from flask import Flask, render_template, request
from collections import deque
from saved.model import *

app = Flask(__name__)

# model = transformer(
#     vocab_size=VOCAB_SIZE,
#     num_layers=NUM_LAYERS,
#     dff=DFF,
#     d_model=D_MODEL,
#     num_heads=NUM_HEADS,
#     dropout=DROPOUT)

# model.load_weights("/Users/jahyeon_gu/WDTT/NF/saved/testmodel_w")

received = deque(maxlen=6)
send = deque(maxlen=5)

@app.route('/')
def base():
    received.clear()
    send.clear()
    received.append("안녕하세요! 반가워요!")
    return render_template('base.html')

@app.route('/chat', methods=['GET', "POST"])
def chat():
    if request.method == "POST":
        msg = request.form.values()
        send.append(msg)
        return render_template('chat.html', sends=list(send))
    return render_template("chat.html")

if __name__ == '__main__':
    app.run()
