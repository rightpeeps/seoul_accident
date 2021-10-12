import os
from flask import Flask, render_template, url_for, request, app
import pickle

app = Flask(__name__)
model = pickle.load(open('rf_model.pkl', 'rb'))

@app.route('/')
@app.route('/index/', methods=['POST','GET'])
def index():
    return render_template('index.html'), 200

@app.route('/result', methods=['POST','GET'])
def predict():
    if request.method == 'POST':
        with open('rf_model.pkl','rb') as f:
            model = pickle.load(f)
            #test = [[3.2,-1]]
            user_hightemp = float(request.form['hightemp'])
            user_lowtemp = float(request.form['lowtemp'])
            user_data = [[user_hightemp, user_lowtemp]]
            prediction = model.predict(user_data)
            output = (prediction[0])
            score = round(output - 132.2)
            if output > 132.2 :
                ans = "지금 온도의 서울은 4년간 평균보다 {}명 정도 부상자가 많을것으로 예측됩니다.".format(score)
                #bgcolor = 'orange'
            if output < 132.2 :
                abscore = abs(score)
                ans = "지금 온도의 서울은 4년간 평균보다 {}명 정도 부상자가 적을것으로 예측됩니다.".format(abscore)
                #bgcolor = 'lightgreen'
        return render_template('result.html', result="{}").format(ans), 200
    else:
        return render_template('result.html'), 200


#export FLASK_DEBUG=1
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)