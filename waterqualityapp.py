# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:50:47 2021

@author: A Hari chandana
"""


from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('waterquality.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('indexnew.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    
    x_test = [[int(x) for x in request.form.values()]]
    
    prediction = model.predict(x_test)
    print(prediction)
    output=prediction[0][0]
    return render_template('indexnew.html', 
  prediction_text=
  'Water quality prediction {}'.format(output))
if __name__ == "__main__":
    app.run(debug=True)
