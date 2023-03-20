from  flask import Flask,request,jsonify,render_template
import numpy as np
import pickle



app = Flask(__name__)
model = pickle.load(open('model.bin','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/boston',methods=['POST'])
def prediction():
    data = [int(x) for x in request.form.values()]
    data =[np.array(data)]
    prediction = model.predict(data)
    out = round(prediction[0],2)
    return render_template('resultat.html',res='house price is {} $ '.format(out))

if __name__=='__main__':
    app.run(port=2000,debug=True)