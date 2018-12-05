import os
from flask import Flask, url_for, render_template, request, redirect, session
from keras3 import train
import numpy as np

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template("home.html", errors="")

def check_value(name, value, min_value, max_value):
    result=""
    try:
        x=float(value)
        if x<min_value or x>max_value:
            result=result+"Error: "+name+" must be in range.<br>"
    except ValueError:
        result=result+"Error: "+name+" must be of type float or int.<br>"
    return result

def validate(gpa, v, q, w, p):
    result=""
    result+=check_value("gpa", gpa, 2.00, 4.00)
    result+=check_value("gre-verbal", v, 130, 170)
    result+=check_value("gre-quntitative", q, 130, 170)
    result+=check_value("gre-writing", w, 0, 6.0)
    result+=check_value("gre-physics", p, 200, 990)
    return result

@app.route("/result")
def render_result():
    #try:
        gpa=request.args["gpa"]
        v=request.args["v"]
        q=request.args["q"]
        w=request.args["w"]
        p=request.args["p"]
        errors=validate(gpa, v, q, w, p)
        if errors=="":
            xx1=[float(gpa)/4.00]
            xx2=[(float(v)-130)/40]      
            xx3=[(float(q)-130)/40]       
            xx4=[float(w)/6.0]      
            xx5=[(float(p)-200)/790]
            data=np.array([xx1,xx2,xx3,xx4,xx5]).transpose()
            result1=train(data)[0]
            result2=train(data)[1]
            result3=train(data)[2]
            return render_template("result.html", result1=result1, \
                                   result2=result2, result3=result3)
        else:
            return render_template("home.html", errors=errors)
    #except ValueError:
        #return "Only valid numbers can be accepted. Please try again."

if __name__ == "__main__":
    app.run(debug=True, port=9999)
