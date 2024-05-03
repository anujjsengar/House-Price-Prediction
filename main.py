from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
model = pickle.load(open('RidgeModel.pkl','rb'))
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    bhk=request.form.get('bhk')
    bath=request.form.get('bath')
    area=request.form.get('area')
    value=model.predict([[bhk,area,bath]])[0]
    value=value if value>0 else -1*value
    return str(value*100000)
if __name__=="__main__":
    app.run(debug=True,port=5001)