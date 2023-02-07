
from flask import Flask,request,jsonify
import pandas as pd
import joblib

app = Flask(__name__)



@app.route('/api',methods=['GET'])
def returnPred():
    q = str(request.args['query'])
    d = {}
    if(q[0]=="0"):
        input  = q[:-2]
        answer = [[float(i) for i in input.split(',')]]
        model = joblib.load('./modelLogistic.joblib')
    
        
        
        if(q[-1]=='1'):
            d['a']=1
            model = joblib.load('./modelRF.joblib')
        if(q[-1]=='2'):
            d['a']=2
            model = joblib.load('./modelgBoost.joblib')
        if(q[-1]=='3'):
            d['a']=3
            model = joblib.load('./modelLogistic.joblib')
        if(q[-1]=='4'):
            d['a']=4
            model = joblib.load('./modelSVM.joblib')
        
        out = str(model.predict(answer)[0])
        if(out=="1" or out=="YES" ):
            out ="The Water is Potable"
        else:
            out="The Water is not Potable"
        
        d['output'] =out
    elif(q[0]=='1'):
       d['output'] = 'pig '
        
        
        
    return d
    

    




if __name__ == "__main__":
    app.run()














        