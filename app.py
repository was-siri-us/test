
from flask import Flask,request,jsonify
import pandas as pd
import joblib

app = Flask(__name__)



@app.route('/api',methods=['GET'])
def returnPred():
    q = str(request.args['query'])
    d = {}
    d['output'] = "pig"
        
        
    return d
    

    




if __name__ == "__main__":
    app.run()














        
