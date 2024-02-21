import os
from flask import Flask, request, jsonify
import pickle
app=Flask(__name__)

clf_path=open("classifier.pkl","rb")
clf=pickle.load(clf_path)

@app.route('/ping')
def printmyname():
    return("hello Amaan")


@app.route('/predict',methods=['POST'])
def prediction():
    loan_req = request.get_json()
    print(loan_req)
    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1
 
    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1
 
    if loan_req['Credit_History'] == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1  

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']

    prediction = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return {"prediction":pred}

if __name__ == "__main__":
    app.run(host="0.0.0.0")
