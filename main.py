from functions import *
from flask_cors import CORS,cross_origin
from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/",methods=["POST","GET"])
@cross_origin()
def hello():
    if request.method=="POST":
        link=request.form.get('link')
        data=[]
        get_data(link,data)
        return render_template("index.html",data=data)
    return render_template("index.html",data=[[]])
if __name__=="__main__":
    app.run(debug=True,host="127.0.0.1",port=8000)