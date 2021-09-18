# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 12:07:37 2021

@author: student
"""

import pickle 
from flask import Flask , render_template, request
 #global variables 
loadedModel = pickle.load(open("loan defaulter.pkl",'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('ilindex.html')
@app.route('/prediction', methods = ['POST'])
def prediction():
    Index = request.form['Index']
    Employed = request.form['Employed']
    AnnualSalary = request.form['Annual Salary']
    BankBalance =  request.form['Bank Balance']
    prediction= loadedModel.predict([[Index,Employed,BankBalance,AnnualSalary]])[0]
    if prediction == 0:
        prediction="The loanee is defaulter"
    else :
        prediction="The loanee is not a defaulter"

    return render_template('ilindex.html', api_output=prediction)

app.run(debug=True)