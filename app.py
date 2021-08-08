import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")        

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)

    response = "["
    tup=jsonObj['temp1'].split(";")
    for i in range(len(tup)):
        a = tup[i].split(",")
        b = 0
        for items in a:
            b+=int(items)
        tup[i] = b
    for i in range(len(tup)):
        response+=""+str(tup[i])+""
        if i != len(tup) - 1:
            response+=","
    response+="]"
    return response
    
if __name__ == "__main__":
	app.run()    
