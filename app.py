from joblib import load
import numpy as np
from flask import Flask ,render_template,request
import pandas as pd

app = Flask(__name__)

ENV = 'prod'
if ENV == 'dev':
    app.debug=True
    
else:
    app.debug=False
    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        Name = request.form['Name']
        sex = request.form['sex']
        income = request.form['income']
        try:
            age = int(request.form['age'])
        except ValueError:
            age = -1
        married = request.form['married']
        if Name == "" or sex == "" or age>120 or age < 0:
            return render_template('index.html', message='Invalid Input')
        
        inp = np.array([sex,age,income,married]).reshape(1,-1)
        model = load("titanic_model.pkl")
        
        prediction = model.predict(inp)
        if prediction == 1:
            return render_template('success.html')
        else:
            return render_template('fail.html')

        


if __name__=="__main__":
    app.run()