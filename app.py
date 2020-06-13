#from flask_ngrok import run_with_ngrok
from flask import Flask,jsonify
import pickle
import numpy as np
app=Flask(__name__)
#run_with_ngrok(app)
@app.route("/")
def index():
  return "HELLO FROM COLAB"
f=open("model.pkl","rb")
w=pickle.load(f)
@app.route("/<Age>/<Sibsp>/<Parch>/<Fare>/<Gender>/<Pclass>/<Place>")
def predict(Age,Sibsp,Parch,Fare,Gender,Pclass,Place):
  data=[int(Age),int(Sibsp),int(Parch),float(Fare)]
  if Gender.casefold()=='m' or Gender.casefold()=='1':
    data+=[1]
  else:
    data+=[0]
  if Pclass=='2':
    data+=[1,0]
  elif Pclass=='3':
    data+=[0,1]
  else:
    data+=[0,0]
  if Place=="q":
    data+=[1,0]
  elif Place=="s":
    data+=[0,1]
  else:
    data+=[0,0]
  arr=np.array([data])
  pred=w.predict(arr)
  if pred==[1]:
    result={"result":"Survived"}
  else:
    result={"result":"Not Survived"}

  return jsonify(result)

app.run(host='0.0.0.0')
